# importing libraries
import random
import sys

# Exception handling for command line argument user input
try:
    if len(sys.argv) != 1:
        file = open(sys.argv[1], 'r')
        student = file.readlines()
        for lines in student:
            splited_lines = lines.split()
            student1 =list( ''.join(splited_lines[1:])) #join the splited lines from 1 to last and make it list
            if '-' in student1:  #it search chr(-) from student1 and remove it from student1
            	student1.remove("-")
            if "'" in student1:
            	student1.remove("'")
            student2=''.join(student1)  #join the list student1 and assigned it into new variable callled student2
            for i in list(student2): #this loop find index of chr(,) in student2 and assigned it into variable j
                j = list(student2).index(",")
            firstn = "".join(list(student2[0:j])) #this line make the list of student2 and join the chr 0 to j (i.e. index of comma)
            lastn = "".join(list(student2[j+1:]))
            email = ''
            for k in list(lastn): #this loop check the uppercase chracter in lastn and assigned it into email
                if k.isupper():
                    email += k+"."
            students_emails = (splited_lines[0]+" "+email+firstn+str(
                random.choice(range(1000, 10000)))+"@poppleton.ac.uk").lower()
            file1 = open('Student_gmail.txt', 'a+')
            file1.write(students_emails+"\n")
        file1.close()
        file.close()
    else:
        print("Error: Missing Command-Line Argument.")
except FileNotFoundError:
    print(f"Error: Cannot open \"{sys.argv[1]}\". sorry about that.")
