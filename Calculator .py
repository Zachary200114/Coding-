def subtract(x, y):
    return x - y

def add(x, y):
    return x + y

def multiply (x,y):
    return x * y

def divide (x,y):
    if y == 0:
        return 'ERROR'
    return x / y

def Calculator():
    print('PICK WHAT OPERATION YOU WANT TO DO: ')
    print('1. Subtract')
    print('2. Add')
    print('3. Multiply')
    print('4. Division')
    print('5. Quit Calculator ')

    while True:
        answer = input('Enter your choice: (1/2/3/4/5): ')
        if answer in ('1','2','3','4'):
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number:'))

            if answer == '1':
                print(num1, '-' , num2, '=', subtract(num1,num2))
            elif answer == '2':
                print(num1, '+', num2, '=', add(num1,num2))
            elif answer =='3':
                print(num1, '*', num2, '=', multiply(num1,num2))
            elif answer =='4':
                print(num1, '/', num2, '=', divide(num1,num2))
            elif answer =='5':
                print('Exiting Calculator')
        break
    else:
        print('ERROR')

if __name__ == '__main__':
    Calculator()
    input('Press Enter To Exit ')


