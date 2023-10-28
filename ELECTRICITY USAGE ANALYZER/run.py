import time
from flask import Flask, render_template, request, redirect, url_for, send_file
from Backend.Calculator import CalCulateUnits
import os

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/why-is-saving-power-important')
def Question():
    return render_template('why_is_saving_energy_important.html')



@app.route('/analyzer', methods = ['GET', 'POST'])
def Analyzer():
    if request.method == 'POST':
        Name_of_App = request.form.getlist('nameofapp')
        Watts = request.form.getlist('watts')
        Quantity = request.form.getlist('no')
        Hours = request.form.getlist('hours')

        CalCulateUnits(name = Name_of_App, watts = Watts,
                       quantity = Quantity, hours = Hours)
        print('I am out')

        return redirect(url_for('AnalyzedReportViewer'))

    return render_template('analyzer.html')



@app.route('/report', methods=["GET", "POST"])
def AnalyzedReportViewer():
    return render_template('report.html')


@app.route('/download')
def download_file_csv():
    p1 = 'CalculatedData.csv'
    return send_file(p1, as_attachment=True)

@app.route('/txtdownload')
def download_txt_file():
    p = 'Conclusion.txt'
    return send_file(p, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
