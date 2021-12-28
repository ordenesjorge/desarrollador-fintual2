class Portfolio:

    def __init__(self):
        self.stock_collection = []

    def profit(self, date_i, date_f):
        profit = 0
        for s in self.stock_collection:
            date_i_aux = date_i
            if date_i < s['date']:
                date_i_aux = s['date']
            if date_f > s['date']:
                profit += s['stock'].price(date_f) - s['stock'].price(date_i_aux)
        return profit

    def add_stock(self, stock, number, date):
    
        if date >= stock.release_date:
            self.stock_collection.append(
                {'stock': stock,
                 'number':number,
                 'date':date}
            )
        else:
            print('date must be equal or greater than stock release date.')
