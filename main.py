# a = ["Asror", "Jasur", "Ulug'bek", "Asror"]
# i = 0
# while len(a)>i:
#     x = a.index("Asror", i)
#     i += 1
# print(x)

# def xo(s):
#     i = 0
#     y = 0
#     z = 0
#     while len(s)>i:
#         if s[i] == "x":
#             y += 1
#         if s[i] == "y":
#             z += 1
#         i += 1
#     if y == z:
#         return True
#     else:
#         return False
# print("xoxo")

s = ["apple", "apple", "granade", "pear"]
i = 0
x = s.count("apple")
si = [x]
while len(s)>i:
    if s[i] == "apple":
        si.append(i)
    i += 1
print(si)
