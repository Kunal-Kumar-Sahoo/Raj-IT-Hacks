import mysql.connector

connection = mysql.connector.connect(
    host='localhost', user='kunal', passwd='6anmol',
    database='RAJITHACKS', auth_plugin='mysql_native_password'
)

cursor = connection.cursor()

def create_new_user(input_json) -> None:
    '''
    :format input_json:
    {
        "email": email_id,
        "password": passwd,
        "role": role
    }
    '''
    email_id = input_json['email_id']
    password = input_json['passwd']
    role = input_json['role'].tolower()[0]
    query = f"INSERT INTO users VALUES('{email_id}', '{password}', '{role}')"
    cursor.execute(query)
    connection.commit()

def sign_in(input_json) -> dict:
    '''
    :format input_json:
    {
        "email": email_id,
        "password": passwd
    }
    '''
    email_id = input_json['email_id']
    query1 = f'SELECT password FROM companies WHERE email_id = "{email_id}"'
    cursor.execute(query1)
    rep = cursor.fetchall()
    for row in rep:
        passwd = row[0]
    return {"password": passwd}

def get_role(email_id) -> str:
    query1 = f'SELECT password FROM companies WHERE email_id = "{email_id}"'
    cursor.execute(query1)
    rep = cursor.fetchall()
    for row in rep:
        passwd = row[0]
    return role
