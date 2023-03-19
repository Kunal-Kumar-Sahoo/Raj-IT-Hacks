from flask import Flask, request, redirect
import sql_queries.queries as queries


app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    queries.create_new_user(request_data)
    return request_data

@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    passwd_json = queries.sign_in(request_data)
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
    


if __name__ == '__main__':
    app.run()