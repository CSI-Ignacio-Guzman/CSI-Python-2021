import requests
res = requests.get(https://www.gutenberg.org/ebooks/67637)
res.raise_for_status()
playfile = open(The History of the Manners and Customs of Ancient Greece Volume II (of 3))
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()