from os import system


system("clear")
b = "1100"  # 12

dec = 0
for i in range(len(b)):
    dec += int(b[i]) * 2**(len(b)-1-i)
print(dec)
