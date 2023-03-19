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

if __name__ == '__main__':
    app.run()