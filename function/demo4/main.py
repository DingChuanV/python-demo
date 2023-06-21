import pyqrcode

s = "dd"

url = pyqrcode.create(s)

url.svg("dd.svg", scale=8)
