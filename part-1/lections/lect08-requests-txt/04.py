import requests


filename = "https://pcoding.ru/csv/01.txt"
response = requests.get(filename)

if response.ok:
    print(response.text)
else:
    print("Нет файла")
    
# x = ord(" ")
# h = hex(x)
# print(hex(0x1F + 0x3))
