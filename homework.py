def palindrome(a):
    a = a.replace(' ', '').lower()
    ra = ''.join(reversed(a))
    if a == ra:
        return True
    else:
        return False
input_a = input()
print(palindrome(input_a))