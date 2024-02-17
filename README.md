# Email Sender App

This Python script allows you to send multiple emails using Gmail's SMTP server.

## Instructions

1. **Setting up App Password for Gmail**:

   To use this script, you need to set up an app password for your Gmail account. Follow these steps:

   - Go to your Google Account settings: [Google Account](https://myaccount.google.com/)
   - Navigate to "Security" on the left sidebar.
   - Scroll down to "Signing in to Google" and click on "App passwords".
   - You may need to enter your Gmail password again for verification.
   - Under "Select app", choose "Mail" and under "Select device", choose "Other (custom name)".
   - Enter a name for the custom name (e.g., "Python Email Sender") and click on "Generate".
   - Google will generate a 16-character app password for you. Copy this password.
   - Use this generated app password instead of your actual Gmail password when running the script.

2. **Running the Script**:

   - Clone this repository or download the `emailsender.py` file.
   - Open a terminal or command prompt and navigate to the directory containing `emailsender.py`.
   - Run the script by executing `python send_emails.py`.
   - Follow the prompts to enter the necessary information: target's Gmail, your Gmail, app password, subject, message, and the number of times to send the email.
