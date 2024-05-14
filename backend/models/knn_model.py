from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


class KNNModel:
    def __init__(self):
        self.model = NearestNeighbors(metric='cosine', algorithm='brute')

    def train(self, features_df):
        features_df_matrix = csr_matrix(features_df.values)

        self.model.fit(features_df_matrix)

    def get_neighbors(self, features_df, product_id, k):
        product_index = features_df.index.get_loc(product_id)

        distances, indices = self.model.kneighbors(features_df.iloc[product_index, :].values.reshape(1, -1), n_neighbors=k)

        return indices
