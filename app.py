from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm
from flask_login import LoginManager
from models import get_user, users
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_login import login_required

app = Flask(__name__)

login_manager = LoginManager(app)

<<<<<<< HEAD
posts = []

@app.route("/")
def index():
    return "{} posts".format(len(posts))

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('profile'))
    return render_template('new_post.html', form=form)

=======
>>>>>>> 8f03d37a3354d86f23546bbdb4d2c7319765b9bb
@app.route("/signup/", methods=["GET", "POST"])
def signup_form():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
<<<<<<< HEAD
    return None
=======
    return None
>>>>>>> 8f03d37a3354d86f23546bbdb4d2c7319765b9bb
