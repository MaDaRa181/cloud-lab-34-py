import requests
import pandas as pd

url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250101&end=20251231&valcode=usd&sort=exchangedate&order=asc&json"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df.to_csv('nbu_2025.csv', index=False)