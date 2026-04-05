from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Example blueprint registration
from your_blueprint_module import your_blueprint
app.register_blueprint(your_blueprint)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)