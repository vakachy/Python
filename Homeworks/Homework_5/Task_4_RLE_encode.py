
file_name = 'Task_4_info.txt'

with open(file_name, 'r') as content:
    s = content.read()

print(s)

count: int = 0
start: int = 0
end: int = 0
rle: str = ''

while (end < len(s)):
    if (s[start] == s[end]):
        if (end == len(s)-1): # если элемент крайний
            count += 1
            end += 1
            rle += str(count) + s[start]
        else: # если элемент не крайний
            end += 1
            count += 1
    else:
        if (end == len(s)-1): # если элемент крайний
            count += 1
            rle += str(count) + s[start]
        else: # если элемент не крайний
            rle += str(count) + s[start]
            start = end
            count = 0

with open('rle_encode.txt', 'w') as file:
    file.write(rle)
