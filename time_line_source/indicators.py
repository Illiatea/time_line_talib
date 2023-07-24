import requests
import json
import talib
import numpy as np


class TimelineSourceIndicator:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        data_str = response.content.decode('utf-8')
        data_json = json.loads(data_str)
        parsed_data = []
        for item in data_json:
            time = item['time']
            value_str = item['value']
            value_json = json.loads(value_str)
            parsed_data.append({'time': time, 'value': value_json})
        return parsed_data

    def get_indicator(self, indicator_name, period):
        data = self.get_data()
        indicator_func = getattr(talib, indicator_name)
        indicator_args = []
        true_data = []
        for d in data:
            try:
                i = d['value']['r'][0]
                indicator_args.append(float(i))
                true_data.append(d)
            except Exception as ex:
                continue
        data = true_data
        indicator_args = np.array(indicator_args)
        indicator_result = indicator_func(indicator_args, timeperiod=period)
        result = [{'time': data[i]['time'], 'value': indicator_result[i]} for i in
                  range(len(data) - period + 1)]
        return result