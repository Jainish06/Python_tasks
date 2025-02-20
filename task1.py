#Armstrong no :

def is_armstrong(num):
    str_num = str(num)
    digit_count = len(str_num)
    digit_sum = sum(int(digit) ** digit_count for digit in str_num)
    if digit_sum == num:
        return True
    else: return False

ans = is_armstrong(153)
print(ans)


#Anagram

def check_anagram(string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    else : return False

ans = check_anagram("silent","listen")
print(ans)



