from flask import Flask, request, jsonify, render_template
from portfolio import Portfolio
from stock import Stock
import pandas as pd
import numpy as np
import datetime
import pickle

app = Flask(__name__)

# read data of stocks
data = pd.read_csv('data.csv', parse_dates=['date'])

# create stock objects
stocks = {}
for name in data['name'].unique():
    stocks[name] = Stock(name, data[data['name'] == name].copy())

# save stock objet to open when needed, this is used to avoid using a database.
with open('portfolio_data', 'wb') as f:
    pickle.dump(Portfolio(), f, pickle.HIGHEST_PROTOCOL)

# home
@app.route('/')
def home():
    return render_template('index.html')

# addstock
@app.route('/addstock',methods=['POST'])
def addstock():

    # get input values
    features = [x for x in request.form.values()]

    # check for data types
    try:
        datetime.datetime.strptime(features[2], '%Y-%m-%d')
    except:
        return render_template('index.html', addstock_text='Incorrect date string format, it should be yyyy-mm-dd.')
    if features[0] not in data['name'].unique():
        return render_template('index.html', addstock_text='Stock name not in database.')
    if not features[1].isnumeric():
        return render_template('index.html', addstock_text='Number of stocks must be a numeric value.')
    
    date = np.datetime64(features[2])

    if stocks[features[0]].price(date) == None:
        return render_template('index.html', addstock_text='Stock did not exist on selected date.')

    # open portfolio object
    with open('portfolio_data', 'rb') as f:
        p = pickle.load(f)

    # add stock to portfolio p
    p.add_stock(
        stocks[features[0]],
        float(features[1]),
        date
    )

    # overwrite portfolio
    with open('portfolio_data', 'wb') as f:
        pickle.dump(p, f, pickle.HIGHEST_PROTOCOL)

    # render results
    return render_template('index.html', addstock_text='Added stocks from {}'.format(features[0]))

# getprofit
@app.route('/getprofit',methods=['POST'])
def getprofit():

    # get input values
    features = [x for x in request.form.values()]

    # check for data types
    try:
        datetime.datetime.strptime(features[0], '%Y-%m-%d')
    except:
        return render_template('index.html', getprofit_text='Incorrect initial date string format, it should be yyyy-mm-dd.')

    try:
        datetime.datetime.strptime(features[1], '%Y-%m-%d')
    except:
        return render_template('index.html', getprofit_text='Incorrect final date string format, it should be yyyy-mm-dd.')

    initial_date = np.datetime64(features[0])
    final_date = np.datetime64(features[1])

    # check if dates make sense
    if initial_date >= final_date:
        return render_template('index.html', getprofit_text='Initial date must be lower than final date.')

    # open portfolio object
    with open('portfolio_data', 'rb') as f:
        p = pickle.load(f)

    # give result depending of button used
    if request.form["profit"] == "getprofit":
        output = p.profit(initial_date, final_date)
        return render_template('index.html', getprofit_text='Your profit is ${}'.format(output))
    elif request.form["profit"] == "getanualprofit":
        output = p.annualized_return(initial_date, final_date)
        return render_template('index.html', getprofit_text='Your annualized return is {}%'.format(output))
    
if __name__ == "__main__":
    app.run(debug=True)