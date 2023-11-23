band = 4
for exp in range(1, band+1):
    print(f'10**{exp} = {10**exp:{band+1}d}')

"""
10**1 =    10
10**2 =   100
10**3 =  1000
10**4 = 10000
"""