t = input("Input time(eg. 07:10 pm): ")

hr = int(t[0:2])

m = int(t[3:5])

apm = t[6:8]


if 0<=m<60 and 0<=hr<12:

    if apm =="am":
        if hr<10:
            ph='0' + str(hr)
        else:
            ph=str(hr)
        p = str(ph) + ':' + str(m)

    elif apm=="pm":
        ph=str(hr+12)
        p = str(ph) + ':' + str(m)


elif hr==12:
    
    if apm =="am":
        ph=str('00')
        p = str(ph) + ':' + str(m)

    elif apm=="pm":
        ph=str(hr)
        p = str(ph) + ':' + str(m)


print(p)
    
