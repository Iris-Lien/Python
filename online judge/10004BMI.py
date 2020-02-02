#people = input()
weight, height = input().split()
bmi = float(weight)/(float(height)*float(height))
if bmi<18.5:
    print('under')
elif 18.5<=bmi<25.0:
    print('normal')
elif 25.0<=bmi<30.0:
    print('over')
else:
    print('obese')
