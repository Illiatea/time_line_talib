import requests
import json
import talib
# TODO: This is explained by the IDE
import numpy as np


# TODO: After other re-factoring, the class name will be more logical to become something like "TALibProcessor".
# TODO: Other "processor" examples:
# TODO: - https://github.com/pysyun/pysyun-timeline/blob/master/pysyun/timeline/converters.py
# TODO: - https://github.com/pysyun/pysyun-timeline/blob/master/pysyun/timeline/filters.py
class TimelineSourceIndicator:

    # TODO: The constructor can create such object, which is logical:
    #  https://github.com/pysyun/pysyun-timeline/blob/master/pysyun/timeline/sources.py#L13
    def __init__(self, url):
        self.url = url

    # TODO: Loading factual data is already available in the following library:
    #  https://github.com/pysyun/pysyun-timeline/blob/master/pysyun/timeline/sources.py#L33
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

    # TODO: All PySyun processor are organized as classes, which store parameters in the constructor and then just
    #  accept the list of data in the method, called "process". This class should be the same,
    #  after you change the constructor.
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
                # TODO: This situation results in unpredicted consequences. Need to analyze, why this happens.
                # TODO: And then, such errors are fixed using logical checks.
                continue
        data = true_data
        indicator_args = np.array(indicator_args)
        indicator_result = indicator_func(indicator_args, timeperiod=period)
        result = [{'time': data[i]['time'], 'value': indicator_result[i]} for i in
                  range(len(data) - period + 1)]
        return result
