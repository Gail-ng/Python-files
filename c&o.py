f=open("classes and objects.py","r")

print(f.name)

contents=f.read()
print(contents)
f.close()

# Python3 program to demonstrate defining a class   
# Class for Student :
pass

# A simple class attribute

name = Bob
age = 26
score = 20.90
track = UI/UX

class Student :
    def init(self,name,age,score):
       self.name ="Bob"
       self.age=26
       self.score=20.90
       self.track="UI/UX"
       
def speak(self):
    print ("Hi, my name is",self.name)


   #float for single parameter as integer

def adult(self):       
       if self.age <18 :
            print (float("I am not an adult"))
            if self.age>18 :
                print (float("I am an adult"))
         

# Program to show changes made to a class variable
 # Class of Student
 
class Student:
    def change_name(self, name, age, score):
        self.name =("Peter")
        self.age =32
        self.score=()

    def change_name(self):
       print("Hey,my name is", self.name , "the new class captain for SS3")

    def character(self):
        if self.score <32 :
            print("I am not a smart student")
            if self.age>32 :
                print("I am a brilliant student")
