from flask import Flask, request, render_template
from osnova import create_file

app = Flask(__name__)


@app.route("/result", methods=['POST'])
def result():
    name = request.form['fsname']
    data = request.form['calendar']
    yes = request.form['yes']
    return  render_template("result.html", the_title='ок', rname=name), create_file(name, data, yes),


@app.route("/",)
def entry():
    return render_template("form.html", the_title='проба')


if __name__ == "__main__":
    app.run(debug=True)