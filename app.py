# app.py
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    text_input = request.form['text_input']
    # summarizer logic 
    return redirect(url_for('summarizer_page', text= text_input))

@app.route('/summarizer_page/<text>')
def summarizer_page(text):
    return render_template('summarizer_page.html', text=text)

# Add a new route for the 'about' page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


# Add your OpenAI summarization logic here
def generate_summary(text):
    response = requests.post(
        "http://127.0.0.1:5000/generate_summary",  # Change this URL based on your Flask app's deployment
        json={"text": text},
    )
    return response.json()["summary"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/summarizer_page", methods=["POST"])
def summarize():
    text_input = request.form["text_input"]
    summary = generate_summary(text_input)
    return redirect(url_for("summarizer_page.html", text=summary))


@app.route("/summarizer_page/<text>")
def summarizer_page(text):
    return render_template("summarizer_page.html", text=text)


# Add a new route for the 'about' page
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
