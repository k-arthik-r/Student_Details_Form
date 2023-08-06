from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://karthik:admin1234@data.kv0kadm.mongodb.net/?retryWrites=true&w=majority")
db = client["student_db"]
collection = db["student"]

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
        # Assuming you have a collection named 'students' in your MongoDB database

        # Check if the student with the given USN already exists
        existing_student = collection.find_one({'_id': usn})

        if existing_student:
            # If the student already exists, update their information
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
            # If the student does not exist, insert a new document
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
