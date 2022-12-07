from flask import Flask, render_template,request
from script import resolute
import os


app = Flask(__name__)
IMG_FOLDER = os.path.join('static','IMG')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        inp = request.form.to_dict()
        numb = inp['phNo']
        resolute(0,0,numb)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)