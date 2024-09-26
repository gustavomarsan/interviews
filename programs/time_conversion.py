"""""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

"12:01:00PM"

Return '12:01:00'.

"12:01:00AM"
Return '00:01:00'.
"""

def timeConversion(s):
    # Write your code here
    if (s[0:2]) == "12" and s[8] == "A" :
        r = "00"+s[2:8]
    elif (s[0:2]) == "12" and s[8] == "P":
        r = s[0:8]
    elif s[8] == "A" :
        r = s[0:8]
    else:
        r = str(int(s[0:2])+12)+s[2:8]
    return r


s = "04:05:39PM"
print(timeConversion(s))