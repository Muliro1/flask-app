from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import LoginForm, RegistrationForm, PostForm, AccountForm
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager

import os



app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['SECRET_KEY'] = 'relapse92'


database = {}
post_database = {}
comment_id = len(post_database) + 1
user_id = len(database) + 1



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', database = database)

@app.route('/info')
def info():
	return render_template('about.html', title = 'About page')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		database.update({'username':form.username.data})
		flash('Account created for {}'.format(form.username.data))
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Registration Page', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit() and request.method ==  'POST':
		session['username'], session['email'] == form.username.data, form.email.data
		if form.username.data in database:
			flash('You are now logged in as {}'.format(form.username.data))
			return redirect(url_for('home'))
	return render_template('login.html', title = 'Login Page', form = form)

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('login'))

@login_required
@app.route('/post-comment', methods = ['GET', 'POST'])
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title = form.title.data, content = form.content.data, author = current_user)
		post_database.update({form.content.data})
		flash('Your post has been created', 'success')
		return redirect(url_for('hello'))
	return render_template('createpost.html', title =  'New Post', form = form, legend = 'New Post')

@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
	form =AccountForm()
	if request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
		return render_template('account.html', title =  'Account', form = form)
app.route("/post/<int:post_id>/delete",  methods = [ 'POST'])
@login_required
def delete_post(post_id):
	flash('Your post has been deleted', 'success')
	return redirect(url_for('hello'))




if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug = True)
    
