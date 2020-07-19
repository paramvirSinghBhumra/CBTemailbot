def readfile(filename):
    import smtplib, ssl, getpass, csv, os,sendgrid
    from sendgrid.helpers.mail import Content, Email, Mail
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    # from_email = Email("personaldeveloper9@gmail.com")
    # to_email = Email(receiver_email)
    # subject = "A test email from Sendgrid"
    # content = Content("text/plain", "Here's a test email sent through Python")
    # 
    # mail = Mail(from_email, subject, to_email, content)
    # response = sg.client.mail.send.post(request_body=mail.get())
    # print(response.status_code)
    # print(response.bodsy)
    # print(response.headers)

    port = 465 #for SSl
    sender_email = 'personaldeveloper9@gmail.com'
    password = getpass.getpass(prompt="enter your password: ")

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
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        #TODO: SENT THE EMAIL HERE
        sever.sendmail(sender_email, receiver_email, message.as_string())

    with open(filename) as file:
        reader = csv.reader(file)
        next(reader) #will skip the first row
        for name, email, grade in reader:
            print(f"Sending email to {email}")
            server.sendmail(
            sender_email,
            email,
            message.format(name=name, grade=grade),
            )


if __name__ == "__main__":
    #firstname, lastname, email = readfile("contacts_file.csv")

    # for i in range(len(firstname)):
    #     send_email(firstname[i], lastname[i], email[i])

    send_email(firstname="Pbosss",receiver_email="paramvir.bhumra@yahoo.com")
