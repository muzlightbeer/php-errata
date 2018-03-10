#!/usr/bin/env python3

import os
import glob
import re

class Errata: 
    def parse_docs(self): 
        function_name_start = "docs/function."
        function_name_end = ".html"
        keywords = ["security", "deprecat", "unsafe", "warning", "code exec", "danger"] # changes here need updating below
        security_matches = []
        deprecat_matches = []
        unsafe_matches = []
        warning_matches = []
        pop_the_champagne_matches = []
        danger_matches = []
        security_fd = open("security.txt", "a")
        deprecat_fd = open("deprecated.txt", "a")
        unsafe_fd = open("unsafe.txt", "a")
        warning_fd = open("warning.txt", "a")
        code_exec_fd = open("code-exec.txt", "a")
        danger_fd = open("danger.txt", "a")
        for filename in glob.iglob("docs/**/function.*.html", recursive=True): 
            fd = open(filename, "r")
            current_file = fd.read()
            for item in keywords:
                temp = re.search(item, current_file, re.IGNORECASE)
                if temp:
                    if item == "security":
                        function_name = re.search('%s(.*)%s' % (function_name_start, function_name_end), filename).group(1)
                        function_name = function_name.replace("-","_")
                        security_matches.append(function_name)
                    if item == "deprecat":
                        function_name = re.search('%s(.*)%s' % (function_name_start, function_name_end), filename).group(1)
                        function_name = function_name.replace("-","_") 
                        deprecat_matches.append(function_name) 
                    if item == "unsafe":
                        function_name = re.search('%s(.*)%s' % (function_name_start, function_name_end), filename).group(1)
                        function_name = function_name.replace("-","_")
                        unsafe_matches.append(function_name)
                    if item == "warning":
                        function_name = re.search('%s(.*)%s' % (function_name_start, function_name_end), filename).group(1)
                        function_name = function_name.replace("-","_")
                        warning_matches.append(function_name)
                    if item == "code exec":
                        function_name = re.search('%s(.*)%s' % (function_name_start, function_name_end), filename).group(1)
                        function_name = function_name.replace("-","_")
                        pop_the_champagne_matches.append(function_name)
                    if item == "danger":
                        function_name = re.search('%s(.*)%s' % (function_name_start, function_name_end), filename).group(1)
                        function_name = function_name.replace("-","_")
                        danger_matches.append(function_name)
            fd.close() 
        if len(security_matches) != 0:
            for x in security_matches:
                security_fd.write("%s\n" % x)

        if len(deprecat_matches) != 0:
            for x in deprecat_matches:
                deprecat_fd.write("%s\n" % x)

        if len(unsafe_matches) != 0:
            for x in unsafe_matches:
                unsafe_fd.write("%s\n" % x)

        if len(warning_matches) != 0:
            for x in warning_matches:
                warning_fd.write("%s\n" % x)

        if len(pop_the_champagne_matches) != 0:
            for x in pop_the_champagne_matches:
               code_exec_fd.write("%s\n" % x)
        
        if len(danger_matches) != 0:
            for x in danger_matches:
                danger_fd.write("%s\n" %x)
 
        security_fd.close()
        deprecat_fd.close()
        unsafe_fd.close()
        warning_fd.close()
        code_exec_fd.close()
        danger_fd.close()
        
def main():
    x = Errata()
    x.parse_docs()

if __name__ == "__main__":
    main()
