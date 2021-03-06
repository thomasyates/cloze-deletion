# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
    url_for, request, session, flash
from functools import wraps
import cloze

# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'


@app.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        message = request.form['question']

	noun = bool(request.form.getlist('noun'))
	verb = bool(request.form.getlist('verb'))
	adjective = bool(request.form.getlist('adjective'))
	adverb = bool(request.form.getlist('adverb'))

	stop = bool(request.form.getlist('stopwords'))

	output = cloze.question_stop(message, stop, noun, verb, adjective, adverb)
	return render_template('login.html', message = output)
	

    return render_template('login.html')
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
