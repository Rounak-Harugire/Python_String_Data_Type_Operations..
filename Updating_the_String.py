String_1 = "hello rounak"
list_1 = list(String_1)
list_1[1] = 'o'
String_2 = ''.join(list_1)
print("\nUpdating character at 2nd Index:- ")
print(String_2)
String_3 = String_1[0:2] + 'o' + String_1[3:]
print(String_3)
