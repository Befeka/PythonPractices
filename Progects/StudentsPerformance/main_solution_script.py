###################################
# A script to students performce in the following format
# Average Student Grade : 50.44
# Hardest Subject : geography
# Easiest Subject : english
# Best Performing Grade : 6
# Worst Performing Grade : 5
# Best Student ID : 549
# Worst Student ID : 637
##################################

import json
from os import path

SUBJECTS = ["math", "science", "history", "english", "geography"]
NUM_STUDENTS = 1000

def report_card(directory,student_id):
    """_summary_
    load studen record from json file
    return dictionary 
    Args:
        directory (file_path): student file directory path
        student_id (int): student id
    """
    
    # Extract the absolute path and  main file
    abs_file_path = path.abspath(__file__)
    # Extract base directory from the absolute path file 
    base_directory = path.dirname(abs_file_path)
    # Join the folder and file name
    file_path = path.join(directory,f'{student_id}.json')
    # join the base directory and the file path
    full_path = path.join(base_directory, file_path)
    
    try:
        with open(full_path,'r') as file:
            card_report = json.load(file)
    except FileNotFoundError :
        return {}
    
    return card_report

def report_cards(directory,num_students) -> list:
    """
    Store all students report card in list
    Args:
        directory (path): student file directory path
        num_students (int): total number of students
    """
    card_reports = []
    
    for student in range(num_students):
        card_report = report_card(directory,student)
        card_reports.append(card_report)
    
    return card_reports

def average_studens_mark(card_reports, subjects)-> dict:
    """a function to calculate and store students average 
        in card report

    Args:
        card_reports (list): a list of dictionary with students report
        subjects (_type_): subjects

    Returns:
        dict: students card report with additional key average_mark
    """
    
    for card_report in card_reports:
        mark = 0
        for subject in subjects:
            if subject not in card_report:
                continue
            mark += card_report[subject] 
        card_report['average_mark'] = mark /len(subjects)
        
def average_mark(card_reports)-> float:
    """calculate and return the average mark of all students

    Args:
        card_reports (list): a list of dictionary with students report

    Returns:
        float: returns the average mark of all students
    """
    
    average_mark = 0
    for card_report in card_reports:
        average_mark += card_report['average_mark']
        
    average_mark /= len(card_reports)
    
    return average_mark

def subject_average(card_reports,subjects)-> dict:
    """A function to calculate and store the average of each subjects

    Args:
        card_reports (_type_): card_reports (list): a list of dictionary with students report
        subjects (list): list of subjects

    Returns:
        dict: The average mark of each subjects with key subject  and value average
    """
    
    # Initialize the value of average value of  subjects to zero
    average_subject = {subject :0 for subject in subjects}
    
    for card_report in card_reports:
        for subject in subjects:
            # adds the value of each subject 
            average_subject[subject] += card_report[subject]
            
    # Divide the total sum of each subject by the num of students
    
    for subject in subjects:

        average_subject[subject] /= len(card_reports)
        
    return average_subject

def grade_by_average(card_reports)-> list:
    
    """Calculate and returns the avarage mark of students by grade

    Args:
        card_reports (_type_): _description_

    Returns:
        list: list of dictionary each with key grade and value average mark
    """

    # Initialize grades from 1 to 8 to each as a list 
    grade_level = {grade : [] for grade in range(1,9)}
    
    for card_report in card_reports:
        grade = card_report['grade']
        average_grade = card_report['average_mark']
        grade_level[grade].append(average_grade )
        
    for grade in  grade_level:
        grade_level[grade] = sum(grade_level[grade])/ len(
            grade_level[grade])
        
    return grade_level

def main():
    
    card_reports = report_cards("students", NUM_STUDENTS)
    average_studens_mark(card_reports,SUBJECTS)
    average_tot_mark = round(average_mark(card_reports),2)
    subj_average = subject_average(card_reports,SUBJECTS)
    sorted_sub_average = sorted(subj_average.items(),
                                key=lambda x:x[1])

    grade_lev_av = grade_by_average(card_reports)

    sorted_grade_lev_av = sorted(grade_lev_av.items(),
                                 key=lambda x:x[1])
    student_sorted_by_ave = sorted(card_reports,
                                   key=lambda x:x['average_mark'])
    
    best_student_id = student_sorted_by_ave[-1]['id']
    worst_student_id = student_sorted_by_ave[-1]['id']
    
    # Print the output 
    print(f'Average Student Grade : {average_tot_mark}')
    print(f'Hardest Subject : {sorted_sub_average[0][0]}')
    print(f'Easiest Subject : {sorted_sub_average[-1][0]}')
    print(f'Best Performing Grade : {sorted_grade_lev_av[-1][0]}')
    print(f'Worst Performing Grade : {sorted_grade_lev_av[0][0]}')
    
    print(f'Best Student ID : {best_student_id}')
    print(f'Worst Student ID : {best_student_id}')
if __name__ =="__main__":
    main()