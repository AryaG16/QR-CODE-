# pip install pyqrcode
import pyqrcode

str=input("Text/URL to encrypt: ")
name=input("Name: ")
b=pyqrcode.create(str)
b.svg("D:\\PYTHON exps\\QR CODE\\"+name+".svg", scale=8)
b.png("D:\\PYTHON exps\\QR CODE\\"+name+".png", scale=6)