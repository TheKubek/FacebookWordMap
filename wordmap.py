import re
import sys
import matplotlib.pyplot as plt
import codecs
from wordcloud import WordCloud
import json


filename = sys.argv[1]

with codecs.open(filename, "r", "utf-8") as file:
    data = json.load(file)
    

messages = ""

for msg in data["messages"]:
    try:
        messages += (msg["content"]) + " "
    except:
        continue


messages = messages.lower()

for word in ["missed", "video", "chat", "left", "youtube", "https", "http",
             "poll" ,"voted", "created", "the", "a", "an"]:
    messages = re.sub(r"\b{}\b".format(word), "", messages)

wordcloud = WordCloud().generate(messages)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

