# Author :- Bishal Kunwar 290, Date: 26th sept 2023

# Question: In this task, you need to create a data structure that represents your personal information and access its individual components by indexing. This task is worth three marks.
# a) Creating a data structure:
# Create a data structure that represents your personal information, such as your name (first, middle, last), age, job, address, email address, and phone number. You may use any combination of built-in object types you like, such as lists, tuples, dictionaries, strings, and numbers.


# Solution:
# Create a dictionary to represent personal information. because it is suitable choice as it allows us to store various types of data associated with different keys.

student_detail = {
    'f_name' : 'Bishal', 
    'l_name' : 'Kunwar',
    'age' : 23,
    'job' : ['student', 'freelance'],
    'address' : {
        'country' : 'canada',
        'city' : 'ontario'
    },
    'email' : 'bishal@gmail.com',
    'phone' : '+ 647-878-9855'
}

# Accessing elements:
f_name = student_detail['f_name']
age = student_detail['age']
job = student_detail['job']
address = student_detail['address']['country']
email = student_detail['email']

# Printing the accessed elements:

print("First Name: ", f_name)
print("Age: ", age)
print("Job: ", job)
print("address: ", address)
print("email: ", email)

'''# Result:
First Name:  Bishal
Age:  23
Job:  ['student', 'freelance']
address:  canada
email:  bishal@gmail.com'''

#Observations from the research and doing:
# 1. As dictionaries are versitile, for personal detail, student detail to access each and every element from the stored multiple types of data, it helps with key and value.
# 2. nested dict helps to organize data more clear.
# 3. Indexing (i.e., using keys) provides an efficient way to access specific components of the data structure.