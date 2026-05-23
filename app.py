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
            chat_history.append({"role": "user", "content":user_input})

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=[msg["content"] for msg in chat_history]
            )
            #chat_history.append(("You: ",user_input))
            #chat_history.append(("AI: ",response.text))
            #chat_history.append({"role":"ai","content":ai_reply})
            ai_reply = response.text
            chat_history.append({"role":"ai","content":ai_reply})

    return render_template("index.html",chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
