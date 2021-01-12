## Identify the data type of the following values:

```
99.9
# float

"False"
# str

False
# bool

'0'
# str

0
# int

True
# bool

'True'
# str

[{}]
# NoneType

{'a': []}
# dict
```
## What data type would best represent:
- A term or phrase typed into a search box?
    - str
- If a user is logged in?
    - bool
- A discount amount to apply to a user's shopping cart?
    - float
- Whether or not a coupon code is valid?   
    - bool
- An email address typed into a registration form?
    - str
- The price of a product?
    - float
- A Matrix?
    - dict
- The email addresses collected from a registration form?
    - str
- Information about applicants to Codeup's data science program?
    - str

## For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.
```
'1' + 2
- Prediction: Error
- Actual: Error

6 % 4
- Prediction: 1 
- Actual: 2 (remainder not quotient)

type(6 % 4)
- Prediction: int
- Actual: int

type(type(6 % 4))
- Prediction: NoneType
- Actual: type (just remember this)

'3 + 4 is ' + 3 + 4
- Prediction: 3 + 4 is 7
- Actual: error

0 < 0
- Prediction: False
- Actual: False

'False' == False
- Prediction: False
- Actual:

True == 'True'
- Prediction: False
- Actual:

5 >= -5
- Prediction: True
- Actual:

!False or False
- Prediction: Error
- Actual: Nothing

True or "42"
- Prediction: Nothing
- Actual: True

!True && !False
- Prediction: True
- Actual: /bin/bash: !False: command not found

6 % 5
- Prediction: 1 
- Actual: 

5 < 4 and 1 == 1
- Prediction: False
- Actual: False

'codeup' == 'codeup' and 'codeup' == 'Codeup'
- Prediction: False
- Actual: False 

4 >= 0 and 1 !== '1'
- Prediction: Error
- Actual: Error

6 % 3 == 0
- Prediction: True
- Actual: True

5 % 2 != 0
- Prediction: True
- Actual: True

[1] + 2
- Prediction: [3]
- Actual: Error: TypeError: can only concatenate list (not "int") to list

[1] + [2]
- Prediction: [1, 2]
- Actual: [1, 2]

[1] * 2
- Prediction: [2]
- Actual: [1, 1]

[1] * [2]
- Prediction: [2]
- Actual: Error: TypeError: can't multiply sequence by non-int of type 'list'

[] + [] == []
- Prediction: True
- Actual: True

{} + {}
- Prediction: Nothing
- Actual: Error: TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

```
