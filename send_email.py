import smtplib, ssl
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(sender,receiver,pd):
    """
        Method to send email to the particular user
        parameter : sender_email, receiver_email, sender_password
    """
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
<<<<<<< HEAD
    sender_email = sender  
=======
    sender_email = sender 
>>>>>>> 77b9cf16361ad9f8bf61c8bef7308138e922caac
    receiver_email = receiver 
    password = pd
    msg = MIMEMultipart("alternative")# create a message

    # setup the parameters of the message
    msg['From']= sender
    msg['To']= receiver
    msg['Subject']= ""# subject

    message = """\
    Hi,
    How are you?
    Email from python"""
        
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
        
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
	"""
	Get the sender email,receiver email and sender gmail password from the command line
	"""
	try:
		#Get the username and number of tweets from command line
		parser = argparse.ArgumentParser(description='Pass the sender email, receiver email and sender password')
		parser.add_argument('--sender_email')
		parser.add_argument('--receiver_email')
		parser.add_argument('--sender_password')

		args = parser.parse_args()
		sender_email = args.sender_email
		receiver_email = args.receiver_email
		sender_password = args.sender_password

		sendEmail(sender_email,receiver_email,sender_password)

	except Exception as ex:
		print("An error occurred: " + str(ex))
