import pandas as pd

data = pd.read_csv('sales_data.csv')

# menampilkan 5 baris pertama
print(data.head(5))

# menampilkan informasi dataset
print("Sales Data Dataset:\n")
data.info()

# menghitung total unit terjual dari SALES column
print(f"\nTotal Sales: {data['SALES'].sum()}")

# menghitung rata-rata unit terjual per transaksi
print(f"Rata-rata unit terjual: {data['QUANTITYORDERED'].mean()}")