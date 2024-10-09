'''
    Lesson: If statments
    Author: Kaylee Baichulall
    Date Created: Oct 9, 2024
    Date Last Modified: Oct 9, 2024
'''

def q1(): 
  num = int(input("In: "))
  num1 = num % 2
  if num1 == 0:
    print(f"{num} is even")
  if num1 == 1:
    print(f"{num} is odd")

def q2(): 
  name = input("In: ")
  if name == "Kalisz":
    print("teacher")
  if name != "Kalisz":
    print("student")


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
