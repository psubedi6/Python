import pandas as pd
import numpy as np
df = pd.read_csv("Countries.csv")
print(df)

#which country has the highest population 
high_pop = df.loc[df["population"].idxmax()]
high_pop_country = high_pop["country"]
print(f"Country with highest population is: {high_pop_country}")

#which is the capital of the country with high pupulation
high_pop_capital = high_pop["capital_city"]
print(f"The capital of the country with high pupulation is: {high_pop_capital}")

#which country has least population
low_pop= df.loc[df["population"].idxmin()]
low_pop_country = low_pop["country"]
print(f"The country with low population is: {low_pop_country}")

#what is the capital of a country with lowest population
low_pop_capital= low_pop["capital_city"]
print(low_pop_capital)

#give me top 5 countries with highest democratic score:
high5_demo = df.sort_values(by = "democracy_score", ascending = False).head(5)
high_demo_con = high5_demo["country"]
print(high_demo_con)

#how many total regions are there
region_count = df["region"].nunique()
print("Total unique regions:", region_count)

#how many countries lie in Eastern Europe region
print((df["region"] == "Eastern Europe").sum())

#who is the political leader of second highest populated country
leader_second_pop = df.nlargest(2, "population").iloc[1]["political_leader"]
print(leader_second_pop)

#how many countries are there whose political leader is unknown
print(df["political_leader"].isna().sum())

#how many countries have republic in their full name
print((df["country_long"].str.contains("Republic")).sum())

#which country in african region has highest population
africa_df = df[(df["continent"] == "Africa")]
print(africa_df.loc[africa_df["population"].idxmax(), "country"])