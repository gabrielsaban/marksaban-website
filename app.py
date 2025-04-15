from flask import Flask, render_template, send_from_directory, request
import datetime
import os
import markdown

app = Flask(__name__, 
            template_folder='src',
            static_folder='src')

# Add custom Jinja filter for current year
@app.template_filter('now')
def _now(format_):
    return datetime.datetime.now().strftime(format_)

# Function to read markdown files
def read_markdown_file(filename):
    """Read a markdown file and convert to HTML."""
    file_path = os.path.join('src', 'text', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Convert markdown to HTML
            html_content = markdown.markdown(content)
            return html_content
    return ""

# Register a new path for templates
app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'src/templates'))

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', request=request)

@app.route('/contact.html')
def contact():
    return render_template('contact.html', request=request)

@app.route('/psychotherapy.html')
def psychotherapy():
    return render_template('psychotherapy.html', request=request)

@app.route('/links.html')
def links():
    # Read markdown content
    tautegorical_content = read_markdown_file('tautegorical.md')
    theatre_content = read_markdown_file('theatre.md')
    playing_content = read_markdown_file('playing.md')
    dreamwork_content = read_markdown_file('dreamwork.md')
    
    return render_template('links.html', 
                          request=request,
                          tautegorical_content=tautegorical_content,
                          theatre_content=theatre_content,
                          playing_content=playing_content,
                          dreamwork_content=dreamwork_content)

# Serve static files from src directory
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(os.path.join('src', 'css'), filename)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(os.path.join('src', 'images'), filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory(os.path.join('src', 'js'), filename)

# Serve PDF files from the text directory
@app.route('/text/<path:filename>')
def text_files(filename):
    return send_from_directory(os.path.join('src', 'text'), filename)

# Public files
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('public', 'favicon.ico')

# Serve robots.txt and sitemap.xml
@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('public', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory('public', 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True, port=3000) 