### Prerequisites
```
Python: 3.x
python-pip
Django
djangorestframework
```
### Steps
```
$ python3 -m venv .venv1
$ git clone https://github.com/deepuranjan/medd-int.git
$ cd medd-int/webapp
$ source .venv1/bin/activate
$ pip install -r requirement.txt
$ cd mywebapp
$ python manage.py runserver
```
### Usage 
Note: postman or any REST client is required 
#### 1. Create Student entry
```
URL: http://localhost:8000/school/students
Method: POST
Payload:
{
	"name": "Deepu Nahak",
	"age": 12,
	"gender": "Male"

}
Respone:
{
    "status": "Added Successfully",
    "roll_no": 59883
} 
```
####2. Search student
```
2. Search student
URL: http://localhost:8000/school/students/23873
Mothod: GET
Respons:
{
    "name": "Deepu Nahak",
    "age": 12,
    "roll_no": 59883,
    "gender": "Male"
}
```
####3. Update student
```
URL: http://localhost:8000/school/students
Method: PUT
Payload:
{
	"name": "Deepu Nahak",
	"age": 19,
	"roll_no": 59883
	"gender": "Male"
}
Response:
{
    "status": "Updated success"
}
```