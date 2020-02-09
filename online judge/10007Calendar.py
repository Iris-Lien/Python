Y, M, D, W = input().split()
import time
import datetime
output = datetime.datetime(int(Y),int(M),int(D)).strftime('%A')
print(output)
