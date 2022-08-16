"""
Routes and views for the flask application.
"""

from resource import *
import time, random, requests, os, sqlite3, shutil, psutil, numpy as np, json
import screen_brightness_control as sbc

app.title = "Barmajino App"
app.icon = ".\\resource\\static\\img\\server.ico"
app.start_page = '/home'

conn_db = sqlite3.connect(".\\resource\\database\\table.db", check_same_thread=False)
cursor_db = conn_db.cursor()

conn_db.execute('''CREATE  TABLE IF NOT EXISTS users
                    (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    First_name varchar(255) NOT NULL,
                    Last_name varchar(255) NOT NULL,
                    Username varchar(20) NOT NULL,
                    Email  varchar(255) NOT NULL);''')


curent_page = None
def data_updating():

    while True:
        global curent_page
        if(curent_page == 'dashboard'):

            cpu_percent = psutil.cpu_percent()
            socketio.emit('cpu_percent', f'{cpu_percent}%')

            virtual_memory = dict(psutil.virtual_memory()._asdict())
            socketio.emit('virtual_memory', f"{virtual_memory['percent']}%")
            try:
                current_brightness = sbc.get_brightness()
            except:
                current_brightness = 'N/A'
            socketio.emit('current_brightness', f"{current_brightness}%")

            battery = psutil.sensors_battery()
            socketio.emit('battery_percent', f"{battery.percent}%")

            ##########################################################
            Tasks = random.randint(0,100)
            socketio.emit('Tasks', f'{Tasks}%')

            earnings_annual = random.randint(2000,9000)
            socketio.emit('earnings_annual', f'${earnings_annual}')

            earnings_monthly = random.randint(100,1500)
            socketio.emit('earnings_monthly', f'${earnings_monthly}')

            pending_requests = random.randint(0,50)
            socketio.emit('pending_requests', f'{pending_requests}')

        
            time.sleep(1)
        elif(curent_page == 'table'):
            # this part created to exicute any code for the table page.
            pass

dashboard = Thread(target=data_updating, daemon=True)

########################################
################ @app ##################
########################################




@app.route('/home', methods=['GET', 'POST'])
def home():
    global curent_page
    curent_page = 'dashboard'
    """Renders the home page."""
    return render_template_string_from_json('index.html')


@app.route('/table', methods=['GET'])
def table():
    sql_query = "SELECT * FROM users;"
    cursor_db.execute(sql_query)
    return render_template_string_from_json('table.html', user_table_data=cursor_db.fetchall())
    #return render_template('table.html', user_table_data=cursor_db.fetchall())

########################################
############# @socketio ################
########################################

@socketio.on('connect')
def on_connect():
    try:
        dashboard.start()
    except:
        pass

@socketio.on('page_update')
def page_update(data):
    global curent_page
    curent_page = data

@socketio.on('add_user_data')
def add_user_data(data):
    #print(message)
    conn_db.execute(f"INSERT INTO users (First_name,Last_name,Username,Email) VALUES {tuple(data)}");
    conn_db.commit()

    sql_query = "select Id from users where id=(select max(Id) from users)"
    data_ = {
    "title" : [column[0] for column in cursor_db.execute(sql_query).description],
    "body" : cursor_db.fetchall()
    }
    last_id = data_['body'][0][0]

    emit('add_user_to_table', [last_id,data])

@socketio.on('update_user_data')
def add_user_data(data):
    #print(message)
    conn_db.execute(f"UPDATE users SET First_name = '{data[1]}',\
   Last_name = '{data[2]}', Username = '{data[3]}', Email = '{data[4]}' WHERE Id='{data[0]}'");
    conn_db.commit()

    emit('update_user_data_done', data)

@socketio.on('delete_user_data')
def delete_user_data(data):
    #print(message)
    conn_db.execute(f"DELETE FROM users WHERE Id =='{data}'");
    conn_db.commit()

    emit('delete_user_data_done', data)