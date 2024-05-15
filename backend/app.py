import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.models.knn_model import KNNModel
from backend.utils.data_processing import load_data, preprocess_data
from backend.utils.recommendation import get_top_recommendations

app = Flask(__name__)
CORS(app)

knn_model = KNNModel()


@app.route("/products", methods=["GET"])
def get_popular_products():
    products_df = load_data("./data/sephora_products_dataset.csv")
    reviews_df = load_data("./data/sephora_reviews_dataset.csv")

    popular_products_df, _ = preprocess_data(products_df, reviews_df)

    merged_df = pd.merge(products_df, popular_products_df, on="product_id", how="inner")

    filtered_products_df = merged_df[["product_id", "product_name", "brand_name", "rating", "reviews", "price_usd", "primary_category"]]
    filtered_products = filtered_products_df.to_dict(orient="records")

    return jsonify(filtered_products), 200


@app.route("/recommend",  methods=["GET"])
def recommend():
    product_id = request.args.get("product_id")
    recommendation_count = request.args.get("recommendation_count")

    if product_id is None:
        return jsonify({"error": "Niepoprawny identyfikator produktu"}), 404

    if recommendation_count is not None and 2 <= int(recommendation_count) <= 7:
        recommendation_count = int(recommendation_count)
    else:
        recommendation_count = 7

    recommendations_ids = get_top_recommendations(product_id, knn_model, recommendation_count)

    products_df = load_data("./data/sephora_products_dataset.csv")

    filtered_products_df = products_df[products_df["product_id"].isin(recommendations_ids)][
        ["product_id", "product_name", "brand_name", "rating", "reviews", "price_usd", "primary_category"]]
    filtered_products = filtered_products_df.to_dict("records")

    return jsonify(filtered_products), 200


if __name__ == "__main__":
    app.run(debug=True)
