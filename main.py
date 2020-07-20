
def extract_emails(filename):
    import pandas as pd
    df = pd.read_csv(filename)

    return df['emails']

def send_email(sender_email, password, receiver_email):
    import smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    port = 465 #for SSl


    # message = """\
    #     Subject: Hi there
    #
    #     This message is sent from Python."""
    message = MIMEMultipart("alternative")
    message['Subject'] = "Colroado Bhangra Institute ~ VIRTUAL BHANGRA CAMP"
    message['From'] = "coloradobhangrainstitute@gmail.com"
    message['To'] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hello Parents and Campers!

    We hope you are staying safe and healthy during these crazy times. We understand a lot has changed, school, classes, life in general - however, we hope we can make it a little better for you!

    We are happy to announce we will be hosting our 6th ANNUAL CAMP this upcoming August (Aug 3-7) VIRTUALLY. Due to social distancing measures, we wanted to share this opportunity to you all, virtually. Children of all skill levels are welcome, where Colorado Bhangra's own dancers will be instructing and leading classes over zoom. Then, there will be a final performance held at the end of the week to be showcased to all friends and family. A member of our team will personally drop off goodie bags and film a final video performance compilation for all of the campers!

    Attached is a form that needs to be completed by JULY 29th to be admitted into camp.

    Pricing:
    $45 per child, ($35 per child for siblings) due in full before the 31st of July. If you sign up before the 27th, you'll get a 10% DISCOUNT! 

    There will be a confirmation email of your submission and instructions of payment will be listed in the email.
    Hope to see you soon!



    If you have general questions, please contact us at mailto:coloradobhangrainstitute@gmail.com.

    For one on one questions, please contact Captain Vriti Seth at <a href="tel:303-809-0300">303-809-0300</a> or Captian Ria Sunil at <a href="tel:303-887-7103">303-887-7103</a>


    For one on one questions, please contact Captain Vriti Seth at tel:(303)-809-0300 or Captian Ria Sunil at tel:(303)-887-7103
    click the link to sign up the form: https://forms.gle/87JJb8P98fUqro6C9
    """

    html = """\
    <html>
      <body>
        <p>
        Hello Parents and Campers!
        <br><br>
        We hope you are staying safe and healthy during these crazy times. We understand a lot has changed, school, classes, life in general - however, we hope we can make it a little better for you!
        <br><br>
        We are happy to announce we will be hosting our 6th ANNUAL CAMP this upcoming August (Aug 3-7) VIRTUALLY. Due to social distancing measures, we wanted to share this opportunity to you all, virtually. Children of all skill levels are welcome, where Colorado Bhangra's own dancers will be instructing and leading classes over zoom. Then, there will be a final performance held at the end of the week to be showcased to all friends and family.
        <br><br>
        Attached is a form that needs to be completed by <span style="color:red"><b><u>JULY 29th</u></b></span> to be admitted into camp.
        <br><br>
        Pricing:
        $45 per child, ($35 per child for siblings) <span style="color:red"><b><u>due in full before the 31st of July.</u></b></span> If you sign up before the 27th, you'll get a 10% DISCOUNT! 
        <br><br>
        There will be a confirmation email of your submission and instructions of payment will be listed in the email.
        <br>
        Hope to see you soon!
        <br>
        <br>
        <br>

        If you have general questions, please contact us at <a href="mailto:coloradobhangrainstitute@gmail.com">coloradobhangrainstitute@gmail.com</a>.  
        <br><br>
        For one on one questions, please contact Captain Vriti Seth at <a href="tel:303-809-0300">303-809-0300</a> or Captian Ria Sunil at <a href="tel:303-887-7103">303-887-7103</a>
        <br><br>
           <iframe src="https://docs.google.com/forms/d/e/1FAIpQLScvu1CI01zHw7HOR0EsaQrTLQAEjA120PovLsjtIueFblHskQ/viewform?embedded=true" width="640" height="2935" frameborder="0" marginheight="0" marginwidth="0"><a href="https://forms.gle/N3RpGj7wJocTypGZ9" style="color:#c71585; font-size:23px;">SIGN UP FORM</a></iframe>
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
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        #TODO: SENT THE EMAIL HERE
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("successfully sent email to %s"%(receiver_email))
        server.quit()


if __name__ == "__main__":
    import getpass
    emails = extract_emails("emails.csv")

    sender_email = 'noreply.cbinstitute@gmail.com'
    password = getpass.getpass(prompt="enter the password for %s: " %(sender_email))

    for email in emails:
        print("sending email to %s"%(email))
        send_email(sender_email, password, email)


    #testing
    # send_email('personaldeveloper9@gmail.com')
