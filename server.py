from flask import Flask, render_template, send_from_directory, request, redirect
import os
import csv


app = Flask(__name__)

@app.route("/")
def Start():
    return render_template('index.html')

@app.route("/<string:page_name>")
def Html_page(page_name):
    return render_template(page_name)

def data_collector_txt(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')


def data_collector_csv(data):
    with open('./database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    request.form == 'POST'
    info = request.form.to_dict()
    data_collector_txt(info)
    data_collector_csv(info)
    return redirect('thankyou.html')


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')





