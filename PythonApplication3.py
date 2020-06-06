
print("hello world")

data = open('test.txt')

for each_line in data:
    (name ,rest) = each_line.split(':')
    if name == 'sandeep ':
        print("got it")
        print(name)
print(rest)
