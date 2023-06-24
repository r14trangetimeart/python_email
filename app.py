from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    print("request", request)
    data = request.get_json()
    print(data)
    sender_email = 'amirry002@gmail.com'
    receiver_email = 'sohailbadghisi1@gmail.com'
    subject = "New user registered"
    message = data['message']
    password = 'uxyikxxuikdjcjdn'
    
    try:
        # SMTP server settings
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Create the email message
        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = receiver_email
        email['Subject'] = subject
        message_json = json.dumps(message)
        email.attach(MIMEText(message_json, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, password)  # Login to the server
            server.send_message(email)  # Send the email

        return "Email sent successfully!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run()
