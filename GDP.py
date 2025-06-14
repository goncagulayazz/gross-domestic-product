
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry

sns.set(style="whitegrid")

df = pd.read_csv("https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv")
df.head()
# Get ISO3 codes of real countries using pycountry
country_codes = {country.alpha_3 for country in pycountry.countries}

# Check column names
print(df.columns)

# Since data contains multiple years, filter for 2019 data only
df_2019 = df[df['Year'] == 2019]

# Filter only real countries' data
df_2019_countries = df_2019[df_2019['Country Code'].isin(country_codes)]

# Select top 10 countries by GDP value
df_2019_sorted = df_2019_countries.sort_values(by="Value", ascending=False).head(10)
print(df_2019_sorted[['Country Name', 'Value']])

# Plot the top 10 countries by GDP per capita in 2019
plt.figure(figsize=[12, 8])
sns.barplot(x="Value", y="Country Name", data=df_2019_sorted, hue="Country Name", palette="viridis", legend=False)
plt.title("Top 10 Countries by GDP per Capita in 2019", fontsize=14)
plt.xlabel("GPD per Capita(USD)", fontsize=12)
plt.ylabel("Country Name", fontsize=12)
plt.show()



