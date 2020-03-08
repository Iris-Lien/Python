card1="1001"
pwd1="123456"
ban1=10000

card2="1002"
pwd2="123456"
ban2=10000

card3="1003"
pwd3="123456"
ban3=10000

error=0

while True:
    card=input("請輸入卡號：")
    pwd=input("請輸入密碼：")
    ban=0
    
    if card==card1 and pwd==pwd1:
        ban=ban1
    elif card==card2 and pwd==pwd2:
        ban=ban2
    elif card==card3 and pwd==pwd3:
        ban=ban3
    else:
        error+=1
        if error>=3:
            print("您已三次輸入錯誤")
            break
        else:
            print("輸入錯誤,請重新輸入")
            continue

    while True:
        num=input("請輸入辦理項目: 1.存款 2.取款 3.結束")
        if num=="1":
            inn=float(input("請輸入存款金額"))
            if inn<=0:
                print("存款請大於0")
            else:
                ban+=inn
                print("存款成功 存入:",inn,"餘額:",ban)
                
        elif num=="2":
            out=float(input("請輸入提款金額"))
            
            if out>ban:
                print("餘額不足提款失敗")
                continue
            else:
                ban-=out
                print("存款成功 提出:",out,"餘額:",ban)
                
        elif num=="3":
                print("請取卡 歡迎再度光臨")
                break
        else:
            print("輸入錯誤,請重新輸入")
            continue
