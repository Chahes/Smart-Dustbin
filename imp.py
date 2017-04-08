import time
import serial
import smtplib
import socket
TO = ['chahes96@gmail.com']
GMAIL_USER = 'chahes96@gmail.com'
GMAIL_PASS = 'stanthony..'
SUBJECT = 'Dustbin Alert!!'
#TEXT = 'The dustbin is full. YOu Have awarded 5 points'
ser = serial.Serial('COM6', 9600)
#s = socket.socket()
#host = '192.168.43.55' # Get local machine name
#port = 12345                # Reserve a port for your service.
#s.bind((host, port))
#s.listen(5)
#st = ""
def send_email(TEXT):

	for t in TO:
		print("Sending Email")
		smtpserver = smtplib.SMTP("smtp.gmail.com",587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo
		smtpserver.login(GMAIL_USER, GMAIL_PASS)
		header = 'To:' + t + '\n' + 'From: ' + GMAIL_USER
		header = header + '\n' + 'Subject:' + SUBJECT + '\n'
		print header
		msg = header + '\n' + TEXT + ' \n\n'
		smtpserver.sendmail(GMAIL_USER, t, msg)
		smtpserver.close()

while True:
	message = ser.readline()
	#ser.write(str(chr(67)))
	print(message)
	if message[0] == 'A':
		send_email("The dustbin is full. Please empty the dustbin. You will be awarded 5 points.")
	else:
		send_email("The dustbin is Empty Now. You have been awarded 5 points.")
	time.sleep(6)
