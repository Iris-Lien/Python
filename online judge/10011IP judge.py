while True:
    try:
        IP = input()
        A, B, C, D = IP.split('.')
        if  A.isdigit() and B.isdigit() and C.isdigit() and D.isdigit():
            if 0<=int(A)<=255 and 0<=int(B)<=255 and 0<=int(C)<=255 and 0<=int(D)<=255:
                print('Y')
            else:
                print('N')
        else:
            print('N')
    except:
        break
