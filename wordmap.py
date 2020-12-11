import os
import re
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json

from polish_words_common import common_words

files = [file.name for file in os.scandir('messages')]
messages = ""
for f in files:
    with open(f'messages/{f}') as file:
        data = json.load(file)
        for msg in data["messages"]:
            try:
                messages += (msg["content"]) + " "
            except:
                continue


messages = messages.lower()

for word in ["missed", "ale", "nie", "video", "chat", "left", "youtube", "https", "http",
             "poll", "voted", "created", "the", "a", "an"] + common_words(1000):
    messages = re.sub(r"\b{}\b".format(word), "", messages)

wordcloud = WordCloud().generate(messages)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

