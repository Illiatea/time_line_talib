import talib
import numpy as np


class TaLibProcessor:

    def __init__(self, indicator_name, period):
        self.indicator_name = indicator_name
        self.period = period

    def process(self, time_line):
        indicator_func = getattr(talib, self.indicator_name)
        indicator_args = []
        data = time_line
        for d in data:
            i = d['value']
            print(i)
            indicator_args.append(float(i))

        indicator_args = np.array(indicator_args)
        indicator_result = indicator_func(indicator_args, timeperiod=self.period)
        result = [{'time': data[i]['time'], 'value': indicator_result[i]} for i in
                  range(len(data) - self.period + 1)]
        return result
