from flask import Flask,render_template,redirect,request
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
api_key = os.getenv("GOOGLE_API")
client = genai.Client(api_key=api_key)
chat_history = []


@app.route("/", methods=["POST","GET"])
def chat():
    global chat_history
    if request.method == "POST":
        user_input = request.form.get("message")

        if user_input:

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=user_input
            )
            chat_history.append(("You: ",user_input))
            chat_history.append(("AI: ",response.text))

    return render_template("index.html",chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
