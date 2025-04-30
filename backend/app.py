from flask import Flask, request, jsonify
from flask_cors import CORS
from run_mmrag import generate_clinical_documentation

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("message", "")

    if not query:
        return jsonify({"error": "Empty query"}), 400

    try:
        result = generate_clinical_documentation(query)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
