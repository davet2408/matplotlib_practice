import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# read csv into a dataframe
data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

# use counter to collect all responses to a language
language_count = Counter()
for response in lang_responses:
    language_count.update(response.split(";"))

languages = []
popularity = []

# take the 15 most used languages and count the popularity of each
for item in language_count.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# reverse the lists so that the most popular is at the top
languages.reverse()
popularity.reverse()

# barh for horizontal bar plot
plt.barh(languages, popularity)

plt.title("Most popular languages")
plt.xlabel("Number of people who use")

plt.tight_layout()

plt.show()
