# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers: [3, 6, 9, 12, 15, 18, 21]

def triple(x):
    return x *3

size = int (input("Enter size :"))
lst=[]
for i in range (size):
    lst_input=int(input(f"Enter your Value {i+1} :"))
    lst.append(lst_input)
print("Sample list :",lst)

res=list(map(triple,lst))
print("Tripled of list numbers :",res)

