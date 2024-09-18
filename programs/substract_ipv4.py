# given a initial ipv4 and a final ipv4 check the diference betwen final  - initil

import sys
import datetime
def substract_ipv4(initial,final) -> int:

    # put the string to a list
    a = initial.split(".")
    b = final.split(".")

    # corvert
    for n in range(len(a)):
        a[n] = int(a[n])
        b[n] = int(b[n])

    result = 0
    tota = 0
    totb = 0
    for i in range(len(a)-1):
        tota = tota+a[i]*256
        totb = totb+b[i]*256
    tota = tota+a[3]
    totb = totb+b[3]
    result = totb - tota

    return result

initial = "20.0.0.10"
final= "20.0.1.0"

print(substract_ipv4(initial, final))

print(5 // 2)

a = 7
print (a.__str__())
print("hello"'world'*2)

print(sys.path)

print(type(datetime.date(2012,1,1)- datetime.date(2011,1,1)))