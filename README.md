# flask-example

## about

The API provides description of useful commands in JSON format.    
There are several topics:

- bash
- git
- python
- vim

## installation

`python3 -m virtualenv env`  

`source env/bin/activate` 

`pip install -r requirements.txt`  
   
   
## use
   
Launch `flask --app init run`  

Fetch random useful recipes by topic  `http://127.0.0.1:5000/api/<topic>`

Fetch a cheat sheet of topic   `http://127.0.0.1:5000/api/cheatsheet/<topic>`

## example

Send GET request:    
    
`http://127.0.0.1:5000/api/bash`   
   
Output:
```javascript 
{"command":"find . -name \"*kt\" | xargs cat | wc -l", "description":"count lines in .kt files (recursively)"}
```


