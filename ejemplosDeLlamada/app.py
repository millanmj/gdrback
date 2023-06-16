import base64
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/jira-auth', methods=['POST'])
def jira_auth_endpoint():
    googleAuth = request.json

    try:
        jira_user_token = authenticate_with_jira(googleAuth)

        return jsonify({'jira_user_token': jira_user_token})

    except requests.exceptions.RequestException as e:
        print(str(e))
        return jsonify({'error': f'Error de autenticación con Jira: {str(e)}'}), 400



def authenticate_with_jira(googleAuth):

    client_id = googleAuth["client_id"]

    return client_id

    #implementacion de auth



if __name__ == '__main__':
    app.run(debug=True)