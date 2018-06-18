from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  r = requests.get('http://httpbin.org/status/418')
  print(r.text)
  return HttpResponse('<pre>' + r.text + '</pre>')
#  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
