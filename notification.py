from flask import Flask, render_template, redirect, url_for
import pandas as pd
from datetime import datetime
from twilio.rest import Client

app = Flask(__name__)

account_sid = 'AC1b4a58dac5c5cc2246a0adf6b6a40843'
auth_token = 'aeeecf34b42fa503f2a9399352c666b8'
client = Client(account_sid, auth_token)


df = pd.read_csv('your_dataset.csv', encoding='UTF-8', quotechar="'")


def get_current_month():
    return datetime.now().strftime('%B')


def get_min_relative_humidity():
    current_month = get_current_month()
    filtered_df = df[df['Month'] == current_month]
    if filtered_df.empty:
        print(f"No data found for {current_month}.")
        return None
    else:
        min_relative_humidity = filtered_df['Min_RH'].values[0]
        return min_relative_humidity


def get_max_relative_humidity():
    current_month = get_current_month()
    filtered_df = df[df['Month'] == current_month]
    if filtered_df.empty:
        print(f"No data found for {current_month}.")
        return None
    else:
        max_relative_humidity = filtered_df['Max_RH'].values[0]
        return max_relative_humidity


def send_notification(message):
    client.messages.create(
        to='+918220608349',
        from_='+16562210522',
        body=message)

def send_sms_alert():

    min_rh_current_month = get_min_relative_humidity()
    max_rh_current_month = get_max_relative_humidity()


    if min_rh_current_month is None or max_rh_current_month is None:
        return "No data found for the current month."


    current_humidity = 10 

    low_threshold = 30


    if current_humidity < low_threshold:
        message = f'Alert! Low humidity detected for {get_current_month()}. Current humidity is {current_humidity}%.'

    elif min_rh_current_month <= current_humidity <= max_rh_current_month:
        message = f'Current humidity for {get_current_month()} is {current_humidity}%, which is within the normal range.'

    else:
        message = f'Alert! High humidity detected for {get_current_month()}. Current humidity is {current_humidity}%, which exceeds the maximum of {max_rh_current_month}%.'
    
    # Send the notification
    print("Sending SMS:", message)
    send_notification(message)
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_alert', methods=['POST'])
def send_alert():
    result_message = send_sms_alert()
    return render_template('result.html', message=result_message)

if __name__ == "__main__":
    app.run(debug=True)