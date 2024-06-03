
def format_name(f_name, l_name):
    list1 = list(f_name)
    front_name = [x.lower() for x in list1]
    front_name[0] = front_name[0].upper()
    final_front = "".join(front_name)


    list2 = list(l_name)
    last_name = [x.lower() for x in list2]
    last_name[0] = last_name[0].upper()
    final_last = "".join(last_name)
    final = final_front + " " + final_last
    return final

print(format_name("aLFi", "wiRDiYan"))
