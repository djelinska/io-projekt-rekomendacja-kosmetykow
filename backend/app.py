from backend.models.knn_model import KNNModel
from backend.utils.data_processing import load_data, preprocess_data

products = load_data("./data/sephora_products_dataset.csv")
reviews = load_data("./data/sephora_reviews_dataset.csv")

features_df = preprocess_data(products, reviews)
print(features_df)

product_id = "P422510"
k_recommendations = 6

knn_model = KNNModel()
knn_model.train(features_df)
neighbor_indices = knn_model.get_neighbors(features_df, product_id, k_recommendations)

print(neighbor_indices)
