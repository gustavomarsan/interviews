def is_palindrome(a: str) -> bool:
    for x in range(0, len(a) // 2):
        if a[x] != a[-(x + 1)]:
            return False
    return True


a = "anitalavalatina"
print(a)
print(is_palindrome(a))
