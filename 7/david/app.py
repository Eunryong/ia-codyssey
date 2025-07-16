from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/", methods=['GET'])
def get():

    return render_template('index.html', title="Flask Example", name="은룡")
    
@app.route("/", methods=['POST'])
def post():
    try:
        data = request.get_json()
        text = data.form.get('input_text')

        lang = request.args.get('lang', data.form.get('lang'))
        fp = BytesIO()
        gTTS(text, "com", lang).write_to_fp(fp)

        return Response(fp.getvalue(), mimetype='audio/mpeg')
    except


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)