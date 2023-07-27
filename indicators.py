import talib

class TaLibProcessor:

    def __init__(self, indicator_name, period):
        self.indicator_name = indicator_name
        self.period = period

    def process(self, time_line):
        indicator_func = getattr(talib, self.indicator_name)
        indicator_args = [float(d['value']) for d in time_line]
        indicator_result = indicator_func(indicator_args, timeperiod=self.period)
        result = [{'time': time_line[i]['time'], 'value': indicator_result[i]} for i in
                  range(len(time_line) - self.period + 1)]
        return result
