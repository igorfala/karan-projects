"""call myemail(receiver, subject, text) function to send email"""

def myemail(receiver, subject, text):
    import smtplib
    receivers = []
    receivers.append(receiver)
    sender = raw_input('Please enter your email address:   ')
    password = raw_input('Please enter your email password:   ')
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        message = "\n Subject: %s\n\n\n%s" %( subject, text.encode('utf-8')) 
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.close()
        print "Succesfully sent"
    except smtplib.SMTPException:
        print "Error: unable to send mail"
