import pandas as pd
import json
from datetime import datetime, timedelta
from send_emails import send_email
from pathlib import Path

#reading the excel file using pandas
data= pd.read_excel("details.xlsx")
print(data)

config_path = Path.cwd() / 'config.json'
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
days=config['days_remaining']

#Checking on wheather the END_DATE is in date format
if data['END_DATE'].dtype== object:
    data['END_DATE']= pd.to_datetime(data['END_DATE'])
if data['START_DATE'].dtype==object:
    data['START_DATE']= pd.to_datetime(data['START_DATE'])


current_date= datetime.now().date()
subject="Remainder to the course assigned!"
flag=False

#iterating each row in the excel file and assigning the values to respective variables
for index, row in data.iterrows():
    end_date= row['END_DATE'].date()
    start_date= row['START_DATE'].date()
    receiver_email= row['EMAIL']
    name= row['NAME']
    course= row['COURSE']
    if current_date == end_date - timedelta(days):#checking on the current date is 3 days before the end date
        flag=True
        #formating the end_date and start_date into string representation DD/MM/YY
        end_date=end_date.strftime('%d/%m/%y')
        start_date=start_date.strftime('%d/%m/%y')

        #calling out the send_email function
        send_email(subject, receiver_email, name, course, start_date, end_date)
if flag==False:
    print("No records found as per the requirements!")
