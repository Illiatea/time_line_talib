import talib
import numpy

class TALibProcessor:

    def __init__(self, time_line):
        self.time_line = time_line

    def get_indicator(self, indicator_name, period):
        indicator_func = getattr(talib, indicator_name)
        indicator_args = []
        data = self.time_line
        for d in data:
            i = d['value']
            print(i)
            indicator_args.append(float(i))

        indicator_args = numpy.array(indicator_args)
        indicator_result = indicator_func(indicator_args, timeperiod=period)
        result = [{'time': data[i]['time'], 'value': indicator_result[i]} for i in
                  range(len(data) - period + 1)]
        return result
