

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1


def pascal_triangle(n):
    if n < 1:
        print("error")
        return []
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        
        k = 2
        current_line = [1, 1]
        while k < n:
            next_line = [1]  # start with leading
            for i in range(len(current_line)-1):
                value = current_line[i] + current_line[i+1]
                next_line.append(value)
            next_line.append(1)  # add final 1
            current_line = next_line
            k += 1
        
        return current_line


print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))
print(pascal_triangle(5))
print(pascal_triangle(6))
print(pascal_triangle(7))
print(pascal_triangle(8))

