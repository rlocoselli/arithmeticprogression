import ap_member

def calculate_last_number_arithmetic_progression(root, firstnumber, count) -> int:
    return str(int(firstnumber) + (int(count)-1)*int(root))

def calculate_sum_number_arithmetic_progression(root, firstnumber, count) -> int:
    x = int(firstnumber)
    mySum = x
    i = 1
    while i < int(count):
        x = x + int(root)
        i = i + 1
        mySum = mySum + x
    
    return str(mySum)

def getApMembers(root, firstnumber, count):
    
    list = []

    x = int(firstnumber)
    i = 1
    
    ini = ap_member.ap_member()
    ini.value = x

    list.append (ini)

    while i < int(count):
        x = x + int(root)
        i = i + 1
        a = ap_member.ap_member()
        a.value = x

        list.append (a)
    

    return list