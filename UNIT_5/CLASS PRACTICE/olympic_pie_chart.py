# Create a pie chart of Olympic medal achievements
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("olympics.csv")
plt.pie(df["Medals"], labels=df["Country"], autopct="%1.1f%%")
plt.title("Olympic Medal Achievements (2016)")
plt.show()
