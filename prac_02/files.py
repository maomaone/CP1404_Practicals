out_file = open('name.txt', 'w')
name = str(input("Enter your name \n"))
print("My name is", name, file=out_file)
out_file.close()


file = open("name.txt", "r")
file.read
print(file.read())

file = open("numbers.txt", "r")
number1 = int(file.readline())
number2 = int(file.readline())
print(number1 + number2)
file.close()

file = open("numbers.txt", "r")
total = 0
for line in file:
 number = int(line)
 total += number
print(total)
file.close()