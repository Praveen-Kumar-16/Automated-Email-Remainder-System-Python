import os
# importing Simple Mail Transfer Protocol library
import smtplib
import json
#Multipurpose internet mail extensions
from email.mime.text import MIMEText 
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

# #server and port values for outlook login
# port =587
# Email_Server= "smtp.gmail.com"

# Load the configuration file
config_path = Path.cwd() / 'config.json'
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
port= config['port']
Email_server= config['email_server']

#Loading environment variables from the .env file
current_dir= Path.cwd()#current working directory
envars = current_dir / "creds.env"
load_dotenv(envars)

#accessing the environment variables
sender_email=os.getenv("EMAIL")
password_email=os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, course, start_date, end_date):
    #context of the email
    msg = MIMEText(f"""\
            Hi {name},
            This is a remainder mail to complete the {course} course assigned to you on {start_date}.
            Please try to finish the course within the specified end date: {end_date}.
        """)
    #assigning with Subject, From, To fields for the email to be sent
    msg["Subject"] = subject
    msg["From"] = formataddr(( "Messenger-Bot", f"{sender_email}"))
    msg["To"]=receiver_email
    

    try:
        server = smtplib.SMTP(Email_server, port)#creating an server instance
        server.starttls()#initiating a secure connection to the SMTP server
        server.login(sender_email,password_email)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print(f"Email sucessfully sent to {receiver_email}")
        server.quit()
    except Exception as e:
        print(f"Failed to send email to {receiver_email}")
        print(e)
