# Display a bar chart of programming language popularity
import matplotlib.pyplot as plt
languages = ["Python", "Java", "C++", "JavaScript"]
popularity = [90, 70, 50, 80]
plt.bar(languages, popularity)
for i in range(len(languages)):
    plt.text(i, popularity[i], str(popularity[i]), ha='center')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Programming Language Popularity")
plt.show()
