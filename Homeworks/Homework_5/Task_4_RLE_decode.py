
file_name = 'rle_encode.txt'

with open(file_name, 'r') as content:
    s = content.read()

print(s)

# s='4a15b3k'
i: int = 0
count: int = 0
start: int = 0
# i: int = 0
sub: str = ''
result: str = ''

while (i < len(s)):
    if (s[i].isnumeric()):
        sub += s[i]
        i += 1
    else:
        result += (s[i]*int(sub))
        i += 1
        sub = ''

print(result)
with open('rle_decode.txt', 'w') as file:
    file.write(result)