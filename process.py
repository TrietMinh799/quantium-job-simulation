import pandas as pd

data_0 = pd.read_csv("./data/daily_sales_data_0.csv")
data_1 = pd.read_csv("./data/daily_sales_data_1.csv")
data_2 = pd.read_csv("./data/daily_sales_data_2.csv")

data_0 = data_0.query("product == 'pink morsel'")
data_1 = data_1.query("product == 'pink morsel'")
data_2 = data_2.query("product == 'pink morsel'")


data = pd.concat([data_0, data_1, data_2], ignore_index=True)
data["sales"] = data["price"].str[1:].astype(float) * data["quantity"].astype(float)
data.drop(columns=["price", "quantity"], inplace=True)
data.drop("product", axis=1, inplace=True)
data = data.iloc[:, [2, 0, 1]]

print(data.head())
data.to_csv("./formatted.csv", index=False)
