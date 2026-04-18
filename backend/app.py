from flask import Flask, request, jsonify
from ai_engine.face_match import verify_face, display_images


app = Flask(__name__)


@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/match", methods=["POST"])
def match_face():
    """
    API endpoint to check face match.
    Expects JSON with 'input_image' and 'database_path'.
    """
    try:
        data = request.get_json()

        if not data or "input_image" not in data or "database_path" not in data:
            return jsonify({"error": "Missing input_image or database_path"}), 400

        input_image = data["input_image"]
        database_path = data["database_path"]

        # 🔎 Debug prints to confirm paths
        import os
        print("Input image path:", input_image)
        print("Database path:", database_path)
        print("Does input image exist?", os.path.exists(input_image))

        print("----------------------------------------------------------------------------------------------")


        matched_image, score = verify_face(input_image, database_path)

        if matched_image:
            match_percentage = (1 - score) * 100
            # Display images side by side (optional, for manual check)
            display_images(input_image, matched_image)

            return jsonify({
                "matched_image": matched_image,
                "match_score": score,
                "match_percentage": f"{match_percentage:.2f}%"
            })
        else:
            return jsonify({"message": "No match found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)