import pandas as pd
import numpy as np

n = 5000

data = {
    "Time": np.random.randint(0, 100000, n),
    "Amount": np.random.uniform(1, 2000, n),
}

# Add V1–V28
for i in range(1, 29):
    data[f"V{i}"] = np.random.normal(0, 1, n)

# Fraud (1%) 
data["Class"] = np.random.choice([0, 1], n, p=[0.98, 0.02])

df = pd.DataFrame(data)
df.to_csv("data/creditcard_fake.csv", index=False)

print("Dataset created!")