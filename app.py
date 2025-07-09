import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime

# === Load environment variables from .env ===
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("Missing GROQ_API_KEY in .env file")

# === Initialize Flask app and Groq client ===
app = Flask(__name__)
groq_client = Groq(api_key=groq_api_key)

# === Main route for GET and POST requests ===
@app.route("/", methods=["GET", "POST"])
def index():
    user_msg = ""
    bot_response = ""
    now = datetime.now()

    if request.method == "POST":
        user_msg = request.form.get("query", "").strip()
        if user_msg:
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",  # ✅ Valid Groq model
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are ChatGenie, a deeply thoughtful and relatable AI assistant. "
                                "You speak with clarity, creativity, and charm. "
                                "You don't give generic answers – instead, you break down concepts like a passionate teacher, "
                                "using analogies, real-life examples, and clear step-by-step reasoning. "
                                "Avoid being robotic. Make the user feel like they're talking to a knowledgeable friend."
                            )
                        },
                        {
                            "role": "user",
                            "content": user_msg
                        }
                    ],
                    temperature=0.8,
                    max_tokens=512
                )
                bot_response = response.choices[0].message.content.strip()
            except Exception as e:
                bot_response = f"❌ Oops, something went wrong: {e}"

    return render_template(
        "index.html",
        user_msg=user_msg,
        bot_response=bot_response,
        now=now
    )

# === Run the app ===
if __name__ == "__main__":
    app.run(debug=True, port=5000)
