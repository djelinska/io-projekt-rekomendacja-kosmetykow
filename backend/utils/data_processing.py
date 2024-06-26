import pandas as pd
import numpy as np


def load_data(data_filename):
    data = pd.read_csv(data_filename, low_memory=False)

    return data


def preprocess_data(products_df, reviews_df, rating_count_threshold=2500):
    products_selected_cols = products_df[["product_id", "product_name"]]
    reviews_selected_cols = reviews_df[["author_id", "rating", "product_id"]]

    print(products_selected_cols.info())
    print(reviews_selected_cols.info())

    merged_df = pd.merge(reviews_selected_cols, products_selected_cols, on="product_id")

    print(merged_df.isna().sum())
    # dataset nie zawiera pustych wartości w kolumnach

    print(merged_df.kurt(numeric_only=True))
    # jedyną numeryczną kolumną jest kolumna "rating"

    print(merged_df['rating'].describe())
    # maksymalna wartość to 5.0, minimalna to 1.0, zatem kolumna nie zawiera wartości odstających

    product_rating_counts = merged_df.groupby("product_id")["rating"].count().reset_index()
    product_rating_counts.rename(columns={"rating": "total_rating_count"}, inplace=True)

    popular_products_df = product_rating_counts[product_rating_counts["total_rating_count"] >= rating_count_threshold]

    merged_with_threshold_df = merged_df[merged_df["product_id"].isin(popular_products_df["product_id"])]

    features_df = merged_with_threshold_df.pivot_table(index="product_id", columns="author_id", values="rating").fillna(0)

    return popular_products_df, features_df


# products = load_data("../data/sephora_products_dataset.csv")
# reviews = load_data("../data/sephora_reviews_dataset.csv")
# preprocess_data(products, reviews)
