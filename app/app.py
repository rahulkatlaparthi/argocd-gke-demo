from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask running on GKE using Helm + Argo CD!"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/version")
def version():
    return {"version": "v1"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
