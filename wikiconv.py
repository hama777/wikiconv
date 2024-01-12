#!/usr/bin/python
# -*- coding: utf-8 -*-
#  convert pukiwiki format to Redmine wiki format
import os
import codecs
import re
import sys

re_image = re.compile("#ref\((.*)\)")
re_strong = re.compile(".*''.+''")

def test_proc() :
    line = "xxx''aaa''xxx"
    res = re_strong.match(line) 
    if res :
        print("strong")

def main_proc() :

#    infile = "Z:\\test.wik"
    args = sys.argv
    infile = args[1]
    pretag=0
    f = codecs.open(infile,'r','utf-8')
    for line in f :
        line = line.rstrip('\r\n')
        if not line.startswith(" ") and pretag == 1 :
            print("</pre>")
            pretag=0

        if line.startswith("***") :
            print("h3. %s \n" % line.replace("***","") ) 
            continue 
        if line.startswith("**") :
            print("h2. %s \n" % line.replace("**","") ) 
            continue 
        if line.startswith("*") :
            print("h1. %s \n" % line.replace("*","") ) 
            continue 
        if line.startswith("--") :
            print("** %s " % line.replace("--","") ) 
            continue 
        if line.startswith("-") :
            print("* %s " % line.replace("-","") ) 
            continue 
        if line.startswith("++") :
            print("## %s " % line.replace("++","") ) 
            continue 
        if line.startswith("+") :
            print("# %s " % line.replace("+","") ) 
            continue 
        if line.startswith(" ") :
            if pretag == 0 :
                print("<pre>")
            pretag=1
            print(line)
            continue 
        res = re_image.match(line) 
        if res :
            print("!%s!" % res.group(1)) 
            continue 
        res = re_strong.match(line) 
        if res :
            print(line.replace("''","*"))
            continue 

        print(line)
    f.close()


# -------------------------------------------------------------
main_proc()
#test_proc()
