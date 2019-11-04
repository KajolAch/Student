#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 2019

@author: Kajol Acharya

     HW08_Kajol_Acharya implemenst  date-arithmetic, field separated file
     reader, Scanning directories and files
"""
from datetime import datetime, timedelta
from prettytable import PrettyTable
import os


def date_arithmetic():
    """ implement Date Arithmetic Operations"""
    date1 = "27 Feb 2000"
    date2 = "27 Feb 2017"
    num_days = 3
    date3 = "31 Oct 2017"
    date4 = "1 Jan 2017"
    d1 = datetime.strptime(date1, "%d %b %Y")
    d2 = datetime.strptime(date2, "%d %b %Y")
    d3 = datetime.strptime(date3, "%d %b %Y")
    d4 = datetime.strptime(date4, "%d %b %Y")
    three_days_after_02272000 = d1 + timedelta(days=num_days)
    three_days_after_02272017 = d2 + timedelta(days=num_days)
    days_passed = d3 - d4

    return three_days_after_02272000, three_days_after_02272017, days_passed


def file_reading_gen(path, fields, sep=',', header=False):
    """ read field-separated text files and yield a tuple with all of values"""
    try:
        file = open(path)
    except FileNotFoundError as f:
        raise FileNotFoundError(f) 
    if header:
        next(file)
    for line in file:
        line = line.strip('\n')
        res = line.split(sep)
        if len(res) == fields:
            yield res  # yield tuple(res)
        else:
            raise ValueError(f"ValueError: {path} has {len(res)} fields but"
                             f" expected {fields}")


class FileAnalyzer:
    """ calculate a summary of the file ."""
    def __init__(self, directory):
        """ intialize values."""
        self.directory = directory
        self.files_summary = dict()
        self.analyze_files()  # summerize the python files data
        self.pretty_print()

    def analyze_files(self):
        """ calculate  files_summary """
        list = os.listdir(self.directory)
        for file_name in list:
            if file_name.endswith(".py"):
                class_cnt = 0
                function_cnt = 0
                line_cnt = 0
                char_cnt = 0
                path = os.path.join(self.directory, file_name)
                try:
                    file = open(path)
                except FileNotFoundError:
                    print("Wrong file or file path")
                for line in file:
                    line_cnt += 1
                    char_cnt += len(line)
                    line = line.strip()
                    if line.startswith("def "):
                        function_cnt += 1
                    if line.startswith("class "):
                        class_cnt += 1
                    self.files_summary[file_name] = {'class': class_cnt,
                                                     'function': function_cnt,
                                                     'line': line_cnt,
                                                     'char': char_cnt}

    def pretty_print(self):
        """ print out pretty table from data stored in self.files_summary"""
        pt = PrettyTable()
        pt.field_names = ["FileName", "Classes", "Functions", "Lines", 
                          "Characters"]
        for files in self.files_summary:
            val1 = [files]
            val2 = list(self.files_summary[files].values())
            val1.extend(val2)
            pt.add_row(val1)
        print(pt)
