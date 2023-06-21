from langdetect import detect

while True:
  text = input("input message:")
  print(detect(text))
