from flask import Flask, render_template, send_from_directory, request
import datetime
import os

app = Flask(__name__, 
            template_folder='src',
            static_folder='src')

# Add custom Jinja filter for current year
@app.template_filter('now')
def _now(format_):
    return datetime.datetime.now().strftime(format_)

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
    return render_template('links.html', request=request)

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