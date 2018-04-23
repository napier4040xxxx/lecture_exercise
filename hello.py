from flask import Flask , render_template 
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	user = {'name': name} 
	return render_template('hello.html', user=user)

@app.route('/users/')
def users():
	names=['simon','thomas','lee','jamie','sylvester']
	return render_template('hello.html', names=names)

if __name__ == "__main__": 
	app.run(host='0.0.0.0', debug=True)