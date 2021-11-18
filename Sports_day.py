dic = {"A":"cricket", "B":"badminton", "C":"football"}
a = []
b = []
c = []

for grp, rl in dic.items():
    if (dic[grp] == "cricket"):
        num = int(input(f"Enter the no of students in {dic[grp]}: "))
        for i in range(num):
            roll = int(input("Enter the student Roll no: "))
            a.append(roll)
    
    elif dic[grp] == "badminton":
        num = int(input(f"Enter the no of students in {dic[grp]}: "))
        for i in range(num):
            roll = int(input("Enter the student Roll no: "))
            b.append(roll)

    elif dic[grp] == "football":
        num = int(input(f"Enter the no of students in {dic[grp]}: "))
        for i in range(num):
            roll = int(input("Enter the student Roll no: "))
            c.append(roll)

print(f"\nStudents of cricket:{a}\nStudents of badminton:{b}\nStudents of football:{c}")

def union(a, b):
    res = list(a)
    for i in b:
        if i not in a:
            res.append(i)
    return res

def inter(a,c):
    tem = []
    for i in a:
        if i in c:
            tem.append(i)
    return tem

def neither_nor(x):
    temp = []
    inte = union(a,c)
    for j in x:
        if j not in inte:
            temp.append(j)
    return temp
    
def either(x,y):
    res = []
    un = union(x,y)
    j = inter(x,y)
    for i in un:
        if i not in j:
            res.append(i)
    return res

print("\n")
if __name__ == '__main__':
    print("Students who participated in cricket and badminton:",union(a,b))
    print("\nStudents who participated either cricket or badminton but not both:",either(a,b))
    print("\nStudents who participated in neither cricket nor football:",neither_nor(b))
    print("\nStudents who participated in cricket and football but not both", either(a,c))