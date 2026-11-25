from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        application="Nilesh's DevOps Automation Platform",
        message="Welcome Nilesh! Your application has been successfully deployed through CI/CD.",
        tagline="Build. Test. Deploy. Automate.",
        status="running",
        developer="Nilesh Katalkar"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)