from flask import Flask, render_template, request
from llm_assistant import generate_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title = code = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            title, code = generate_code(prompt)
    return render_template("index.html", title=title, code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
