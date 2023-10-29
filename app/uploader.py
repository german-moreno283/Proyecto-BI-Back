from filestack import Client
client = Client("ASOcJeKFZS1m5rYyTVyFFz")

from urllib.request import urlopen
def file_uploader():
  file_link=client.upload(filepath="../data/Predicted.csv")
  print("File uploaded with link: ",file_link.url)
  return file_link.url