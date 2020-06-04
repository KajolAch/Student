#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 2019

@author: Kajol Acharya

     HW09_Kajol_Acharya implements class Student,Instructor, Repository
"""
from HW08_Kajol_Acharya import file_reading_gen
from prettytable import PrettyTable
from collections import defaultdict
from HW10_Kajol_Acharya import Major
import os


class Student:
    "has an instance of 1 student having cwid, name, major, courses"
    PT_FIELDS = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required',
                'Remaining Electives' ]
    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._course = dict()
        self._majors = dict()

    def pt_row(self):
        "returns what is needed for pretty table: cwid, name, major, students"
        return self._cwid, self._name, self._major, self._majors[self._major].passing_grade((self._course)), self._majors[self._major].remaining_required(set(self._course.keys())), self._majors[self._major].remaining_electives(set(self._course.keys()))
        

    def add_courses(self, course, grade):
        """adds courses and grade to the instance of Student"""
        self._course[course] = grade

    def add_major(self, dept, major):
        """adds major to the instance of Student"""
        self._majors[dept] = major.get(dept) 

class Instructor:
    "has an instance of 1 instructor having cwid, name, dept, courses"
    PT_FIELDS = ['CWID', 'Name', 'Dept', 'Course', '#Students']

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses = defaultdict(int)
        
    def pt_row(self):
        "returns a generator with cwid, name, dept, courses, no of students"
        for courses, students in self._courses.items():
            yield [self._cwid, self._name, self._dept, courses, students]

    def add_courses(self, course):
        """adds courses to the instance of Instructor"""
        self._courses[course] += 1

           
class Repository:
    "hold the students, instructors and grades for a single University"
    def __init__(self, path, pt=False):
        self.path = path
        self._students = dict()
        self._instructors = dict()
        self._majors = dict()
        self._read_majors_file(os.path.join(path, 'majors.txt'))
        self._read_student_file(os.path.join(path, 'students.txt'))
        self._read_instructors_file(os.path.join(path, 'instructors.txt'))
        self._read_grades_file(os.path.join(path, 'grades.txt'))
       
        if(pt): 
            self.majors_prettytable()
            self.student_prettytable()
            self.instructor_prettytable()
            
    def _read_majors_file(self, path):
        """read the majors file"""
        try:
            for dept, flag, courses in file_reading_gen(path, 3, sep='\t',
                                                     header=True):
                # print(dept,flag, courses)
                if dept in self._majors:                 
                    self._majors[dept].add_courses(flag,courses)
                else:
                    self._majors[dept]= Major(dept)
                    self._majors[dept].add_courses(flag,courses)   
        except FileNotFoundError as fne:
            print(fne)
        except ValueError as ve:
            print(ve)

    def _read_student_file(self, path):
        """read the student file"""
        try:
            for cwid, name, major in file_reading_gen(path, 3, sep=';',
                                                      header=True):
                self._students[cwid] = Student(cwid, name, major)             
                self._students[cwid].add_major(major, self._majors)
        except FileNotFoundError as fne:
            print(fne)
        except ValueError as ve:
            print(ve)

    def _read_instructors_file(self, path):
        """read the instructors file"""
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='|',
                                                     header=True):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except FileNotFoundError as fne:
            print(fne)
        except ValueError as ve:
            print(ve)

    def _read_grades_file(self, path):
        """read the grades file"""
        try:
            for cwid, course, grade, instructor_cwid in file_reading_gen(path, 4, sep='|', header=True):
                if cwid in self._students:
                    self._students[cwid].add_courses(course, grade)
                else:
                    print(f"Found grade for unknown student{cwid}")
                if instructor_cwid in self._instructors:
                    self._instructors[instructor_cwid].add_courses(course)
                else:
                    print(f"Got course of unknown instructor{instructor_cwid}")
        except FileNotFoundError as fne:
            print(fne)
        except ValueError as ve:
            print(ve)

    def student_prettytable(self):
        pt = PrettyTable()
        pt.field_names = Student.PT_FIELDS
        # print(Student.PT_FIELDS)
        for student in self._students.values():
            pt.add_row(student.pt_row())
        print("Student Summary")    
        print(pt)


    def instructor_prettytable(self):
        pt = PrettyTable()
        pt.field_names = Instructor.PT_FIELDS
        for instructor in self._instructors.values():
            for row in instructor.pt_row():
                # print(row)
                pt.add_row(row)
        print("Instructor Summary")     
        print(pt)

    def majors_prettytable(self):
            pt = PrettyTable()
            pt.field_names = Major.PT_FIELDS
            for dept in self._majors:
                pt.add_row(self._majors[dept].pt_row())
            print("Majors Summary")     
            print(pt)
            
if __name__ == '__main__':
    stevens = Repository('\SEM 3\Student\Student', True)