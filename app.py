from flask import Flask, render_template, request
from configparser import ConfigParser
import pymongo

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini')

client = pymongo.MongoClient(config['connection']['connection_string'])
db = client[config['database']['db_name']]
collection = db[config['database']['collection_name']]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_student', methods=['POST'])
def save_student():
    name = request.form.get('name')
    usn = request.form.get('usn')
    grade = request.form.get('grade')
    linkedin = request.form.get('linkedin')
    github = request.form.get('github')


    if name and usn and grade:

        existing_student = collection.find_one({'_id': usn})

        if existing_student:
            collection.update_one(
                {'_id': usn},
                {
                    '$set': {
                        'name': name,
                        'grade': grade,
                        'linkedin': linkedin,
                        'github': github
                    }
                }
            )
            message = "Data updated successfully."
        else:
            student_data = {
                '_id': usn,
                'name': name,
                'grade': grade,
                'linkedin':linkedin,
                'github': github
            }
            collection.insert_one(student_data)
            message = "Data logged successfully."

        return render_template('index.html', message=message, success=True)
    else:
        return render_template('index.html', message="Something went wrong.", success=False)


if __name__ == '__main__':
    app.run(debug=True)
