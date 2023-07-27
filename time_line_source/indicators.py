# TODO: This class is the only class in the project. Therefore, it can be in the root of the project to avoid the
#  "time_line_source" folder to become part of the namespace.
import talib
import numpy

# TODO: There is a style error here
class TALibProcessor:

    # TODO: The timeline should be passed to the "process" method as the only argument.
    def __init__(self, time_line):
        self.time_line = time_line

    # TODO: In the Pysyun time-line all such methods are called "process", because they may be called automatically
    #  in the pipeline.
    # TODO: Such arguments as "indicator_name" and "period" define rules for this processor and should be specified,
    #  while creating the processor. That is - they should be specified in the constructor.
    def get_indicator(self, indicator_name, period):
        indicator_func = getattr(talib, indicator_name)
        indicator_args = []
        data = self.time_line
        for d in data:
            i = d['value']
            # TODO: This slows down the overall code, while processing big amount of data + makes logs unreadable due
            #  to the big amount of logs.
            print(i)
            indicator_args.append(float(i))

        # TODO: Numpy is used only to produce this array. If you can produce this in another way - you do not need
        #  to reference the Numpy library, which is quite a big one.
        indicator_args = numpy.array(indicator_args)
        indicator_result = indicator_func(indicator_args, timeperiod=period)
        result = [{'time': data[i]['time'], 'value': indicator_result[i]} for i in
                  range(len(data) - period + 1)]
        return result
