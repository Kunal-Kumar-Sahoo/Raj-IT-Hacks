from flask import Flask, request, redirect
import sql_queries.queries as queries
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app)

@app.route('/registerStartup', methods=['POST'])
def signup_startup():
    request_data = request.get_json()
    queries.create_new_user(request_data, 's')
    return request_data

@app.route('/registerPeople', methods=['POST'])
def signup_person():
    request_data = request.get_json()
    queries.create_new_user(request_data, 'p')
    return request_data

@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    passwd_json = queries.get_password(request_data)
    return {
        "authenticated": passwd_json['password'] == request_data['password'],
        "role": queries.get_role(request_data['email']) if passwd_json['password'] == request_data['password'] else -1
    }

@app.route('/pool_investment', methods=['POST'])
def pool_investment():
    request_data = request.get_json()
    email_id = request_data['email']
    balance = queries.get_balance(email_id)
    investment_amount = request_data['investment_amount']
    print(type(investment_amount))
    try:
        if(balance > investment_amount):
            queries.update_pool_investment(email_id, investment_amount)
            print(f'Transaction successful')
        else:
            print('Insufficient funds')
    except Exception as e:
        print(e)
    return {
        'email': email_id, 'balance': queries.get_balance(email_id), 'pool_investment': queries.get_invested_amount(email_id)
    }


@app.route('/pool_returns', methods=['POST'])
def pool_returns():
    request_data = request.get_json()
    email_id = request_data['email']
    no_of_days = request_data['no_of_days']
    invested_amount = queries.get_invested_amount(email_id)
    invested_amount = invested_amount if invested_amount > 0 else 0
    balance = queries.get_balance(email_id)
    queries.update_balance(email_id, balance + invested_amount + invested_amount * no_of_days / 2)
    queries.update_pool_investment(email_id, -invested_amount)

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    email_id = request_data['email']
    funding = queries.get_predicted_amount(email_id)
    print({'email': email_id, 'returns': funding/4 if funding > 0 else 0})
    return {'email': email_id, 'returns': funding/4 if funding > 0 else 0}


@app.route('/submit_problem', methods=['POST'])
def submit_problem():
    '''
    :json_param:
    {
        "problem": problem_desc,
        "location": problem_loc
    }
    '''
    request_data = request.get_json()
    problem_description = request_data['problem']
    problem_location = request_data['location']
    queries.write_problem(problem_description, problem_location)


@app.route('/premium_to_insurance', methods=['POST', 'GET'])
def pay_premium():
    request_data = request.get_json()
    email_id= request_data['email']
    funding, valuation, revenue = queries.get_monetary_details(email_id)
    
    roi = (valuation - revenue) / valuation
    
    premium_percent = 100

    if roi == -1:
        premium_percent = 20
    elif roi > -1 and roi <= -.90:
        premium_percent = 19
    elif roi > -0.90 and roi <= -0.80:
        premium_percent = 18
    elif roi > -0.80 and roi <= -0.70:
        premium_percent = 17
    elif roi > -0.70 and roi <= -0.60:
        premium_percent = 16
    elif roi > -0.6 and roi <= -0.5:
        premium_percent = 15
    elif roi> -0.50 and roi<=-0.40:
        premium_percent = 14
    elif roi> -0.40 and roi<=-0.0:
        premium_percent = 13
    elif roi > -0.30 and roi<=-020:
        premium_percent = 12
    elif roi> -0.20 and roi<=-.10:
        premium_percent = 11
    elif roi > -0.10 and roi<=0.0:
        premium_percent = 10
    elif roi >0 and roi<=0.10:
       premium_percent = 9
    elif roi > 0.10 and roi<=0.20
        premium_percent = 8
    elif roi >0.20 and roi<=0.20:
        premium_percent = 7
    elif roi >0.30 and roi<=0.40:
        premium_percent = 6
    elif roi >0.40 and roi<=0.50:
        premium_percent = 5   
    elif roi >0.50 and roi<=0.60:
        premium_percent = 4
    elif roi >0.60 and roi<=0.70:
        premium_percent = 3
    elif roi >0.70 and roi<=0.80:
        premium_percent = 2  
    elif roi >0.180 and roi<=0.9:
        premium_percent = 1  
    else:
        premium_percent = 0

    premium = (premium_percent * funding)/100

    return premium


if __name__ == '__main__':
    app.run()