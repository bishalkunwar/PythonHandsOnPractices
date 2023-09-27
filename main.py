print("hello world")

'''
Author : Hesam Akbari
Python2 : second session processing Data using files in python

Review of python 1 with files.
Using text file in python
file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

** all the input and output are inform of strings!
afile = open('test.txt','w')
alist = ['3\n','6\n', '8\n', '10\n', '11\n', '15\n']
afile.writelines(alist)
afile.close()
'''
# I like to write an application which opens a test.txt store the data which is a number and greater
# that equal to 10 into separate line!
'''
afile = open('test.txt','w')
alist = ['3\n','6\n', '8\n', '10\n', '11\n', '15\n']
afile.writelines(alist)
afile.close()
'''
alist = ['3\n','6\n', '8\n', '10\n', '11\n', '15\n']
with open('test.txt','w' ) as afile:
    afile.writelines(alist)

'''
infile = open('test.txt')
outfile = open('text2.txt','w')
lines = infile.readlines()
print(lines)
for line in lines :
    if line.strip('\n').isdigit() and int(line.strip('\n')) >= 10:
        outfile.write(line)
infile.close()
outfile.close()
'''
with open('test.txt') as infile, open('test2.txt','w') as outfile:
    for line in infile:
        if line.strip('\n').isdigit() and int(line.strip('\n')) >= 10:
            outfile.write(line)

#------------------------------------------------DATA FILES---------------------------
'''
 ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
'''
# what if I like to store complex data in a file! ( list, tuples, dictionaries, objects, JSON data...)
'''
python object serialization (AKA pickling): its a good choice for complex data to stored on a file
you convert a complex data into sequence of zero's and ones' (binary) and store it in a file
this process called serialization

Deserialization is convert the data stored in a file into proper structure they deserve 
pickling ----> process  of converting complex object into byte stream
unpickling --------> is the inverse operation
'''

import pickle
time = int(input('Enter the number of data: '))
data = []
for i in range(time): data.append(int(input(f'Enter data # {i+1}')))
print(data)
# pickling the list to binary and dump it
student1 = {'ID': 'C0777777', 'name':'Hesam', 'age': 38, 'marks': (65, 67,86,45)}
student2 = {'ID': 'C0777788', 'name':'Tony', 'age': 28, 'marks': (45, 77,86,45)}
name = 'Hesam'
value = 34
with open('datafile.txt','wb') as file :
    pickle.dump(data, file)
    pickle.dump(student1, file)
    pickle.dump(student2, file)
    pickle.dump(value, file)
# unpickling the data by loading and converting it back
with open('datafile.txt','rb') as file:
    while True:
        try:
            data = pickle.load(file)
            print(data,type(data),sep='  ------------>')
        except EOFError: break

# PICKLE FILES CAN BE HACKED AND ITS NOT SECURE, IF YOU RECIEVE A RAW PICKLE FILE OVER THE NETWORK
# DO NOT TRUST THEM YET IF YOU DO YOUR OWN PICKLING YOU ARE SAFE.

#--------------------------------------------------------------------------------------
# python is a really good tool to manipulate and visualizing data...
# Excel sheet and CSV files also are comment to dealt with
# EXCEL and CSV ----> great tools to create tabular form data (table base data)
#-----------------------------------------------------------------------------
import csv
csv_rowList = [['c077337733','Marcelo','33','89'], ['c077338833','Jay','27','78'], ['c076537767','Priyan','25','100']]
with open('students.csv','w', newline='') as file:
    writer = csv.writer(file) # writting in comma seperated value (CSV)
    writer.writerow(['student_ID', 'name','age','mark'])
    writer.writerows(csv_rowList)
sum = 0
counter = 0
''' Appling reader from csv
with open('students.csv','r') as file:
    csv_file = csv.reader(file)
    for line in csv_file :
        print(line)
        if line[3].isdigit():
            sum += int(line[3])
            counter += 1
    print(sum/counter)
'''
adict = {1:2, 2:3, 3:4}
print(adict)
alistTuple = [(1,2), (2,3), (3,4)]
adict2 = dict(alistTuple)
print(adict2)
alistStudent = []
with open('students.csv','r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file :
        print(dict(row))
        alistStudent.append(dict(row))
sum = 0
for std in alistStudent : sum += int(std['mark'])
print('average is ', sum/len(alistStudent))








