#!flask/bin/python
from flask import Flask
from main import generate

app = Flask(__name__)

@app.route('/create/<string:vid_name>/', methods=["GET"])
def generateVid(vid_name):
    return generateVideo(vid_name) 

if __name__ == '__main__':
    app.run(debug=True)