from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gabor'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Bristol!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


# Tell Flask that this view function accepts GET and POST requests,
# overriding the default, which is to accept only GET requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # When the browser sends the GET request to receive the web page with the form,
    # form.validate_on_submit() method is going to return False.
    #
    # When the browser sends the POST request as a result of the user pressing the submit button,
    # form.validate_on_submit() is going to gather all the data,
    # run all the validators attached to fields,
    # and if everything is all right it will return True
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
