from flask import Flask, render_template, request
import psycopg2
import datetime

date = datetime.datetime.today()

month_dict = {'December': 'Декабрь', 'January': 'Январь', 'February': 'Февраль', 'March': 'Март', 'April': 'Апрель',
              'May': 'Май', 'June': 'Июнь', 'Jule': 'Июль', 'August': 'Август', 'September': 'Сентябрь',
              'October': 'Октябрь', 'November': 'Ноябрь'}

date_ru = month_dict.get(date.strftime('%B'))

connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="200699",
    host="localhost",
    port="5432"
)

connection.autocommit = True
cursor = connection.cursor()


app = Flask(__name__)


@app.route('/baza')
def baza():
    cursor.execute("SELECT * FROM Сентябрь")
    rows = cursor.fetchall()
    return render_template('baza.html', rows=rows)


@app.route('/', methods=['post', 'get'])
@app.route('/home', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        # первое поле
        if request.form.get('name'):
            field_name = request.form.get('name')
            field_category = request.form.get('row')
            field_price = request.form.get('price')
            field_comment = request.form.get('comment')

            cursor.execute(f"INSERT INTO Сентябрь(name, category, sum, comment)"
                           f"VALUES ('{field_name}', '{field_category}', {field_price}, '{field_comment}')")
        # второе поле
        if request.form.get('name_1'):
            field_name_1 = request.form.get('name_1')
            field_category_1 = request.form.get('row_1')
            field_price_1 = request.form.get('price_1')
            field_comment_1 = request.form.get('comment_1')

            cursor.execute(f"INSERT INTO Сентябрь(name, category, sum, comment)"
                           f"VALUES ('{field_name_1}', '{field_category_1}', {field_price_1}, '{field_comment_1}')")
        # третье пол
        if request.form.get('name_2'):
            field_name_2 = request.form.get('name_2')
            field_category_2 = request.form.get('row_2')
            field_price_2 = request.form.get('price_2')
            field_comment_2 = request.form.get('comment_2')

            cursor.execute(f"INSERT INTO Сентябрь(name, category, sum, comment)"
                           f"VALUES ('{field_name_2}', '{field_category_2}', {field_price_2}, '{field_comment_2}')")

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
