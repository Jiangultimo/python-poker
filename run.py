from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from flask import render_template
from BeginSpider import bilibiliCid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="index")

@app.route('/getBilibiliCid', methods=['POST'])
def get_bilibili_cid():
    if request.method == 'POST':
        aid = request.form.get('aid')
        responseText = {
            'code': 200,
            'lists': bilibiliCid.get_bilibili_cid(aid)
        }
        return make_response(jsonify(responseText))

if __name__ == '__main__':
    app.run(debug=True)
