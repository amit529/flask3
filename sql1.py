from flask import Flask,request,flash,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Expenses.sqlite3'

db=SQLALchemy(app)

class Expenses(db.Model):
     name=db.column(db.string(50))
     salary=db.column(db.string(50))
     house_rent =db.column(db.string(50))
     travel_charges=db.column(db.string(50))
     food  =db.column(db.string(50))
def __init__(self,Name,salary,house_rent,travel_charges,food):
    self.name= name
    self.salary=salary
    self.house_rent=house_rent
    self.travel_charges=travel_charges
    self.food=food

@app.route('/')
def details():
   return render_template('details.html',Expenses=Expenses.query.all())
@app.route('/data',methods=['GET','POST'])
def data():
   if request.method=='POST':
      if not  request.form['name'] or not request.form['salary'] :
          flash("please enter the name and salary")
      else:
           person=Expenses(request.form['name'],request.form['salary'],request.form['house_rent'],
              request.form['travel_charges'],request.form['food'])
           db.session.add(person)
           db.session.commit()
           flash("data is entered successfully")
           return redirect(url_for('details'))
    return render_template('saved.html')
@app.route('/savings/<float:savings>',methods=['GET','POST'])
def my_savings(savings):
    if request.method=='GET':
       if request.form['salary']>0:
          savings=Expenses(request.form['salary'])-Expenses(request.form['house_rent']+request.form            ['travel_charges']+request.form['food'])
    return "my savings %f ' % savings

if __name__=='__main__':
   db.create_all()
   app.run(debug=run)

