from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars = {}

@app.route('/', methods = ['GET', 'POST'])
def index():
  default_stock = 'GOOG'
  if request.method == 'GET':
    return render_template('stockinfo.html', stock_id = default_stock)
  else:
  	# request was a POST
  	app.vars['stock'] = request.form['stock_id']

  	f = open('%s.txt'%(app.vars['stock']), 'w')
  	f.write('Stock: %s\n'%(app.vars['stock']))
  	f.close()

  	return render_template('figure.html', stock_id = default_stock)

@app.route('/figure')
def figure():
  #app.stock_dat = https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOG&interval=1min&apikey=M388VQYSPCRW5TYU

	return render_template('figure.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
