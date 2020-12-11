import json
import os
from datetime import datetime

import matplotlib.pyplot as plt

import numpy as np


def freq_graph():
    timestamps = []
    files = []
    for f in os.scandir('messages'):
        name = f.name
        if len(name) == 14:
            old_name = name
            name = name[:8] + '0' + name[8:]
            os.rename(f'messages/{old_name}', f'messages/{name}')
        files.append(name)
    files.sort()
    for f in files:
        with open(f'messages/{f}') as file:
            data = json.load(file)
            for message in data['messages']:
                timestamps.append(message['timestamp_ms'])
    print(files)
    days = round((timestamps[0] - timestamps[-1]) / 1000 / 3600 / 24)
    print(datetime.fromtimestamp(timestamps[0]/1000))
    print(datetime.fromtimestamp(timestamps[-1]/1000))
    print(timestamps[0])
    print(timestamps[-1])
    print(days)
    points, length = np.linspace(min(timestamps), max(timestamps), days, retstep=True, dtype=np.int64)
    y = []
    for point in points:
        nxt = point + length
        y.append(len([x for x in timestamps if point <= x < nxt]))
    plt.plot([datetime.fromtimestamp(ms/1000.0) for ms in points], y)
    plt.show()


if __name__ == '__main__':
    freq_graph()
