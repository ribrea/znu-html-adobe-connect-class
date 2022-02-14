## Create html class instead of flash for adobe connect meeting

# Run
#### 1. Login to [LMS](https://lms.znu.ac.ir/login/index.php) and copy your session
![IMG](https://github.com/ribrea/znu-html-adobe-connect-class/blob/master/static/image/3.png?raw=true)
#### 2. Find your course id and copy it
##### go to one course
![IMG](https://github.com/ribrea/znu-html-adobe-connect-class/blob/master/static/image/1.png?raw=true)
##### Copy your course id
![IMG](https://github.com/ribrea/znu-html-adobe-connect-class/blob/master/static/image/2.png?raw=true)
#### Run cli.py and give needed arguments

# Usage
#### 1. Run cli.py with arguments
```bash
python cli.py 
session
course_id[s] splited by comma
```
#### 2. Or create .env file and add needed arguments
```.env
CLASS_IDSs='17825, 17623, 17806'
COOKIE='Session'
```
