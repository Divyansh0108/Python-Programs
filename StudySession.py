import random

print('''
      Exams are coming,and the program will tell you which on to study today.
''')

subjects = input("So, enter all the subjects you have to study for the exam, separated by a comma: ").split(',')

print(f"So today we are studying: " + str(subjects[random.randint(0,len(subjects))]))