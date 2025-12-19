from flask import Flask, render_template,  request
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        completion = client.chat.completions.create(
            model = "gpt-4.1-mini",
            messages = [{"role":"system", "content": "you are a helpful assistant"},{"role":"user", "content": user_input}]
        )
        response = completion.choices[0].message.content
    return render_template("index.html", response = response)
    
if __name__ == "__main__":
    app.run(debug = True)