from indicators import TaLibProcessor
import json

with open('timeline.json', 'r') as json_file:
    time_line = json.load(json_file)

sma_data = TaLibProcessor("SMA", 10).process(time_line)
print(sma_data)
