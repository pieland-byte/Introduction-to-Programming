# This program will sort 3 numbers into ascending order

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num > second_num and first_num > third_num:
    temp_3 = first_num
elif first_num < second_num and first_num < third_num:
    temp_1 = first_num
else:
    temp_2 = first_num

if second_num > first_num and second_num > third_num:
    temp_3 = second_num
elif second_num < first_num and second_num < third_num:
    temp_1 = second_num
else:
    temp_2 = second_num

if third_num > second_num and third_num > first_num:
    temp_3 = third_num
elif third_num < second_num and third_num < first_num:
    temp_1 = third_num
else:
    temp_2 = third_num

print(temp_1, temp_2, temp_3)
