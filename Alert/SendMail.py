import smtplib
import ssl


password = "*"
recisender = "fitnessdune@gmail.com"pient = "asharma2633.ca18@chitkara.edu.in"
subject = "With Out Mask Face Detected"
content = "ATTENTION!\nIntruder detected!"  # Email Body
message = '\r\n'.join(['To: %s' % sender, 'From: %s' %
                       recipient, 'Subject: %s' % subject, '', content])
context = ssl.create_default_context()


def send_notification():
    try:
        email = smtplib.SMTP("smtp.gmail.com", 587)
        email.ehlo()  # Can be omitted
        email.starttls(context=context)  # Secure the connection
        email.login(sender, password)
        # TODO: Send email here
        email.sendmail(sender, recipient, message.encode("utf8"))
    except Exception as e:
        print(e)
    finally:
        email.quit()


send_notification()

# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
