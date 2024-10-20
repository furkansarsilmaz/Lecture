from tkinter import *
from tkinter import messagebox
class lecture():
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x250")
        self.root.configure(background="gray")

        self.label_frame = Frame(self.root,background="gray")
        self.label_frame.pack(anchor=N,pady=20)

        self.notes_label = Label(self.label_frame,
text="FF:44\nDD:49\nDC:59\nCC:69\nCB:79\nBB:84\nBA:89\nAA:100",width=7,height=9)
        self.notes_label.grid(row=2,column=0)

        self.name_label = Label(self.label_frame,text="Name : ")
        self.name_label.grid(row=0,column=0)
        
        self.point_label = Label(self.label_frame,text="Point : ")
        self.point_label.grid(row=1,column=0)

        self.name_text = Text(self.label_frame,width=12,height=1)
        self.name_text.grid(row=0,column=1)

        self.point_text = Text(self.label_frame,width=12,height=1)
        self.point_text.grid(row=1,column=1,pady=5)

        self.calculate_button = Button(self.label_frame,width=5,height=2,text="Enter",command=lambda:self.calculate())
        self.calculate_button.grid(row=2,column=1)
        
        self.notes = {"FF":44,"DD":49,"DC":59,"CC":69,"CB":79,"BB":84,"BA":89,"AA":100}
        
    def calculate(self):
        name = self.name_text.get("1.0",END).strip()
        point = int(self.point_text.get("1.0",END).strip())
        for key,values in self.notes.items():
            if values >= point:
                messagebox.showinfo("Succeed",f"{name}, Your letter grade is {key}")
                break
    



if __name__ == "__main__":
    root = Tk()
    lecture(root)
    root.mainloop()