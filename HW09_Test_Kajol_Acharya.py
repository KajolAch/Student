
import unittest
import os
from HW09_Kajol_Acharya import Instructor, Student, Repository
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 2019

@author: Kajol Acharya

    Test cases for HW09_Kajol_Acharya student, instructor, repository
    FileAnalyzer
"""


class TestModuleGeneratorFile(unittest.TestCase):
    """ All test for HW09."""
    def test_student_file(self):
        "test the student file values"
        actual_result = dict()
        exp_res = {'10103': 'Baldwin, C', '10115': 'Wyatt, X', 
                   '10172': 'Forbes, I', '10175': 'Erickson, D',
                   '10183': 'Chapman, O',
                   '11399': 'Cordova, I', '11461': 'Wright, U', 
                   '11658': 'Kelly, P',
                   '11714': 'Morton, A', '11788': 'Fuller, E'}

        stevens = Repository('\SEM 3\Student\Student', True)
        for student in (stevens._students):
            actual_result[student] = stevens._students[student]._name
        self.assertEqual(actual_result, exp_res)
        # Repository._read_student_file()
    
    def test_instructor_file(self):
        stevens = Repository('\SEM 3\Student\Student', True)
        actual_result = dict()
        first_row_res = {'98765': 'Einstein, A'}
        for instructor in (stevens._instructors):
            actual_result[instructor] = stevens._instructors[instructor]._name
            break   # only stored first value
        self.assertEqual(actual_result, first_row_res)


    def test_student_prettytable(self):
        stevens = Repository('\SEM 3\Student\Student', False)
        student_res =dict()
        exp_res ={'10103': ('Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']), 
        '10115': ('Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']), 
        '10172': ('Forbes, I', 'SFEN', ['SSW 555', 'SSW 567']), '10175': ('Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687']), 
        '10183': ('Chapman, O', 'SFEN', ['SSW 689']), 
        '11399': ('Cordova, I', 'SYEN', ['SSW 540']), 
        '11461': ('Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800']), '11658': ('Kelly, P', 'SYEN', ['SSW 540']), 
        '11714': ('Morton, A', 'SYEN', ['SYS 611', 'SYS 645']), '11788': ('Fuller, E', 'SYEN', ['SSW 540'])}
        for student in stevens._students.values():
            student_res[student._cwid] = student._name, student._major, sorted(student._course.keys())
        self.assertEqual(exp_res,student_res)   


    def test_instructor_prettytable(self):
        stevens = Repository('\SEM 3\Student\Student', True)
        instructor_res =dict()
        exp_res ={'98765': ('Einstein, A', 'SFEN', ['SSW 540', 'SSW 567']), 
        '98764': ('Feynman, R', 'SFEN', ['CS 501', 'CS 545', 'SSW 564', 'SSW 687']), 
        '98763': ('Newton, I', 'SFEN', ['SSW 555', 'SSW 689']), 
        '98762': ('Hawking, S', 'SYEN', []), '98761': ('Edison, A', 'SYEN', []), 
        '98760': ('Darwin, C', 'SYEN', ['SYS 611', 'SYS 645', 'SYS 750', 'SYS 800'])}
        for instructor in stevens._instructors.values():
            instructor_res[instructor._cwid] = instructor._name, instructor._dept, sorted(instructor._courses.keys())
        
        #print(instructor_res)
        self.assertEqual(exp_res,instructor_res)   
      
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
