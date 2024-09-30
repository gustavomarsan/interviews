""""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity.
If the amount spent by a client on a particular day is greater than or equal to  the client's median spending 
for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send 
the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of n days, determine the number 
of times the client will receive a notification over all n days.

Example
expenditure = [10, 20, 30, 40,50]       d = 3

result = 1

The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, 
the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two 
middle values.

(solved with fixed sliding windows)
"""

def list_media(a: list)-> int:
    a.sort()
    if len(a) % 2 == 1:
        a.pop(len(a)//2)
        return sum(a)/len(a)
        sum = 0
        for n in range(len(a)):
            sum += a[n]
        return sum/len(a)
    else:
        i = int(len(a)/2) - 1
        return (a[i] + a[i+1]) / 2
        
def activityNotifications(expenditure: list, d: int) -> int:
    # Write your code here
    p1 = 0
    c = 0
    for n in range(d, len(expenditure)):
        if expenditure[n] >= (list_media(expenditure[p1:p1+d])) * 2:
            c +=1
        p1 += 1
    return c

expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5,]
d = 5
print(activityNotifications(expenditure, d))
