from flask import Flask, render_template, request, redirect, flash
import db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Для использования flash-сообщений

# Инициализация базы данных при запуске приложения
db.create_table()

@app.route('/')
def index():
    """Отображение списка клиентов."""
    try:
        clients = db.get_all_clients()
    except Exception as e:
        flash(f"Ошибка при получении клиентов: {e}", 'error')
        clients = []
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET', 'POST'])
def add_client():
    """Добавление нового клиента."""
    if request.method == 'POST':
        # Получаем данные из формы
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        patronymic = request.form['patronymic']
        passport_data = request.form['passport_data']
        phone_number = request.form['phone_number']
        birth_date = request.form['birth_date']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        
        # Валидация данных (можно улучшить в зависимости от требований)
        if not first_name or not last_name or not passport_data:
            flash("Заполните обязательные поля: Имя, Фамилия, Паспортные данные.", 'error')
            return render_template('add_client.html')

        try:
            # Добавляем клиента в базу данных
            db.add_client(first_name, last_name, patronymic, passport_data, phone_number, birth_date, check_in_date, check_out_date)
            flash("Клиент успешно добавлен!", 'success')
            return redirect('/')
        except Exception as e:
            flash(f"Ошибка при добавлении клиента: {e}", 'error')

    return render_template('add_client.html')

if __name__ == '__main__':
    app.run(debug=True)
