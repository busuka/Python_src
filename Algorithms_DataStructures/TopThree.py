input_list = [25, 36, 4, 55, 71, 18, 0, 71, 89, 65]

# Algorithm1 : Search for list in 3 times
test_list = input_list.copy()
output = ""
for i in range(3):
    maxval = max(test_list)
    output += str(maxval) + " "
    test_list.remove(maxval)
print(output)

# Algorithm2 : Sort and take 3 items from list
test_list = input_list.copy()
x = sorted(test_list, reverse=True)[0:3]
print(" ".join(map(str, x)))