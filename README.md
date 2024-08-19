# Storage.Timeline TA-Lib processor

This project provides a flexible TaLibProcessor class for applying TA-Lib indicators to time series data.

## Installation

```
pip install git+https://github.com/pysyun/python_storage_timeline_talib.git@main
```

## Usage

The `TaLibProcessor` class allows you to apply various TA-Lib indicators to your time series data. It supports both single-value indicators (like SMA, EMA) and multi-value indicators (like Bollinger Bands, MACD, etc.).

### Basic Usage

```python
from storage_timeline_talib import TaLibProcessor

# Create a processor for a specific indicator
sma_processor = TaLibProcessor('SMA', period=20)

# Process your time series data
time_line_data = [{'time': 1672531200, 'value': 100}, {'time': 1672617600, 'value': 101}, ...]
result = sma_processor.process(time_line_data)
```

### Multi-value Indicator Example (Bollinger Bands)

```python
bb_processor = TaLibProcessor('BBANDS', period=20, nbdevup=2, nbdevdn=2, matype=0)
result = bb_processor.process(time_line_data)
```

### Multi-value Indicator Example (MACD)

```python
macd_processor = TaLibProcessor('MACD', period=26, fastperiod=12, slowperiod=26, signalperiod=9)
result = macd_processor.process(time_line_data)
```

## Output Format

The processor returns a list of dictionaries. Each dictionary contains:
- `time`: The original timestamp (Unix timestamp)
- `value`: The indicator value(s)

For single-value indicators:
```python
[{'time': 1672531200, 'value': 105.5}, ...]
```

For multi-value indicators (e.g., Bollinger Bands):
```python
[{'time': 1672531200, 'value': {'upper': 110.5, 'middle': 105.5, 'lower': 100.5}}, ...]
```

## Supported Indicators

This processor supports all indicators available in TA-Lib. Some common ones include:

### Single-value indicators:
- SMA (Simple Moving Average)
- EMA (Exponential Moving Average)
- RSI (Relative Strength Index)

### Multi-value indicators:
- BBANDS (Bollinger Bands)
- MACD (Moving Average Convergence Divergence)
- STOCH (Stochastic)
- STOCHF (Stochastic Fast)
- STOCHRSI (Stochastic Relative Strength Index)
- AROON (Aroon)
- MAMA (MESA Adaptive Moving Average)
- MINMAX (Lowest and Highest Values over a specified period)
- MINMAXINDEX (Index of Lowest and Highest Values over a specified period)
- HT_PHASOR (Hilbert Transform - Phasor Components)
- HT_SINE (Hilbert Transform - SineWave)

Refer to the [TA-Lib documentation](https://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html) for a full list of supported indicators and their parameters.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
