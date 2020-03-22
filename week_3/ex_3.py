# Student Marks Administration
# Pete Dwyer 01/11/17
# Saul Johnson 20/06/2019

from datafile import data


def show_raw_data(dat):
   for ind in range(0, len(data), 2):
       print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4))

#Groups and prints students who gained distinction grade
def show_distinction(dat):
   for ind in range(0, len(data), 2):
         if int(dat[ind + 1]) >= 70:
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), "Distinction".rjust(10))          

#Groups and prints students who gained merit grade
def show_merit(dat):
   for ind in range(0, len(data), 2):
         if 70 > int(dat[ind + 1]) >= 60:
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), "Merit".rjust(10))

#Groups and prints students who gained pass grade
def show_pass(dat):
   for ind in range(0, len(data), 2):
        if 60 > int(dat[ind + 1]) >= 40:
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), "Pass".rjust(10))

#Groups and prints students who failed but are eligible to resubmit
def show_fail_resub(dat):
   for ind in range(0, len(data), 2):
        if 30 < int(dat[ind + 1]) <= 40:
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), "Fail, eligible to resubmit".rjust(10))

#Groups and prints students who failed
def show_fail(dat):
   for ind in range(0, len(data), 2):
        if 30 > int(dat[ind + 1]):
            print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4), "Fail".rjust(10))

#Creates a list containing just the marks
def marks(dat):
    marks = []
    for ind in dat:
        if type(ind) == (int):
            marks.append(ind)
    return marks

#Creates a list containing just the names
def names(dat):
    names = []
    for ind in dat:
        if type(ind) == (str):
            names.append(ind)
    return names

#Find the index of the highest mark
high_index = (marks(data).index(max(marks(data))))

#Prints the highest mark and name of student by using the index
#of the highest mark in mark list and corresponding index in name list
def print_max(dat):
    print(("The highest mark was "),max(marks(data)),("scored by "),(names(data)[high_index]))


#Returns average value for marks rounded to whole number
def average_mark(dat):
    total = 0
     
    for i in marks(dat):
        total = total + i
    return(round(total / len(marks(dat))))
    
#Prints average mark rounded to whole number
def show_average_mark():
   print("The average mark is:", average_mark(data))

#Counts number of below average marks
def below_average(dat):
    below = 0 
    for ind in range(0, len(dat),2):
       if int(dat[ind + 1]) < average_mark(data):
          below += 1
    return below

#Counts number of above average marks
def above_average(dat):
    above = 0
    for ind in range(0, len(dat),2):
       if int(dat[ind + 1]) > average_mark(dat):
           above += 1
    return above
    
#Prints number of below average and number of above average marks
def above_below_ave(dat):
    print("There were", below_average(dat),"students with below average marks and", above_average(dat),"students with above average marks")


#Prints pass grades
def show_grade(dat):
    show_distinction(data)
    print("")
    show_merit(data)
    print("")
    show_pass(data)

#Prints fail grades
def show_fails(dat):
    show_fail_resub(data)
    print("")
    show_fail(data)

#Prints the range of marks attained
def range_of_marks(dat):
    print("The range of marks is: Lowest", min(marks(dat)),": Highest",(max(marks(dat))))




show_grade(data)
print("")
print("")
show_fails(data)
print("")
print("")
print_max(data)
range_of_marks(data)
show_average_mark()
above_below_ave(data)
