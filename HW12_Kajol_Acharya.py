#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 2019

@author: Kajol Acharya

     HW012_Kajol_Acharya implements Flask, Jinja2, sqlite3
"""
import sqlite3
from flask import Flask, render_template

app =Flask(__name__)

@app.route('/Hello')

def hello():
    return "Hello world"

@app.route('/Goodbye')

def seeya():
    return "See you later"



@app.route('/instructor')
        
def Instructor_summary():
    try:
        DB_FILE ="/sqlite/810_startup.db"
        db = sqlite3.connect(DB_FILE)
    except sqlite3.OperationalError:
        print(f"Error:Unable to open database at {DB_FILE}")    
    else:
        query = """select i.cwid,i.name,i.dept,g.Course, COUNT(StudentCWID)
                from Instructors as i,  Grades as g
                    where g.InstructorCWID = i.CWID
                group by g.Course , i.Name
                ORDER BY COUNT(StudentCWID) ASC"""
        data = [{'cwid':cwid, 'name':name, 'dept':dept,'course':course,'students':student}
        for cwid, name, dept, course, student in (db.execute(query))]
       
    print (data)  
    return render_template(
        'instructor.html',
        title="Stevens Repository",
        table_title ='Course and student count',
        instructors=data
    )
app.run(debug=True)