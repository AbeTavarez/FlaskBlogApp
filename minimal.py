from flask import Flask

app = Flask(__name__)

# Home Page
@app.route('/')
def main():
    return 'HOME PAGE'


# Blog
@app.route('/blog')
def blog_page():
    return 'BLOG PAGE'
