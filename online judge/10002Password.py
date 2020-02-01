a, b, c = input().split()
sum_a = (int(a)//100)+(int(a)%100)//10+(int(a)%10)
sum_b = (int(b)//100)+(int(b)%100)//10+(int(b)%10)
sum_c = (int(c)//100)+(int(c)%100)//10+(int(c)%10)
sum_all = 10*(sum_a+sum_b)+sum_c

if 100<=sum_all<=999:#三位數
    sum_allrev=(int(sum_all)%10)*100+((int(sum_all)%100)//10*10)+int(sum_all)//100
    print(sum_allrev)
elif sum_all>999: #超過三位數
    sum_all = "%03d" % sum_all
    sum_allrev=(int(sum_all)%10)*100+((int(sum_all)%100)//10*10)+int(sum_all)//100
    sum_allrev = "%03d" % sum_allrev
    print(sum_allrev)
else:#不足三位數
    if 10<=sum_all<=99:
        sum_all = sum_all*10
    if sum_all<10:
        sum_all = sum_all*100
    sum_all = "%03d" % sum_all
    sum_allrev=(int(sum_all)%10)*100+((int(sum_all)%100)//10*10)+int(sum_all)//100
    sum_allrev = "%03d" % sum_allrev
    print(sum_allrev)
