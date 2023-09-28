# Sample List: [4, 5, 2, 9]
# Square the elements of the list:[16, 25, 4, 81]

def square(lst):
    return lst ** 2

size = int (input("Enter size :"))
lst=[]
for i in range (size):
    lst_input=int(input(f"Enter your Value {i+1} :"))
    lst.append(lst_input)
print("Sample List :",lst)

res = list(map(square,lst))
print("Squared List",res)