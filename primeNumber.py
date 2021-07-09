# Function - If a number it's only divisible by 1 and itself, is prime
def isPrime(number):
    if number == 1:
        print(f"The number {number} is not prime :(")
        return False
    else:
        for i in range(2,number):
            if number % i == 0:
                print(f"The number {number} is not prime :(")
                return False
    print(f"The number {number} is prime! :)")
    return True

# Function - The user write a number and the other function check it
def askForANumber():
    number = input("Type a number and check if it's prime or not!: ")
    number = int(number)
    isPrime(number)

exit = False
while exit == False:
    askForANumber()
    keepIn = input("Do you want to write more numbers? Type (y) or (n): ")
    if keepIn == 'y':
        exit = False
    else:
        exit = True
