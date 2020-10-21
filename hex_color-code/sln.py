import re

def get_hex_code(n:int)->[]:
    result = list()
    for i in range(n):
        result += re.findall(r".(#[a-fA-F\d]{6}|#[a-fA-F\d]{3})",input("CSS Code here: "))
    return result

if __name__ == "__main__":
    n = int(input("Number of Lines of code: "))
    print(*get_hex_code(n))
