from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask
app=Flask(__name__)

#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#sqlalchemy 초기화
db=SQLAlchemy(app)

#migrate 초기화
migrate=Migrate(app, db)

#table 만들기
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)
    memo=db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
        
        
# [Create]
# INSERT INTO users (username, email) VALUES ('gvg4991','14.73oo6o19@gmail.com')
# user=User(username='gvg4991',email='14.73oo6o19@gmail.com')
# db.session.add(user)
# db.session.commit()
# User.query.all()  (user의 id값을 가지고옴)

# [Read]
# SELECT * FROM users;
# users = User.query.all() #복수

# SELECT * FROM users WHERE username='gvg4991';
# users = User.query.filter_by(username='gvg4991').all()

# SELECT * FROM users WHERE username='gvg4991' LIMIT 1;
# user = User.query.filter_by(username='gvg4991').first()

# SELECT * FROM users WHERE id=2 LIMIT 1;
# user = User.query.get(2)
# primary key만 get으로 가져올 수 있음.

# SELECT * FROM users WHERE email LIKE '%water%';
# users = User.query.filter(User.email.like("%water%")).all()

# ORDER
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()

# ORDER + LIMIT + OFFSET
# users = User.query.order_by(User.username).limit(1).offset(2).all()

# [DELETE]
# DELETE FROM users WHERE id=1;
# user = User.query.get(1)  (제거시킬 데이터 번호를 입력: 1)
# db.session.delete(user)
# db.session.commit()

# [UPDATE]
# UPDATE users SET username='yo' WHERE id=2;
# user = username = 'yo'
# db.session.commit()