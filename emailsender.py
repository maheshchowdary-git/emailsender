import smtplib
from email.message import EmailMessage
import logging

logging.basicConfig(filename='email_sender.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(username, password, user_mail, subject, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(username, password)
            
            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = subject
            msg['From'] = username
            msg['To'] = user_mail
            
            s.send_message(msg)
            
            logging.info(f"Email sent to {user_mail} successfully")
            print(f"Email sent to {user_mail} successfully")
    except Exception as e:
        logging.error(f"Error sending email to {user_mail}: {e}")
        print(f"Error sending email to {user_mail}: {e}")

def main():
    try:
        username = input("Enter your email id: ")
        password = input("Enter your email password: ")
        
        user_mail = input("Enter recipient's email: ")
        subject = input("Enter subject: ")
        message = input("Enter message: ")
        
        if '@' not in user_mail or '.' not in user_mail:
            raise ValueError("Invalid email address")
        
        number_of_mails = int(input("Enter how many times you want to send this email: "))
        
        for _ in range(number_of_mails):
            send_email(username, password, user_mail, subject, message)
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
        print(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


