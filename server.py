from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


# USING FOR LOOP for extracting dict and writing to textfile
def write_to_file(data):
    with open("web_dev/database.txt", mode="a") as database:
        for k, v in data.items():
            database.write(f'{k}: {v}\n')
        database.write("\n")


# USING A DictWirter passing whole dictionary
def write_to_csv(data):
    with open('web_dev/database.csv', 'a', newline="") as database:
        field_names = ["email", "subject", "message"]
        dictwriter_object = csv.DictWriter(
            database, fieldnames=field_names, delimiter=",")
        dictwriter_object.writerow(data)
        database.close()


# USING csv.writer with extracting items from dictionary
def write_to_csv2(data):
    with open("web_dev/database2.csv", mode="a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer = csv.writer(database, delimiter=",",
                            quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong"
