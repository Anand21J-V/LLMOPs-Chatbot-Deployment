# 🧞 ChatGenie – Your Friendly LLM Chatbot with Groq & Flask

Welcome to **ChatGenie**, a lightweight, fast, and deeply human-like chatbot app built using **Flask** and **Groq's LLaMA 3.3-70B-Versatile** model. This project demonstrates how to build and deploy a production-grade chatbot UI powered by state-of-the-art LLM APIs in a minimal Flask application – a great entry into the world of **LLMOps**.

---

## 🚀 Features

- 🔮 **ChatGenie Personality**: Helpful, warm, and expressive conversational tone
- ⚡ **Groq LLaMA 3.3-70B**: Uses Groq’s blazing-fast inference API
- 🧠 **System Prompt Engineering**: Tailored behavior using smart prompt setup
- 🌐 **Web UI via Flask**: Clean and minimal HTML frontend
- 🔐 **.env-based Configuration**: Keeps API keys safe and manageable

---

## 📁 Project Structure

chatgenie/
├── app.py # Main Flask app logic
├── templates/
│ └── index.html # HTML template
├── .env # API keys and secrets
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/chatgenie.git
cd chatgenie
2. Install Dependencies
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Create a .env File
env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
💡 Get your Groq API key from: https://console.groq.com/

4. Run the Flask App
bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

🌟 How It Works
User submits a question via a form on the webpage.

The Flask app sends the message to Groq’s LLaMA-3.3-70B-Versatile model.

Groq returns a response crafted with our system prompt personality.

The chatbot displays both the user’s query and the AI's response.

📦 Dependencies
Flask

python-dotenv

groq (official Groq Python client)

datetime (built-in)

Install with:

bash
Copy
Edit
pip install flask python-dotenv groq
🧠 LLMOps Concepts Demonstrated
API orchestration and environment setup

System prompt engineering

Server setup with Flask

Error handling for inference failures

Token/temperature tuning for creative responses

📌 Future Enhancements
Session history & multi-turn memory

Streaming responses

User auth & rate-limiting

Deploy via Gunicorn + NGINX on AWS EC2

🛡️ License
MIT License

🙌 Acknowledgements
Groq API

Meta’s LLaMA Models

Flask & Jinja2 templating
