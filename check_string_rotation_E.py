def check(s1, s2):
    if len(s1) != len(s2):
        print("NO")
    if len(s1) == 0 and len(s2) == 0:
        print("YES")
    temp = s1+s1
    flag = 0
    for i in range(len(temp)):
        if s2 == temp[i:i+len(s2)]:
            flag = 1
            break
    if flag == 0:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    check("ABCD", "ZXCV")
