import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open ('database.txt', mode="a", encoding="utf8") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f'\n{name}, {email}, {message} ')

def write_to_csv(data):
    with open ('database.csv', newline='', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email ,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html') #make new page here, copied from form page
        except:
            return 'did not save to database'
    else:
        return 'somethings fucky'

@app.route('/subaru')
def subaru():
    return 'Subaru  ha ha ha'

"""
these 2 lower commands MUST be typed into the terminal in order to execute 127.0.0.1

$env:FLASK_APP = "server.py"

flask run

OR

flask run --debug

(for live changes)

"""