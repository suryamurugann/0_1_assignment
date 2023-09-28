def sum_list():
    samole_list=[]
    size=int(input("Enter size :"))
    for i in range (size):
        list=int(input(f"enter {i+1} list :"))
        samole_list.append(list)
    print(samole_list)
    total=sum(samole_list)
    print("sum of the list :",samole_list,"=",total)


sum_list()