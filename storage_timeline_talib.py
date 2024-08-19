import talib
import numpy as np


class TaLibProcessor:
    def __init__(self, indicator_name, period, **kwargs):
        self.indicator_name = indicator_name
        self.period = period
        self.kwargs = kwargs

    def process(self, time_line):
        indicator_func = getattr(talib, self.indicator_name)
        indicator_args = np.array([float(d['value']) for d in time_line])

        if self.indicator_name in ['BBANDS', 'MACD', 'STOCH', 'STOCHF', 'STOCHRSI', 'AROON', 'MAMA', 'MINMAX',
                                   'MINMAXINDEX', 'HT_PHASOR', 'HT_SINE']:
            indicator_results = indicator_func(indicator_args, timeperiod=self.period, **self.kwargs)
            result_keys = self.get_result_keys(self.indicator_name)

            result = [{'time': time_line[i]['time'],
                       'value': {key: indicator_results[j][i] for j, key in enumerate(result_keys)}}
                      for i in range(len(time_line))]
        else:
            indicator_result = indicator_func(indicator_args, timeperiod=self.period)
            result = [{'time': time_line[i]['time'], 'value': indicator_result[i]}
                      for i in range(len(time_line))]

        return result

    @staticmethod
    def get_result_keys(indicator_name):
        result_keys = {
            'BBANDS': ['upper', 'middle', 'lower'],
            'MACD': ['macd', 'macdsignal', 'macdhist'],
            'STOCH': ['slowk', 'slowd'],
            'STOCHF': ['fastk', 'fastd'],
            'STOCHRSI': ['fastk', 'fastd'],
            'AROON': ['aroondown', 'aroonup'],
            'MAMA': ['mama', 'fama'],
            'MINMAX': ['min', 'max'],
            'MINMAXINDEX': ['minidx', 'maxidx'],
            'HT_PHASOR': ['inphase', 'quadrature'],
            'HT_SINE': ['sine', 'leadsine']
        }
        return result_keys.get(indicator_name, [])
