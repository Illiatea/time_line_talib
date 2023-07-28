from storage_timeline_talib import TaLibProcessor
import json

with open('timeline.json', 'r') as json_file:
    time_line = json.load(json_file)

sma_data = TaLibProcessor("SMA", 7).process(time_line)
print(sma_data)
