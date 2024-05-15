from backend.utils.data_processing import load_data, preprocess_data


def get_top_recommendations(product_id, knn_model, k=3):
    products = load_data("./data/sephora_products_dataset.csv")
    reviews = load_data("./data/sephora_reviews_dataset.csv")

    _, features_df = preprocess_data(products, reviews)

    knn_model.train(features_df)

    neighbor_indices = knn_model.get_neighbors(features_df, product_id, k)

    recommendations = []
    for i in range(0, k):
        neighbor_index = neighbor_indices.flatten()[i]
        neighbor_product_id = features_df.index[neighbor_index]

        recommendations.append(neighbor_product_id)

    return recommendations
