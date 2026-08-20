def first_palindrome(words):
    for w in words:
        if w == w[::-1]:
            return w
    return ""

if __name__ == "__main__":
    print(first_palindrome(["abc","car","ada","racecar","cool"]))  # ada
    print(first_palindrome(["notapalindrome","racecar"]))          # racecar
