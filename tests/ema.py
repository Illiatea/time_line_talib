from storage_timeline_talib import TaLibProcessor
import json

with open('timeline.json', 'r') as json_file:
    time_line = json.load(json_file)

ema_data = TaLibProcessor("EMA", 20).process(time_line)
print(ema_data)
