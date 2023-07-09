from flask import Flask, request, render_template
from model import db, Users
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

DATABASE = {
    'drivername': 'sqlite',
    'database': 'database.db'
}

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get-cfp", methods=["POST"])
def get_cfp():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        paper_title = request.form.get("paper_title")
        paper_category = request.form.get("paper_category")
        paper_summary = request.form.get("paper_summary")

        id = random.randint(1, 1999)

        log = Users(id=id, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                    paper_title=paper_title, paper_summary=paper_summary, paper_category=paper_category)
        db.session.add(log)
        db.session.commit()

        return "THANK YOU FOR SUBMITTING :)"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
