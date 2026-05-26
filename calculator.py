from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title('Calculator')
        master.geometry('300x400')
        master.config(bg='gray')
        master.resizable(0, 0)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=20, fg='black', bg='#ccddff', font=('Arial', 24), textvariable = self.equation).place(x=0, y=0)
        
    ## use array and loop to create buttons to avoid repetition

        ## array with button text and position (column, row)
        button_info = [
            ('(', 0, 1), (')', 1, 1), ('DEL', 2, 1), ('/', 3, 1),
            ('7', 0, 2), ('8', 1, 2), ('9', 2, 2), ('*', 3, 2),
            ('4', 0, 3), ('5', 1, 3), ('6', 2, 3), ('-', 3, 3),
            ('1', 0, 4), ('2', 1, 4), ('3', 2, 4), ('+', 3, 4),
            ('C', 0, 5), ('0', 1, 5), ('.', 2, 5), ('=', 3, 5)
        ]

        ## create buttons using loop and lambda to pass text value to show function
        for (text, col, row) in button_info:
            if(text == 'C'):
                Button(width=4, height=3, text=text, relief='flat', 
                       command=self.clear).place(x=col*72.5, y=row*63.5)
            elif(text == '='):
                Button(width=4, height=3, text=text, relief='flat', 
                       command=self.solve).place(x=col*72.5, y=row*63.5)
            elif(text == 'DEL'):
                Button(width=4, height=3, text=text, relief='flat',             
                       command=self.delete).place(x=col*72.5, y=row*63.5)
            else:
                Button(width=4, height=3, text=text, relief='flat', 
                   command=lambda t=text: self.show(t)).place(x=col*72.5, y=row*63.5)
            

    ## function to update entry value and display it
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    ## function to delete last character from entry value and update display
    def delete(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    ## function to clear entry value and update display
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    ## function to evaluate the expression in entry value and display result
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

## create main window and run the application
root = Tk()
calculator = Calculator(root)
root.mainloop()
