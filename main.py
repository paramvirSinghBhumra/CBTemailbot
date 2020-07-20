def readfile(filename):
    pass

def send_email(firstname="null", lastname='null', receiver_email='personaldeveloper9@gmail.com'):
    import smtplib, ssl, getpass
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

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
    Hello Parents and Campers!

    We hope you are staying safe and healthy during these crazy times. We understand a lot has changed, school, classes, life in general - however, we hope we can make it a little better for you!

    We are happy to announce we will be hosting our 6th ANNUAL CAMP this upcoming August (Aug 3-7) VIRTUALLY. Due to social distancing measures, we wanted to share this opportunity to you all. Children of all skill levels are welcome, where Colorado Bhangra's own dancers will be instructing and leading classes over zoom. Then, there will be a final performance held at the end of the week to be showcased to all friends and family.

    Attached is a form that needs to be completed by JULY 29th to be admitted into camp.

    Pricing:
    $45 per child, ($35 per child for siblings) due in full before the 31st of July. If you sign up before the 27th, you'll get a 10% DISCOUNT! 

    There will be a confirmation email of your submission and instructions of payment will be listed in the email.



    If you have general questions, please contact mailto:coloradobhangrainstitute@gmail.com.  

    For one on one questions, please contact Captain Vriti Seth at tel:(303)-809-0300 or Captian Ria Sunil at tel:(303)-887-7103
    """

    html = """\
    <html>
      <body>
        <p>
        Hello Parents and Campers!
        <br><br>
        We hope you are staying safe and healthy during these crazy times. We understand a lot has changed, school, classes, life in general - however, we hope we can make it a little better for you!
        <br><br>
        We are happy to announce we will be hosting our 6th ANNUAL CAMP this upcoming August (Aug 3-7) VIRTUALLY. Due to social distancing measures, we wanted to share this opportunity to you all. Children of all skill levels are welcome, where Colorado Bhangra's own dancers will be instructing and leading classes over zoom. Then, there will be a final performance held at the end of the week to be showcased to all friends and family.
        <br><br>
        Attached is a form that needs to be completed by JULY 29th to be admitted into camp.
        <br><br>
        Pricing:
        $45 per child, ($35 per child for siblings) due in full before the 31st of July. If you sign up before the 27th, you'll get a 10% DISCOUNT! 
        <br><br>
        There will be a confirmation email of your submission and instructions of payment will be listed in the email.
        <br>
        <br>
        <br>

        If you have general questions, please contact <a href="mailto:coloradobhangrainstitute@gmail.com">coloradobhangrainstitute@gmail.com</a>.  
        <br><br>
        For one on one questions, please contact Captain Vriti Seth at tel:(303)-809-0300 or Captian Ria Sunil at tel:(303)-887-7103
        <br><br>
        </p>
           <iframe src="//https://docs.google.com/forms/d/e/1FAIpQLSceGkMaS4G8tHPHBq2IK09jDTV8IIcrLeQK_QaTu2hZc_tH4w/viewform?embedded=true" width="640" height="410" frameborder="0" marginheight="0" marginwidth="0"><a href="https://forms.gle/87JJb8P98fUqro6C9" style="color:red">SIGN UP FORM</a></iframe>
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

    filename="email_attachments/Invite.png"

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)


    #creates secure ssl default context for the mail
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    #with ... as server ensures that the connection is closed once we're done with the code here
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        #TODO: SENT THE EMAIL HERE
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()


if __name__ == "__main__":
    #firstname, lastname, email = readfile("contacts_file.csv")

    # for i in range(len(firstname)):
    #     send_email(firstname[i], lastname[i], email[i])

    send_email(firstname="Pbosss",receiver_email="personaldeveloper9@gmail.com")
