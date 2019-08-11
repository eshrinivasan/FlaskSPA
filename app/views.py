from flask import jsonify, render_template, request

from app import app
from pandas import read_excel
import sys
import requests 

def symbolsearcher(company):
    file_name = "COMPANIES_LISTEDIN_NSE_EQUITY_L.xlsx"
    col_name = "NAME OF COMPANY"
    outcol_name = "SYMBOL"
    wanted_col=[0,1]
    try:
        df = read_excel(file_name, sheet_name=0, skipinitialspace=True, usecols=wanted_col)
        df1 = df[df[col_name].str.contains(company, na=False, case=False)]
        print(df1)
        return df1.iloc[0][outcol_name]
    except IndexError:
        print("NA")

@app.route('/', defaults={'js': 'plain'})
@app.route('/<any(plain, jquery, fetch):js>')
def index(js):
    return render_template('{0}.html'.format(js), js=js)


@app.route('/add', methods=['POST'])
def add():
    company = request.form['text']
    result = symbolsearcher(company)
    print(result)
    return result