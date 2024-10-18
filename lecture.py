class lecture():
    def __init__(self,point):
        self.point = point
        self.notes = {
"FF":44,
"DD":49,
"DC":59,
"CC":69,
"CB":79,
"BB":84,
"BA":89,
"AA":100,
}
    def calculate(self):
        for key,values in self.notes.items():
            if values >= self.point:
                print(f"Your note is {key}")
                break




if __name__ == "__main__":
    point = int(input("What is your note : "))
    lecture(point).calculate()