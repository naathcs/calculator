# Python Calculator
A simple calculator created in Python to practice library imports and array usage.

## Table of Contents
  - [Overview](#overview)
  - [Views](#views)
  - [About](#about)
  - [Process Breakdown](#process-breakdown)
  - [Tutorial Source](#tutorial-source)
    - [Links](#links)
  - [Author](#author)

## Overview

The goal of this is to exercise my current Python knowledge and apply different techniques that can be used in an develper environment and in a data analyst environment as well.

## Views
<div align="center">
  <img width="305" height="433" alt="calculator-usage" src="https://github.com/user-attachments/assets/e997ebd6-7c10-4368-a87b-35d383170ee9" />
</div>

## About

This calculator was created using an Youtube tutorial video as reference with code changes to practice topics learned on a Google Data Analytics Certificate.

<b>Library:</b> `Tkinter` <br>
<b>Code Adaptation:</b> `Array`, `For Loop`, `Lambda`, extra functions.

## Process Breakdown

The exercises was followed until the end to understand the basics of the simple Python project and its steps. 
After the completion of the project as it is, it was decided to change how a couple of items are approached to a more clean view of the code. <br>
The first step was to replace all the single numeric lines for an array that would display all the 'buttons' and its location in the array. 
After, a `For loop` is used to identify each item in the array and give an action (from a function), if necessary. 
For the functions, the on that was added from the main exercise was the `delete()` function that is used as an action in the 'DEL' button in the calculator.
<br>
```
def delete(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)
```
<br>
For the library import, the attributes `Tk, Entry, Button, StringVar` were used to create the window for the calculator, display the results, create the button and called the functions to it, and to hold and display the values as they were updated, in their respective orders. The Lambda function was used to pass the text from the array to be shown in the button.
<br>
To add the buttons in the correct location, I attempted to use a pre-algebra "trick" to calculatea the correct location of each item in the array inside the screen.

## Tutorial Source

[![Watch the video](https://i.ytimg.com/vi/6CZB6VTy3Hg/hqdefault.jpg?sqp=-oaymwEnCPYBEIoBSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLDfn9vsWCjHHRYxN9CEdzo9EW-O4w)](https://youtu.be/6CZB6VTy3Hg?si=fNL9mxVuoap-CKxb)

### Links
These are the links that were used as reference and guide to adapt the original code to its current source.

- [X and Y Calculation](https://www.reddit.com/r/learnmath/comments/eoo07x/i_discovered_a_cool_mental_math_trick_is_this/) - A pre-algebra explanation of the calculation that was attempted to be used in the X and Y axis of the array.
- [Lambda Simply Explained](https://www.reddit.com/r/learnpython/comments/1g0ktqk/can_someone_explain_lambda_to_a_beginner/) - A simple explanation of the lambda function that was used and the simple approach of it.

## Author

- Website - [Github](https://github.com/naathcs)
