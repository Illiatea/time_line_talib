from storage_timeline_talib import TaLibProcessor
import json

with open('timeline.json', 'r') as json_file:
    time_line = json.load(json_file)

rsi_data = TaLibProcessor("RSI", 7).process(time_line)
print(rsi_data)
