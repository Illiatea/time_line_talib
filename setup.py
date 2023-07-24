from setuptools import setup

setup(
    name='time_line_talib',
    version='1.0',
    author='Illiatea',
    author_email='illiatea2@gmail.com',
    py_modules=['time_line_talib.time_line_source.indicators'],
    install_requires=['requests', 'TA-Lib']
)