from flask import Flask, render_template,request
from script import resolute, shaper
import os
import base64, io
from PIL import Image


app = Flask(__name__)
IMG_FOLDER = os.path.join('static','IMG')
global token
token = False

@app.route('/')
def home():
    cacheWipe()
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        inp = request.form.to_dict()
        numb = inp['phNo']
        resolute(0,0,numb)
        encoded_img_data=showOnWeb(token=True)
        cacheWipe()
    return render_template('index.html', img_data=encoded_img_data.decode('utf-8'))


def showOnWeb(token):
    if(token):
        im=Image.open("foo.png")
        data = io.BytesIO()
        im.save(data, "PNG")
        encoded_img_data = base64.b64encode(data.getvalue())
        return encoded_img_data


def cacheWipe():
    if os.path.exists("foo.png"):
        os.remove('foo.png')
    else:
        print('cache clean')


if __name__ == '__main__':
    app.run(debug=True)