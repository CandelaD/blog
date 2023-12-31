from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from forms import SignupForm, PostForm, LoginForm
from flask_login import LoginManager
from models import get_user, users
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2ed4fa9067c9a1db295e2c7c7bdd6f31'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blog'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return ('index.html')

@app.route('/post/new', methods=['GET', 'POST'])
#@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.title.data,
            author=current_user
        )
        db.session.add(post) 
        db.session.commit()
        flash('post created')
    return render_template('new_post.html', form=form)

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

login_manager = LoginManager(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('you already logged in')
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user and bcrypt.check_password_hash(user.possword, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            flash('you loggeg in successfully')
            return redirect(next_page if next_page else url_for(index))
        else:
            flash('email or password is wrong', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

