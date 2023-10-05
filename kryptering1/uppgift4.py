def function_s(n):
    int_list = [int(i) for i in str(n)]
    sum = 0
    i = 0
    while i < len(int_list):
        sum += (int_list[i])**2
        i = i+1
    return sum

def sheck_for_A(list):
    list_A = [1,4,16,20,37,42,58,89,145]
    if any(value in list for value in list_A):
        return True
    else:
        return False

def function_x0(x,k): #skapar antingen en vald längd av lista eller skapar en lista tills man får ett element från A
    if k == 0:
        Xk = [x]
        statement = False
        i = 0
        while statement == False:
            statement = sheck_for_A(Xk)
            sum = function_s(Xk[i])
            Xk.append(sum)
            i += 1
        return Xk[: -1]
    else:
        Xk = [x]*k
        i = 1
        while i < k:
            Xk[i]=function_s(Xk[i-1])
            i += 1
        return Xk

def find_xa():
    i=0
    x=1
    A1, A4, A16, A20, A37, A42, A58, A89, A145 = ([] for i in range(9))

    while x < 10001:
        a_value = function_x0(x,0)
        last_element = str(a_value.pop())
        if  last_element == "1":
            A1.append(x)
        elif last_element == "4":
            A4.append(x)
        elif last_element == "16":
            A16.append(x)
        elif last_element == "20":
            A20.append(x)
        elif last_element == "37":
            A37.append(x)
        elif last_element == "42":
            A42.append(x)
        elif last_element == "58":
            A58.append(x)
        elif last_element == "89":
            A89.append(x)
        elif last_element == "145":
            A145.append(x)
        x += 1
    A1len = len(A1)
    A4len = len(A4)
    A16len = len(A16)
    A20len = len(A20)
    A37len = len(A37)
    A42len = len(A42)
    A58len = len(A58)
    A89len = len(A89)
    A145len = len(A145)
    print("\nDet finns {} stycken 1or och listan ser ut:".format(A1len))
    print(A1)
    print("\nDet finns {} stycken 4or och listan ser ut:".format(A4len))
    print(A4)
    print("\nDet finns {} stycken 16 och listan ser ut:".format(A16len))
    print(A16)
    print("\nDet finns {} stycken 20 och listan ser ut:".format(A20len))
    print(A20)
    print("\nDet finns {} stycken 37 och listan ser ut:".format(A37len))
    print(A37)
    print("\nDet finns {} stycken 42 och listan ser ut:".format(A42len))
    print(A42)
    print("\nDet finns {} stycken 58 och listan ser ut:".format(A58len))
    print(A58)
    print("\nDet finns {} stycken 89 och listan ser ut:".format(A89len))
    print(A89)
    print("\nDet finns {} stycken 145 och listan ser ut:".format(A145len))
    print(A145)

find_xa()