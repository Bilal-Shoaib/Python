#basic commands
#console.writeline()/console.write() = print()
#use "\n" after comma to enter new line, eg; print("My Name is " + name, "\n" "My Age is " + age)
#abc = [optional]->int(input("message: ") for faster prompt-input)
#after every conditional/iterative statement use ':'
#for strmanipulation use stringname[ starting index : ending index : step over ]
#use stringname[index:index + 1:] to extract one at a time
#always use [] for array index
#use .upper()/.lower() to convert to either case

#list of dictionaries
def printdict() :
    House = [
        {"name":"ali", "occupation":"student", "age" : 20,},
        {"name":"hassan", "occupation":"businessman", "age" : 35,},
        {"name":"bilal", "occupation":"student", "age" : 19,},
        {"name":"azhar", "occupation":"teacher", "age" : 47,}
    ]
    for members in House :
        print(members["name"], end = ", ")
    print()
    for members in House :
        print(members["occupation"], end = ", ")
    print()
    for members in House :
        print(members["age"], end = ", ")

#printdict()

#calculator
def calc() :
    try :
        x = int(input("whats val of x? "))
        y = int(input("whats val of y? "))

        op = input("Addition (+)\nSubtraction (-)\nMultiplication (*)\nDivision (/)\nRemainder (%)\nChoose operator: ")
    except ValueError:
        print("Value is not Integer")
    
    match op :
        case "+" :
            print(x + y)
        case "-" :
            print(x - y)
        case "*" :
            print(x * y)
        case "/" :
            print(int(x / y))
        case _ :
            print(x % y)
    
#calc()

#triangle printer
def trgprint() :
    fill = "/\\"
    empty = " "

    while True:
        n = input('Number of Rows: ')
        if not n.isdigit() or int(n) < 2:
            print('Unsupported Input, Retry')
            continue
        else:
            n = int(n)
            break

    for block in range(n) : print(empty * (n - block), fill * (block + 1), sep = "")

#trgprint()

#extract & manipulate strings
def strmanipulation() :
    #email = "bilal:202236@gmail.com"
    index = 0
    count = 0
    chr = ''
    firstname = ""
    rollnum = ""

    email = input("Enter the E-mail Address: ")
    while chr != ":" :
        chr = email[index:index + 1:]
        index += 1
    while chr != "@" :
        chr = email[count:count + 1:]
        count += 1
    
    firstname = email[0:index - 1].capitalize()
    rollnum = email[index:count - 1]

    print("First Name is: " + firstname ,"\n" "Roll Number is: " + rollnum)

#strmanipulation()

#Move up and Clear line
def upnclear(num):
    up, clear ='\033[1A', '\x1b[2K'
    for _ in range(num):print(up, end = clear)
#upnclear()