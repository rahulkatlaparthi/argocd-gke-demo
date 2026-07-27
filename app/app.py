from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version 2 deployed from GitHub Feature Branch!"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/version")
def version():
    return {"version": "v1"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
