from flask import Flask, url_for, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message_body"]
#         database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csv_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message_body"]
        csv_writer = csv.writer(
            csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name='index.html'):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'something went wrong'
