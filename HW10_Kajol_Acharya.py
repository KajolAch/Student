
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed nov 06 2019

@author: Kajol Acharya

     HW 10_Kajol_Acharya defines class Major
"""

class Major:
    PT_FIELDS = [ 'Dept', 'Required', 'Electives']
    PASSING_GRADES =['A','A-','A+','B','B+','B-','C+','C']

    def __init__(self, dept):
        self._dept = dept

        # self._courses = dict()
        self._required = set()
        self._electives = set()

    def add_courses(self, flag, course):
        """flag has value R/E adds remaning and elective courses"""
        # self._courses[flag].add(course)
        if flag.upper() == 'R':
            self._required.add(course)
        elif flag.upper() == 'E':
            self._electives.add(course)           
        else:
            raise ValueError(f"Unexpected flag {flag} encountered in majors.txt")
        
    def remaining_required(self, courses):
        "returns the remaining required courses"
        return self._required.difference(courses)

    def remaining_electives(self, courses):
        "returns elective courses or none if it is taken"
        if (self._electives.intersection(courses)!= set()):
            return None
        else:
            return  self._electives.difference(courses)

    def passing_grade(self, course):
        "returns set of courses which is included in passing grades"
        return {course for course,grade in course.items() if grade in Major.PASSING_GRADES}

    def pt_row(self):
        "returns what is needed for pretty table: dept, required, electives"
        return self._dept, self._required, self._electives
