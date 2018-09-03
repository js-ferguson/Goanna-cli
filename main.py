#Goanna PMS

from classes.patient import Patient
from classes.patientFile import PatientFile
import datetime

pat_dict = {'None':'None'}

def main_menu():

    print('\nGoanna PMS - Main menu \n')
    print('(N)ew patient')
    print('(O)pen patient file')
    print('(S)earch patient')
    print('(Q)uit \n')

    greeting = input('What would you like to do?: ')
    if greeting.lower() in ['n', 'new']:
        temp_pat = Patient()
        PatientFile.create_new_file(
            temp_pat.getPatnum(),
            temp_pat.getFullName(),
            temp_pat.getFName(),
            temp_pat.getLName(),
            temp_pat.getPatRecord()
            )
        temp_pat.add_record_library()
        main_menu()
    elif greeting.lower() in ['o', 'open']:
        id = input('enter first name, last name and patient number as a single string: ')
        PatientFile.open_existing_file(id)
        main_menu()
    elif greeting.lower() in ['s', 'search']:
        search_name()
        #main_menu()
    else:
        print('Enter N to start a new patient file \nPress O to open an existing patient file')
        main_menu()

def search_name():
    entry = []
    substr = input('enter string: ')
    try:
        with open ('patient_list.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if line.lower().find(substr) != -1:
                    entry.append((linenum, line.rstrip('\n')))
                    for linenum, line in entry:
                        print("Line ", linenum, ": ", line, sep='')
    except FileNotFoundError:
        print("Log file not found.")
    open_file = input('would you like to open this file? [y/n]: ')
    if open_file == 'y':
        str1 = ''.join(str(e) for e in entry)
        clean = str1.replace(" ", "")
        id = clean[4:-2]
        PatientFile.open_existing_file(id)
        main_menu()
    else:
        main_menu()



    '''search_term = input("Enter a name or patient number: ")
    with open("patient_list.txt") as file:
        for line in file:
            line = line.rstrip()  # remove '\n' at end of line
            if search_term == line:
                print(line)
                '''
main_menu()
