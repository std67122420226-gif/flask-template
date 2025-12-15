from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', title='My Home Page')

@app.route('/about')
def about():
                        title='About Page',
                        name='thanchanok',
                        email='std.67122420226@ubru.ac.th',
                        phone='080-465-8319'
                        return render_template('about.html',
                                                title=title,
                                                name=name,
                                                email=email,
                                                phone=phone)

@app.route('/favorite/foods')
def fav_foods():
  title = 'favorite Foods Page'
  foods = ['ส้มตำ','ต้มยำกุ้งน้ำข้น','ก๋วยเตี๋ยวต้มยำ','กระเพราหมูกรอบ','หมูกะทะ']
  return render_template('fav_foods.html',
                        foods=foods,
                        title=title)

@app.route('/sports')
def fav_sports():
  title = 'Favorite Sprots Page'
  sports = ['บอลเล่','ปิงปอง','แบดมินตัน','เปตอง']
  return render_template('fav_sports.html',
                        title=title,
                        sports=sports)

@app.route('/greeting/<username>')
def welcome(username):
  title = 'Welcome Page'
  return render_template('welcoome.html',
                        title=title,
                        username=username)