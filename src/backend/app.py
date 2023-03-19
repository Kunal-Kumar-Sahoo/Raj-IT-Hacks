from flask import Flask

app = Flask(__name__)


<<<<<<< Updated upstream
@app.route('/')
def index() -> None:
    return 'Raj IT Hacks 2.0'
=======
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


>>>>>>> Stashed changes

if __name__ == '__main__':
    app.run()