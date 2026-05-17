from flask import Flask, Response, redirect, render_template, send_from_directory, request
import datetime
import os
import markdown
from functools import lru_cache
from flask_compress import Compress

app = Flask(__name__, 
            template_folder='src',
            static_folder='src')

# Add gzip compression
compress = Compress(app)

SITE_URL = "https://marksaban.co.uk"
SITEMAP_PAGES = (
    ("/", "1.00"),
    ("/contact", "0.80"),
    ("/psychotherapy", "0.80"),
    ("/resources", "0.80"),
)

# Add custom Jinja filter for current year
@app.template_filter('now')
def _now(format_):
    return datetime.datetime.now().strftime(format_)

# Function to read markdown files with caching
@lru_cache(maxsize=32)
def read_markdown_file(filename):
    """Read a markdown file and convert to HTML with caching."""
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

def static_response(directory, filename, max_age=31536000):
    """Serve static assets with cache headers for faster repeat visits."""
    return send_from_directory(directory, filename, max_age=max_age)


@app.route('/')
def index():
    return render_template('index.html', request=request)

@app.route('/index.html')
def legacy_index():
    return redirect('/', code=301)

@app.route('/contact')
def contact():
    return render_template('contact.html', request=request)

@app.route('/contact.html')
def legacy_contact():
    return redirect('/contact', code=301)

@app.route('/psychotherapy')
def psychotherapy():
    return render_template('psychotherapy.html', request=request)

@app.route('/psychotherapy.html')
def legacy_psychotherapy():
    return redirect('/psychotherapy', code=301)

@app.route('/resources')
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

@app.route('/links.html')
def legacy_links():
    return redirect('/resources', code=301)

# Health check endpoint for UptimeRobot
@app.route('/ping')
def ping():
    return "OK", 200

# Serve static files from src directory
@app.route('/css/<path:filename>')
def css(filename):
    return static_response(os.path.join('src', 'css'), filename)

@app.route('/images/<path:filename>')
def images(filename):
    return static_response(os.path.join('src', 'images'), filename)

@app.route('/js/<path:filename>')
def js(filename):
    return static_response(os.path.join('src', 'js'), filename)

# Serve PDF files from the text directory
@app.route('/text/<path:filename>')
def text_files(filename):
    return static_response(os.path.join('src', 'text'), filename, max_age=604800)

# Public files
@app.route('/favicon.ico')
def favicon():
    return static_response('public', 'favicon.ico')

# Serve robots.txt and sitemap.xml
@app.route('/robots.txt')
def robots_txt():
    robots = f"User-agent: *\nDisallow:\nSitemap: {SITE_URL}/sitemap.xml\n"
    return Response(robots, mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap_xml():
    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"""<url>
  <loc>{SITE_URL}{path}</loc>
  <lastmod>{today}</lastmod>
  <priority>{priority}</priority>
</url>"""
        for path, priority in SITEMAP_PAGES
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    return Response(sitemap, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True, port=3000) 
