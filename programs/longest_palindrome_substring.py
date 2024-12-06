"""""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.
longest_substring_palindrome("banana") -> "???anana???"

trick = [0, 1, 2, 3, 4, 5, 6] --> [|, 1, |, 3, |, 5, |, 7, |, 9, |, 11, |, 13, , |]   (to fin even substrings)

Solucction: Using a sliding window, ponter in for loop walkin 1 by 1 and checking left and right sides, again, while neighbor 
are equals

"""

def long_palin_subs(a: str)-> str:
    a2 = ["|"]
    for item in a :
        a2.append(item)
        a2.append("|")
    print(a)
    print(a2)

    beg = 0
    fin = 1
    for p in range(1, len(a2) -1) :
        i = 1
        while p - i >= 0 and p + i < len(a2) and a2[p-i] == a2[p+i] :
            #print("p=", p, p-1, p+i, a2[p-i], a2[p+i], "entro")
            if 2*i +1 > fin - beg :
                beg = p - i
                fin = p + i
               
            i += 1
        print(p, beg, fin)
    return a[beg//2 : (fin-1)//2+1]



a = "anitaa"
print(long_palin_subs(a))


