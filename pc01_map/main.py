text = ""
with open('./text', 'r') as file:
    text = file.read()

ORD_A = 97                  # lowercase
ORD_Z = 122                 # lowercase
cycle = ORD_Z - ORD_A + 1   # 26

char_range = range(ORD_A, ORD_Z + 1)

# dict + edge cases
trans_dict = {k:k + 2 for k in char_range}
trans_dict[ord('y')] = ord('a')
trans_dict[ord('z')] = ord('b')

table = str.maketrans(trans_dict)
print(text.translate(table))
print()
print('pc01_map'.translate(table))
