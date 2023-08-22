# import flask
from flask import Flask

# create flask instance

app = Flask(__name__)
# print name
print(__name__)

@app.route('/index')
def index():
     return '<html><head><title>Hotels</title></head><body><h1>Hello</h1></body></html>'

if __name__ == "__main__":
     app.run(debug=True)
     