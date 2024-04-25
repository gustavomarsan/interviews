def is_one_edit(a: str, b: str) -> bool:
    if a == b:
        return True

    if abs(len(a) - len(b)) > 1:
        return False

    if len(a) == len(b):
        counter = 0
        for x in range(len(a)):
            if a[x] != b[x]:
                counter += 1
                if counter > 1:
                    return False
        return True


a = "Hola Mundo"
b = "Hole Mund"

print(is_one_edit(a, b))
