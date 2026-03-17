import numpy as np
import pandas as pd

df = pd.read_csv("anime.csv")
print(df)

#make a new column for episode count
df["Episodes"] = df ["Title"].str.extract(r"\((\d+)\s+eps\)")

#make a new column for time stamp
df["Time Stamp"] = df["Title"].str.extract(r"([A-Za-z]{3}\s\d{4}\s-\s[A-Za-z]{3}\s\d{4})")

#which anime has the highest score
high_score= df.loc[df["Score"].idxmax()]
print(high_score)

#give me top 5 highest scoring anime
top5_score = df.sort_values(by= "Score", ascending= False).head(5)
print(top5_score)

#which anime has the highest episode count
high_episode = df.loc[df["Episodes"].idxmax()]
print(high_episode)

#animes with top 5 episode count
df["Episodes"] = df["Episodes"].astype(int)
top5_anime= df.sort_values(by="Episodes", ascending= False).head(5)
print(top5_anime)

#which is the longest running anime
df["Start year"]= df["Time Stamp"].str.extract(r"(\d{4})").astype(int)
df["End year"] = df ["Time Stamp"].str.extract(r"-\s[A-Za-z]{3}\s(\d{4})").astype(int)
df["Months"]= ((df["End year"]- df["Start year"])*12).astype(int)
longest= df.sort_values(by= "Months", ascending = False).head(2)
print(longest)
df["Title"] = df["Title"].str.split("(").str[0].str.strip()
print(df)