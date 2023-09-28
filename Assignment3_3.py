
def count_strings(str):
    up_count = 0
    low_count = 0

    for char in str:
        if char.isupper():
            up_count += 1
        elif char.islower():
            low_count += 1

    return f"Input = {string}\nNo. of Upper case characters : {up_count}\nNo. of Lower case Characters : {low_count}"

string = input("Enter Your String :")
res= count_strings(string)
print(res)