
import unittest
import os
from HW11_Kajol_Acharya import Instructor, Student, Repository
from HW10_Kajol_Acharya import Major
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 2019

@author: Kajol Acharya

    Test cases for HW09_Kajol_Acharya student, instructor, repository
    FileAnalyzer
"""


class TestModuleGeneratorFile(unittest.TestCase):
    """ All test for HW11."""
    
    
    def test_instructor_file(self):
        stevens = Repository('\SEM 3\Student\Student', True)
        actual_result = dict()
        first_row_res = {'98764': 'Cohen, R'}
        for instructor in (stevens._instructors):
            actual_result[instructor] = stevens._instructors[instructor]._name
            break   # only stored first value
        self.assertEqual(actual_result, first_row_res)


    
    def test_instructor_prettytable(self):
        stevens = Repository('\SEM 3\Student\Student', True)
        instructor_res =dict()
        exp_res = {'98764': ('Cohen, R', 'SFEN', ['CS 546']), 
        '98763': ('Rowland, J', 'SFEN', ['SSW 555', 'SSW 810']), 
        '98762': ('Hawking, S', 'CS', ['CS 501', 'CS 546', 'CS 570'])}
        for instructor in stevens._instructors.values():
            instructor_res[instructor._cwid] = instructor._name, instructor._dept, sorted(instructor._courses.keys())
        self.assertEqual(exp_res,instructor_res)  

    def test_instructor_table_db(self):
        stevens = Repository('\SEM 3\Student\Student', True)
        instructor_res =dict()
        exp_res = {0: ('98762', 'Hawking, S', 'CS', 'CS 501', 1), 
        1: ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1), 
        2: ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
         3: ('98762', 'Hawking, S', 'CS', 'CS 570', 1), 
         4: ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
          5: ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4)}
        for i,_instructorsDB in enumerate(stevens._instructorsDB.values()):
            instructor_res[i]=_instructorsDB
        #print(instructor_res)    
        self.assertEqual(exp_res,instructor_res) 
      
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
