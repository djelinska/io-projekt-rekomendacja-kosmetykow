from flask import Flask, request, jsonify
from backend.models.knn_model import KNNModel
from backend.utils.recommendation import get_top_recommendations

app = Flask(__name__)

knn_model = KNNModel()


@app.route("/recommend",  methods=['GET'])
def recommend():
    product_id = request.args.get("product_id")
    recommendation_count = request.args.get("recommendation_count")

    if product_id is None:
        return jsonify({"error": "Niepoprawny identyfikator produktu"})

    if recommendation_count is not None and 2 <= int(recommendation_count) <= 7:
        recommendation_count = int(recommendation_count)
    else:
        recommendation_count = 3

    recommendations = get_top_recommendations(product_id, knn_model, recommendation_count)

    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(debug=True)
