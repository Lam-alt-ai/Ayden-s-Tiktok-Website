"""
Ayden's TikTok Marketing Services Website
Simple Flask server for personal marketing website
"""
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Main landing page"""
    return render_template('ayden_index.html')

@app.route('/styles.css')
def styles():
    """Serve CSS file"""
    return send_from_directory('.', 'ayden_styles.css', mimetype='text/css')

@app.route('/script.js')
def script():
    """Serve JavaScript file"""
    return send_from_directory('.', 'ayden_script.js', mimetype='application/javascript')

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return {'status': 'active', 'service': 'Ayden TikTok Marketing'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)