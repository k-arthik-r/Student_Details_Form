<div align="center">
<h1>Student Details Form</h1>
</div>
  
------------------------

<div align="center">
  <a><img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/MongoDB_Atlas-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white"></a> &nbsp;
</div>

------------------------

The Student Details Form site built to take the data like Name, USN (University Seat Number), Grade, Linked-in Profile Name, Github Profile Name and store it in the Mongo DB Atlas Cloud. Its Hosted Under Azure Web
Service.

------------------------

## Requirments
Python 3.11.1 (Recommended) 

<a href="https://www.python.org/downloads/" alt="3.11.1">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
  
<h4>Modules Required</h4>

- flask
- pymongo
- configparser

--------------------------
## How to Run?

- Intialize a Git Repository.
```bash
  git init
```

- Clone the Current Git Repository.
  
```bash
  git clone https://github.com/k-arthik-r/https://github.com/k-arthik-r/Student_Details_Form.git
```

- Crete a Virtual Environment named env and Activate it(PowerShell)
  
```bash
  python -m venv env

  .\env\Scripts\Activate.ps1
```

- Install all the Modules Present in [requirements](requirements.txt)
  
```bash
  pip install -r requirements.txt
```

- Give The Appropriate Mongo DB Credentials in [config](config.ini)

- After Importing all the mentioned modules, Run [app](app.py)
  
```bash
  python app.py
```

-------------------------

## How the Website Works?

Ithe Webpage will take Data Like Name, USN, Grade, Linked IN Profile, Github Profile and Stres it in Mongo DB Atlas. If the USN is Alreday Present then it will Just Updates the Data for that USN. USN is used as _id here. 

![Doc2](https://github.com/k-arthik-r/Student_Details_Form/assets/111432615/5578ea60-2f50-4538-9a68-0b0431f66b17)

----------------------------

## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

----------------------------

## Feedback
If you have any feedback, please reach out to us at voidex.developer@gmail.com .
You are also welcomed to add new features by creating Pull Requests.


