from indicators import TaLibProcessor
import json

with open('timeline.json', 'r') as json_file:
    time_line = json.load(json_file)

rsi_data = TaLibProcessor("RSI", 14).process(time_line)
print(rsi_data)
