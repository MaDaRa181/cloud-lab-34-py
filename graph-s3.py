import matplotlib.pyplot as plt

s3.download_file(bucket_name, "nbu_2025.csv", "downloaded_nbu_2025.csv")
df_plot = pd.read_csv("downloaded_nbu_2025.csv")

df_plot["exchangedate"] = pd.to_datetime(df_plot["exchangedate"], format="%d.%m.%Y")

plt.figure(figsize=(12, 6))
plt.plot(
    df_plot["exchangedate"], df_plot["rate"], label="Курс USD до UAH", color="blue"
)
plt.title("Курс долара США за 2025 рік")
plt.xlabel("Дата")
plt.ylabel("Курс (UAH)")
plt.grid(True)
plt.legend()

plt.savefig("usd_rate_2025.png")
s3.upload_file("usd_rate_2025.png", bucket_name, "usd_rate_2025.png")
print("Графік вивантажено на S3")
