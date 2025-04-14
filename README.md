# Mark Saban Site

Personal website for Mark Saban, psychotherapist and Jungian analyst.

## Site Structure

- `src/` - Contains all website source files
  - `templates/` - Base template used by all pages
  - `css/` - CSS stylesheets (styles.css, links.css)
  - `js/` - JavaScript files (links.js, contact.js)
  - `images/` - Website images
  - HTML files: index.html, contact.html, psychotherapy.html, links.html
- `public/` - Contains public assets
  - `favicon.ico` - Site favicon
  - `robots.txt` - Instructions for search engine crawlers
  - `sitemap.xml` - XML sitemap for search engines

## Technical Information

The site uses:
- Jinja2 templates with a Flask server for development
- Responsive design with modern CSS
- Leaflet.js for the map on the contact page
- Schema.org structured data for SEO
- Open Graph tags for social media sharing

## Development Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run development server:
```
python app.py
```

3. View the site at [http://localhost:3000](http://localhost:3000)

## SEO Optimizations

- Proper meta descriptions and keywords
- Valid robots.txt and XML sitemap
- Structured data (JSON-LD) for better search results
- Open Graph tags for social sharing
- Canonical URLs to prevent duplicate content
