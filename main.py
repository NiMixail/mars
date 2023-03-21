from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs

# from flask_login import login_user
# from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    tls = [db_sess.query(User).filter(User.id == j.team_leader).first() for j in db_sess.query(Jobs)]
    return render_template("index.html", jobs=db_sess.query(Jobs), tls=tls)


'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)
'''


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='127.0.0.1')
