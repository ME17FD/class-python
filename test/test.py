import sqlite3
from main import *
from randomdata import *
from random import choice,randint

"""CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        lname TEXT NOT NULL,
        major TEXT NOT NULL,
        year INTEGER DEFAULT 0 NOT NULL);"""
"""CREATE TABLE IF NOT EXISTS GRADES(
        module TEXT NOT NULL,
        grd INTEGER DEFAULT NULL,
        studentid INTEGER NOT NULL,
        FOREIGN KEY(studentid) REFERENCES Students(id)
        );"""
studentlist=[]





