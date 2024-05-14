from backend.models.knn_model import KNNModel
from backend.utils.recommendation import get_top_recommendations

knn_model = KNNModel()

product_id = "P422510"
k_recommendations = 6

recommendations = get_top_recommendations(product_id, knn_model, k_recommendations)

print(recommendations)