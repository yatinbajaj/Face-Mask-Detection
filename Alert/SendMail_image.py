from email.message import EmailMessage
import smtplib
import ssl
import imghdr
import os

sender = "fitnessdune@gmail.com"
password = "0018$$YbDs"
recipient = "fitnessdune@gmail.com"
subject = "With Out Mask Face Detected"
context = ssl.create_default_context()

msg = EmailMessage()

# generic email headers
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# set the plain text body
msg.set_content('ATTENTION!\nIntruder detected!.')
with open("Face-Mask-Detection\plot.png", 'rb') as m:
    file_data=m.read()
    # it will give the type of file to reciever
    file_type=imghdr.what(m.name)
    # it will give the name of file to reciever
    file_name = os.path.basename(m.name)
    

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)


def send_notification():
    try:
        email = smtplib.SMTP("smtp.gmail.com", 587)
        email.ehlo()  # Can be omitted
        email.starttls(context=context)  # Secure the connection
        email.login(sender, password)
        # TODO: Send email here
        email.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        email.quit()


send_notification()
