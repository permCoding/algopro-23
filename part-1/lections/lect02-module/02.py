from os import system


system("clear")  # for Win -> cls

b = "1100"

i = 0
while i < len(b):
    print(b[i])    
    i += 1

for i in range(len(b)):
    print(i, b[i])

# for smb in b:
#     print(smb)