import smtplib, ssl
import argparse

def sendEmail(sender,receiver,pd):
    """
        Method to send email to the particular user
        parameter : sender_email, receiver_email, sender_password
    """
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender 
    receiver_email = receiver 
    password = pd
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

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
