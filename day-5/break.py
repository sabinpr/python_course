import time

nonsence = 'kjflkgjkdfhgkjdfhg;kkfhg;lkldfhg'

for char in nonsence:
    if char == ';':
        break
    time.sleep(0.3)
    print(char)