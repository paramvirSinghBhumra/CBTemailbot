def readfile(filename):
    pass

def send_email(firstname="null", lastname='null', receiver_email='personaldeveloper9@gmail.com'):
    import smtplib, ssl, getpass
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    port = 465 #for SSl
    sender_email = 'personaldeveloper9@gmail.com'
    # password = getpass.getpass(prompt="enter your password: ")
    password = input("enter password: ")


    # message = """\
    #     Subject: Hi there
    #
    #     This message is sent from Python."""
    message = MIMEMultipart("alternative")
    message['Subject'] = "subject of email"
    message['From'] = sender_email
    message['To'] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi {firstname},
    How are you?"""
    html = """\
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a>
           has many great tutorials.
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2) #email clients will try to run this first

    #creates secure ssl default context for the mail
    context = ssl.create_default_context()
    #with ... as server ensures that the connection is closed once we're done with the code here
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        #TODO: SENT THE EMAIL HERE
        sever.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    #firstname, lastname, email = readfile("contacts_file.csv")

    # for i in range(len(firstname)):
    #     send_email(firstname[i], lastname[i], email[i])

    send_email(firstname="Pbosss",receiver_email="paramvir.bhumra@yahoo.com")
