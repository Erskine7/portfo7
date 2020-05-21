# Make sure to not call any file flask.py because
# this would conflict with Flask itself.

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# The above code, 14 - 16, replaced all repetitious code below. ALSO Contact info bottom of page.<<

# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# End of what code 14 - 16 replaced <<<<<<<<<<<<<<<<<<<<<<


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['Email']  # 30 min lost because i did't have capital 'E'
#         subject = data['Subject']
#         message = data['Message']
#         file = database.write(f'\n{email}, {subject}, {message}')


# Creating CSV to data base replaces above code.

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['Email']  # 30 min lost because i did't have capital 'E'
        subject = data['Subject']
        message = data['Message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'Something went wrong. Please try again.'

