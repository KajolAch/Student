
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

        stevens = Repository('\SEM 3\SSW 810 Python\HW01', True)
        for student in (stevens._students):
            actual_result[student] = stevens._students[student]._name
        self.assertEqual(actual_result, exp_res)
        # Repository._read_student_file()
    
    def test_instructor_file(self):
        stevens = Repository('\SEM 3\SSW 810 Python\HW01', True)
        actual_result = dict(

        )
        first_row_res = {'98765': 'Einstein, A'}
        for instructor in (stevens._instructors):
            actual_result[instructor] = stevens._instructors[instructor]._name
            break   # only stored first value
        self.assertEqual(actual_result, first_row_res)

      
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
