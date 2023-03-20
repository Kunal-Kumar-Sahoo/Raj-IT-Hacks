import mysql.connector

connection = mysql.connector.connect(
    host='localhost', user='root', passwd='6anmol',
    database='RAJITHACKS', auth_plugin='mysql_native_password'
)

cursor = connection.cursor()

def create_new_user(input_json, role_) -> None:
    '''
    :format input_json:
    {
        "email": email_id,
        "password": passwd,
        "role": role,
        "name": name,
    }
    '''
    email_id = input_json['email']
    password = input_json['password']
    role = role_
    name = input_json['name']
    query = f"INSERT INTO users VALUES('{email_id}', '{password}', '{role}')"
    cursor.execute(query)
    connection.commit()

    if role == 's':
        place = input_json['place']
        domain = input_json['domain']
        description = input_json['description']
        funding = input_json['funding']
        valuation = input_json['valuation']
        revenue = input_json['revenue']
        future_plans = input_json['future_plans']
        risk = input_json['risk'].lower()[0]

        query_ = f"INSERT INTO startup(name, place, domain, description, email_id, funding, valuation, revenue, future_plans, risk) VALUES('{name}', '{place}', '{domain}', '{description}', '{email_id}', {funding}, {valuation}, {revenue}, '{future_plans}', '{risk}')"
        cursor.execute(query_)
        connection.commit()
    
    elif role == 'p':
        balance = input_json['balance']

        query_ = f"INSERT INTO people(email_id, name, balance) VALUES('{email_id}', '{name}', {balance})"
        cursor.execute(query_)
        connection.commit()


def get_password(input_json) -> dict:
    '''
    :format input_json:
    {
        "email": email_id,
        "password": passwd
    }
    '''
    email_id = input_json['email']
    query1 = f'SELECT password FROM users WHERE email_id = "{email_id}"'
    cursor.execute(query1)
    rep = cursor.fetchall()
    for row in rep:
        passwd = row[0]
    return {"password": passwd}

def get_role(email_id) -> str:
    query1 = f'SELECT role FROM users WHERE email_id = "{email_id}"'
    cursor.execute(query1)
    rep = cursor.fetchall()
    for row in rep:
        role = row[0]
    return role

def get_balance(email_id):
    query = f'SELECT balance FROM people WHERE email_id="{email_id}"'
    cursor.execute(query)
    balance = cursor.fetchall()
    return balance[0][0]

def update_balance(email_id, amount) -> None:
    query = f'UPDATE people SET balance = {amount} WHERE email_id = "{email_id}"'
    cursor.execute(query)
    connection.commit()

def update_pool_investment(email_id, amount) -> None:
    balance = get_balance(email_id)
    query = f'SELECT pool_investment FROM people WHERE email_id="{email_id}"'
    cursor.execute(query)
    pool_investment = cursor.fetchall()[0][0]
    update_balance(email_id, balance-amount)
    query = f'UPDATE people SET pool_investment = {pool_investment+amount} WHERE email_id = "{email_id}"'
    cursor.execute(query)
    connection.commit()

def get_invested_amount(email_id):
    query = f"SELECT pool_investment FROM people WHERE email_id='{email_id}'"
    cursor.execute(query)
    return cursor.fetchall()[0][0]

def get_predicted_amount(email_id):
    query = f"SELECT funding FROM startup WHERE email_id = '{email_id}'"
    cursor.execute(query)
    funding = cursor.fetchall()[0][0]
    return funding

def write_problem(problem):
    query = f'INSERT INTO problems(problem_description) VALUES ("{problem}")'
    cursor.execute(query)
    connection.commit()

    return 200
    

if __name__ == '__main__':
    # print(get_invested_amount())
    pass
