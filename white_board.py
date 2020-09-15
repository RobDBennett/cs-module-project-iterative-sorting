# 

array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def find_three(array):
    for item in array:
        if item % 3 == 0:
            print(item)


find_three(array)