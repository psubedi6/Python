import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("/Users/prakashsubedi/Desktop/Python/Matplotlib_Seaborn/Ipl_cricket_project/IPL.csv")
print(df.head())

#check the rows and column in a dataset
print(f"The rows are {df.shape[0]} and the columns are {df.shape[1]}")

#how many columns have null values in total
print(df.isnull().sum())

#toss decison trends
sns.countplot(x = df["toss_decision"],palette = "mako")
plt.title("Toss decison")
plt.xlabel("decisions")
plt.ylabel("wins")
plt.show()

#Toss winner vs match winner
result = (df["toss_winner"] == df["match_winner"]).value_counts()
plt.xticks(ticks=[0,1], labels=["Lost", "Win"])
sns.barplot(x = result.index, y = result.values, palette= "muted")
plt.title("Toss winner vs match winner")
plt.xlabel("win and lost")
plt.ylabel("chances to win")
plt.show()

#how do teams wim?(Runs vs wicket)
result = df["won_by"].value_counts()
sns.barplot(result, palette= "rainbow")
plt.title("Run vs wicket winner")
plt.xlabel("wins by")
plt.ylabel("wins count")
plt.show()

#most player of the match award winner
player_of_the_match = df["player_of_the_match"].value_counts().head(5)
sns.barplot(y=player_of_the_match.index, x= player_of_the_match.values)
plt.title("Most man of the match")
plt.xlabel("wins by")
plt.ylabel("wins count")
plt.show()

#top scorer
highscores= df.groupby("top_scorer")["highscore"].sum().sort_values(ascending = False).head(5)
highscores.plot(
    kind = "barh", 
    color = ["red", "blue", "green", "orange", "purple"]
)
plt.title("Top scorers")
plt.ylabel("players name")
plt.xlabel("players score")
plt.show()

#best bowling figure
df["highest_wicket"]= df["best_bowling_figure"].str.extract(r"(\d+)").astype(int)
highscore= df.groupby("best_bowling")["highest_wicket"].sum().sort_values(ascending= False).head(5)
highscore.plot(
    kind= "barh"
)
plt.title("higest wicket taker")
plt.ylabel("players name")
plt.xlabel("wickets taken")
plt.show()

#most matches played by venue
venue = df["venue"].value_counts().head(5).sort_values(ascending=False)
sns.barplot(
    y=venue.index,
    x=venue.values,
    palette="Paired",
)
plt.title("Match played in venue")
plt.xlabel("number of match played")
plt.ylabel("name of stadium")
plt.show()

#who won the highest margin my run
print(df[df["won_by"] == "Runs"].loc[df[df["won_by"] == "Runs"]["margin"].idxmax()])

#which team won the most matches
match = df["match_winner"].value_counts().sort_values(ascending=False)
top5 = match.head(5)

sns.barplot(
    y=top5.index,
    x=top5.values,
    palette="viridis",
)
plt.title("Teams who won most of the matches ")
plt.xlabel("number of match won")
plt.ylabel("Team names")
plt.show()