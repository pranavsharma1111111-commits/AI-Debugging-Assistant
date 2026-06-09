from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os
app = Flask(__name__)
CORS(app)
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/analyze", methods=["POST"])
def analyze_code():

    try:
        data = request.json
        code = data.get("code")
        language = data.get("language")
        if not code:
            return jsonify({
                "result": "No code provided."
            })

        prompt = f"""
You are an AI debugging assistant.

Analyze the following {language} code.

Return output EXACTLY in this format:

ERROR:
...

EXPLANATION:
...

FIXED CODE:
...

Rules:
- Be short and direct.
- Find syntax or logic errors.
- Mention line/problem clearly.
- Explain simply in 1-2 sentences.
- Provide corrected code.
- Avoid long teaching paragraphs.

Code:
{code}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("===== GEMINI RESPONSE =====")
        print(response.text)

        return jsonify({
            "result": response.text
        })

    except Exception as e:

        print("===== ERROR =====")
        print(str(e))

        return jsonify({
            "result": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)