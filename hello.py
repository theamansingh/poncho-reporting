from flask import Flask, render_template, request, url_for

import os
import json
import requests
TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
# user_access = False


@app.route('/index')
def index():
    return render_template('index.html')


# @app.route('/validation', methods=['POST', 'GET'])
# def login_validation():
#     email = request.form.get('email')
#     password = request.form.get('password')

#     if email == 'admin@box8.in' and password == 'box8@123':
#         return render_template('reporting.html')
#     else:
#         return render_template('index.html')


@app.route('/reporting')
def reporting():
    crm_data = requests.get(
        'https://be.redash.box8.co.in/api/queries/14990/results.json?api_key=ZRsL4loL2WPJfUH3Ep5QvZW2AzkT29Vi7FRJNbZ3')
    crm_data = json.loads(crm_data.text)['query_result']['data']['rows']

    crm_data_1 = requests.get(
        'https://be.redash.box8.co.in/api/queries/14996/results.json?api_key=em5Y2v5Tm033s9hj97QI6U6yXrWDYZL8R340uI9c')
    crm_data_1 = json.loads(crm_data_1.text)[
        'query_result']['data']['rows']
    return render_template('reporting.html', crm_data=crm_data, crm_data_1=crm_data_1)


if __name__ == "__main__":
    app.run(debug=True)
