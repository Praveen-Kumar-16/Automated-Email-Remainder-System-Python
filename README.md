# Automated Email Reminder System

This repository contains a Python script for sending automated reminder emails based on data from an Excel file. The script reads configuration details from a config.json file and uses environment variables for email credentials.

## Overview
 The project consists of two main files:
 
  - **main.py**: Reads data from `details.xlsx`, checks if the current date is close to the end date, and sends reminder emails.
  - **send_emails.py**: Contains the send_email function used to send the reminder emails.

## Table of Contents
  - **Installation**
  - **Configuration**
      - **Setting Up config.json**
      - **Setting Up .env for Gmail Accounts**
      - **Setting Up .env for Other Email Providers**
  - **Usage**
  - **Requirements**
  - **Contributing**
  - **License**


## Installation

  1. Clone the repository:

    git clone https://github.com/your-username/your-repository.git
    cd your-repository

   2. Install the required packages:

      Make sure you have Python installed. Then install the required packages using pip:
  
    pip install -r requirements.txt

## Configuration

#### Setting Up `config.json`

Create a config.json file in the root directory of your project with the following content:

    {
        "email_server": "smtp.gmail.com",
        "port": 587,
        "days_remaining": 3
    }

   - **email_server**: SMTP server address. For Gmail, use smtp.gmail.com. For Outlook, use smtp-mail.outlook.com.
   - **port**: SMTP port number. For Gmail, use 587. For Outlook, use 587 as well.
   - **days_remaining**: The number of days before the END_DATE to send the reminder.



#### Setting Up `.env` for Gmail Accounts

If you are using a Gmail account, you need to create an App Password. Follow these steps:

  1. Create an App Password for Gmail:
     - Go to [`Google Account Security`](https://myaccount.google.com/intro/security).
     - Under "Signing in to Google," select "App passwords."
     - Select "Mail" and "Other" (or type a custom name like AutomatedEmailReminder).
     - Click "Generate" and copy the 16-character password.

  2. Create a .env file in the root directory of your project with the following content:

    EMAIL=your-email@gmail.com
    PASSWORD=your-app-password

  Replace your-email@gmail.com with your Gmail address and your-app-password with the 16-character app password generated from Google.



#### Setting Up `.env` for Other Email Providers

If you are using another email provider, you will need to update `config.json` and `.env` accordingly.

 Example `.env` for Outlook:

    EMAIL=your-email@outlook.com
    PASSWORD=your-outlook-password

#### Update the `config.json` for Outlook settings:

    json

    {
        "email_server": "smtp-mail.outlook.com",
        "port": 587,
        "days_remaining": 3
    }

## Usage

  1. Prepare your Excel data:

     Create or update the details.xlsx file in the root directory with the following columns:

     - NAME: Recipient's name
     -EMAIL: Recipient's email address
     -COURSE: Course name
     - START_DATE: Start date of the course (format: YYYY-MM-DD)
     - END_DATE: End date of the course (format: YYYY-MM-DD)

  #### Example `details.xlsx`:
    NAME	EMAIL	COURSE	START_DATE	END_DATE
    John Doe	john.doe@gmail.com	Python Programming	2024-01-01	2024-01-31

  2. Run the script:

  Execute the main.py script to send reminder emails:

    python main.py

  The script will check if the current date is 3 days before the END_DATE and send reminder emails accordingly.



## Requirements

  - Python 3.6 or higher
  - pandas
  - python-dotenv

To install the required packages, use the requirements.txt file:

    pandas
    python-dotenv



## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any bug fixes, features, or improvements.



## License
This project is licensed under the MIT License. See the LICENSE file for details.
