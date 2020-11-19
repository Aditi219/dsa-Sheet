def check(s):
    flag = 1
    for i in range(len(s)//2):
        if s[i] == s[len(s)-i-1]:
            pass
        else:
            flag = 0
            break
    if flag == 0:
        print("Not a Palindrome")
    else:
        print("A Palindrome")


s = list(input())
check(s)
