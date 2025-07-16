from flask import Flask, request, Response, render_template, jsonify
import os
from io import BytesIO
from gtts import gTTS

app = Flask(__name__)

@app.route("/")
def post():
    if request.method == 'GET':
        return render_template('index.html', title="Flask Example", name="은룡")
    if request.method == 'POST':
        try:
            text = request.form.get('input_text', '').strip()
            lang = request.form.get('lang', 'ko')

            if not text:
                return jsonify({"error": "텍스트가 비어 있습니다."}), 400

            fp = BytesIO()
            tts = gTTS(text=text, lang=lang, tld="com")
            tts.write_to_fp(fp)
            fp.seek(0)
            return Response(fp.getvalue(), mimetype='audio/mpeg')
        
        except Exception as e:
            return jsonify({"error": f"gTTS 변환 실패: {str(e)}"}), 500


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)