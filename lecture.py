notes = {
"FF":44,
"DD":49,
"DC":59,
"CC":69,
"CB":79,
"BB":84,
"BA":89,
"AA":100,
}
loop = True
while loop:
    try:
        point = int(input("Enter your exam point : "))
        for key, value in notes.items():
            if value >= point:
                print(f"Your note is {key}")
                break
        again = input("Y for retry, N for quit : ").lower()
        if again == "n" :
            loop = False
            print("Goodbye")
            break

    except ValueError:
        print("Please give a number")