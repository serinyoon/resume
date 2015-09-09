from flask import Flask, render_template
import os
import json
app = Flask(__name__)

def initialize():
    filepath = os.getcwd() + '/content.json'
    data = json.load(open(filepath))
    print filepath
    return data

@app.route('/')
def resume():
    data = initialize()
    return render_template('resume.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)