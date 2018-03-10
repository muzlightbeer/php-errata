#!/usr/bin/env python3

import os
import glob
import re

security_functions = []
deprecat_functions = []
unsafe_functions = []
warning_functions = []
pop_the_champagne_functions = []
danger_functions = []

def create_lists():
    global security_functions
    global deprecat_functions
    global unsafe_functions
    global warning_functions
    global pop_the_champagne_functions
    global danger_functions

    fd = open("security.txt", "r")
    temp = fd.readlines()
    security_functions = [x.strip() for x in temp] #https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
    fd.close()

    fd = open("deprecated.txt", "r")
    temp = fd.readlines()
    deprecat_functions = [x.strip() for x in temp]
    fd.close()

    fd = open("unsafe.txt", "r")
    temp = fd.readlines()
    unsafe_functions = [x.strip() for x in temp]
    fd.close()

    fd = open("warning.txt", "r")
    temp = fd.readlines()
    warning_functions = [x.strip() for x in temp]
    fd.close

    fd = open("code-exec.txt", "r")
    temp = fd.readlines()
    pop_the_champagne_functions = [x.strip() for x in temp]
    fd.close()

    fd = open("danger.txt", "r")
    temp = fd.readlines()
    danger_functions = [x.strip() for x in temp]
    fd.close()
 
def check_code():
    try:
        os.stat("output")
    except:
        os.mkdir("output")
    security_found_fd = open("output/security_found.txt", "a")  
    deprecated_found_fd = open("output/deprecated_found.txt", "a")
    unsafe_found_fd = open("output/unsafe_found.txt", "a")
    warning_found_fd = open("output/warning_found.txt", "a")
    code_exec_found_fd = open("output/code_exec_found.txt", "a")
    danger_found_fd = open("output/danger_found.txt", "a")
    for filename in glob.iglob("SOURCE/**/*.php*", recursive=True): 
        fd = open(filename, "r")
        current_file = fd.read()

        for item in security_functions:
            temp = re.search(item, current_file, re.IGNORECASE)
            if temp: 
                security_found_fd.write("%s in %s\n" % (item, filename))
       
        for item in deprecat_functions:
            temp = re.search(item, current_file, re.IGNORECASE)
            if temp: 
                deprecated_found_fd.write("%s in %s\n" % (item, filename))

        for item in unsafe_functions:
            temp = re.search(item, current_file, re.IGNORECASE)
            if temp:
                unsafe_found_fd.write("%s in %s\n" % (item, filename))

        for item in warning_functions:
            temp = re.search(item, current_file, re.IGNORECASE)
            if temp:
                warning_found_fd.write("%s in %s\n" % (item, filename))

        for item in pop_the_champagne_functions:
            temp = re.search(item, current_file, re.IGNORECASE)
            if temp:
                code_exec_found_fd.write("%s in %s\n" % (item, filename)) 

        for item in danger_functions:
            temp = re.search(item, current_file, re.IGNORECASE)
            if temp:
                danger_found_fd.write("%s in %s\n" % (item, filename))

        fd.close()

    security_found_fd.close()
    deprecated_found_fd.close()
    unsafe_found_fd.close()
    warning_found_fd.close()
    code_exec_found_fd.close()
    danger_found_fd.close()

def main():
    create_lists()   
    check_code()

if __name__ == "__main__":
    main()
