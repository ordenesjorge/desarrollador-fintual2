import numpy as np

class Portfolio:

    def __init__(self):
        self.stock_collection = []

    # dates mus be datetime64, if initial date is lower than stock purchase date, the latter is used instead for that stock profit.
    def profit(self, date_i, date_f):
        profit = 0
        for s in self.stock_collection:
            date_i_aux = date_i
            if date_i < s['date']:
                date_i_aux = s['date']
            if date_f > s['date']:
                profit += (s['stock'].price(date_f) - s['stock'].price(date_i_aux))*s['number']
        profit = round(profit)
        return profit

    # this annualized return uses number of days. 
    # It can be negative even if profit is positive since it takes the profit into the total of years even if a stock was pruchased after
    def annualized_return(self, date_i, date_f):
        initial_invesment = 0
        actual_value = 0
        for s in self.stock_collection:
            date_i_aux = date_i
            if date_i < s['date']:
                date_i_aux = s['date']
            if date_f > s['date']:
                initial_invesment = s['stock'].price(date_i_aux)*s['number']
                actual_value = s['stock'].price(date_f)*s['number']

        if initial_invesment == 0:
            return 0
        delta_dates = date_f - date_i
        n_days = delta_dates.astype('timedelta64[D]')
        n_days = n_days / np.timedelta64(1, 'D')
        a_return = (((actual_value-initial_invesment)/initial_invesment)**(365/n_days))-1
        a_return = round(a_return,2)
        return a_return

    # adds a stock object with a number of stocks and a date of purchase as a dict in a list
    def add_stock(self, stock, number, date):
    
        if date >= stock.release_date:
            self.stock_collection.append(
                {'stock': stock,
                 'number':number,
                 'date':date}
            )
        else:
            print('date must be equal or greater than stock release date.')