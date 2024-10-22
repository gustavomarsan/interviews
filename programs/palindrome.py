def is_palindrome(a: str) -> bool:
    for x in range(len(a) // 2):
        if a[x] != a[~x]:
            return False
    return True


a = "anitalavalatina"
print(a)
print(is_palindrome(a))
