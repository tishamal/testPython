import pandas as pd

a_dict = {'1st': 1, '2nd': "sAMAN", '3rd': 5, '4th':7, '5th': 9}
ser = pd.Series(a_dict)

#print('Range access:')
#print(ser)
#print(a_dict)
print('Access: Index number -',ser[1])

print('Access: Index label -',ser['2nd'])