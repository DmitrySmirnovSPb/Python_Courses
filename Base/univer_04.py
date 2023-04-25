from sklearn.decomposition import TruncatedSVD, PCA

import numpy as np

m = np.random.rand(50, 10)
print(m)

import pandas as pd

data = pd.DataFrame(m)
print(data.head(5))

svd = TruncatedSVD(5)
svd.fit(data)
TruncatedSVD(n_components=5)
new_m = svd.transform(data)
new_data = pd.DataFrame(new_m)

print(new_m)
print(new_data)