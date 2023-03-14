from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    tls = [db_sess.query(User).filter(User.id == j.team_leader).first() for j in db_sess.query(Jobs)]
    return render_template("index.html", jobs=db_sess.query(Jobs), tls=tls)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

    u1 = User()
    u1.surname, u1.name, u1.age, u1.position, u1.speciality = 'Qwerty', 'Uiop', 22, 'colonist', 'doctor'
    u1.address, u1.email = 'module_1', 'qwertyuiop@mars.org'
    u2 = User()
    u2.surname, u2.name, u2.age, u2.position, u2.speciality = 'Poiuy', 'Trewq', 42, 'colonist', 'biologist'
    u2.address, u2.email = 'module_2', 'poiuytrewq@mars.org'
    u3 = User()
    u3.surname, u3.name, u3.age, u3.position, u3.speciality = 'Kodeforsov', 'Polycarp', 24, 'colonist', 'pilot'
    u3.address, u3.email = 'module_2', 'polycarp@mars.org'

    job1 = Jobs()
    job1.team_leader, job1.job = 1, "Deployment of residential modules 1 and 2"
    job1.work_size, job1.collaborators, job1.is_finished = 15, "2, 3", False

    job2 = Jobs()
    job2.team_leader, job2.job = 4, "Exploration of mineral resources"
    job2.work_size, job2.collaborators, job2.is_finished = 15, "1, 2", False

    db_sess = db_session.create_session()
    db_sess.add(user), db_sess.add(u1), db_sess.add(u2), db_sess.add(u3)
    db_sess.add(job1), db_sess.add(job2)
    db_sess.commit()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='127.0.0.1')