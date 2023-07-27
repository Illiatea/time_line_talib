from time_line_source.indicators import TALibProcessor

# TODO: Now tests do not match the new code. You can just save a JSON file locally and use it to avoid calling the
#  database and linking to a database library.
url = "https://europe-west1-hype-dev.cloudfunctions.net/storage-timeline-all?format=string&schema=ethereum.lovelyswap" \
      "-v4.lovely.finance&timeLine=0x3aB9323992DFf9231D40E45C4AE009db1a35e40b"
my_data = TALibProcessor(url)

ema_data = my_data.get_indicator("EMA", 20)
print(ema_data)
