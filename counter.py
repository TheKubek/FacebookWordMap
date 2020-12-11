import json
import os
from collections import Counter


def count_msgs():
    senders = []
    files = [file.name for file in os.scandir('messages')]
    for f in files:
        with open(f'messages/{f}') as file:
            data = json.load(file)
            for message in data['messages']:
                senders.append(message['sender_name'])
    return Counter(senders), len(senders)


if __name__ == '__main__':
    with open('result.txt', mode='w', encoding='UTF-8') as file:
        counter, length = count_msgs()
        for name in [c[0] for c in counter.most_common()]:
            file.write(f'{name}: {counter[name]}\n')
        file.write(str(length) + "\n")
