from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from BeginSpider import bilibiliCid

app = Flask(__name__)
print(Flask)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

@app.route('/getBilibiliCid', methods=['GET'])
def get_bilibili_cid():
    if request.method == 'GET':
        print(bilibiliCid.get_bilibili_cid('78'))
        responseText = {
            'code': 200,
            'lists':bilibiliCid.get_bilibili_cid('78')
        }
        return make_response(jsonify(responseText))

if __name__ == '__main__':
    app.run(debug=True)
