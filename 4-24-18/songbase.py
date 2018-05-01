from Flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    #return HTML
    return "<h1>this is the index page!<h1>"
