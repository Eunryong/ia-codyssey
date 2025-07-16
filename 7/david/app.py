from flask import Flask, request, Response, render_template, jsonify
import os
from io import BytesIO
from gtts import gTTS

app = Flask(__name__)

VALID_LANGS = ["ko", "en", "ja", "es"]

@app.route("/", methods=["GET", "POST"])
def post():
    if request.method == 'GET':
        return render_template('index.html', title="Flask Example", name="은룡")
    elif request.method == 'POST':
        try:
            text = request.form.get('input_text', '').strip()
            lang = request.form.get('lang', 'ko')

            if not text:
                return jsonify({"error": "텍스트가 비어 있습니다."}), 400
            if lang not in VALID_LANGS:
                return jsonify({"error": f"잘못된 언어 코드입니다. 허용: {', '.join(VALID_LANGS)}"}), 400
            
            fp = BytesIO()
            tts = gTTS(text=text, lang=lang, tld="com")
            tts.write_to_fp(fp)
            fp.seek(0)
            
            import base64
            audio_base64 = base64.b64encode(fp.getvalue()).decode("utf-8")

            image_url = "/static/david.jpg"
            with open(IMAGE_MAP.get(lang, image_url), "rb") as f:
                image_base64 = base64.b64encode(f.read()).decode("utf-8")

            return jsonify({
                "audio": audio_base64,
                "image": image_base64,
                "lang": lang
            })
        except Exception as tts_error:
            return jsonify({"error": f"음성 변환 중 오류 발생: {str(tts_error)}"}), 500

        except Exception as e:
            return jsonify({"error": f"gTTS 변환 실패: {str(e)}"}), 500


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)