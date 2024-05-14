from backend.utils.data_processing import load_data, preprocess_data

products = load_data("./data/sephora_products_dataset.csv")
reviews = load_data("./data/sephora_reviews_dataset.csv")

features_df = preprocess_data(products, reviews)
print(features_df)
