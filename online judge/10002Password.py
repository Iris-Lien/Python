a, b, c = input().split()
sum_a = (int(a)//100)+(int(a)%100)//10+(int(a)%10)
sum_b = (int(b)//100)+(int(b)%100)//10+(int(b)%10)
sum_c = (int(c)//100)+(int(c)%100)//10+(int(c)%10)
sum_all = 10*(sum_a+sum_b)+sum_c
sum_allrev = str(sum_all)[::-1]
sum_allrev = "%03d" % int(sum_allrev)
print(sum_allrev)
