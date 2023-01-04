import smtplib
from datetime import datetime

now = datetime.now()

time = now.strftime("%H:%M:%S")
today = now.strftime("%D")
footerMsg = "Sent at: " + time + '\n' + "Dated: " + today


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('thisispratikkabade@gmail.com', 'jljrvlrektohtmmc')

    subject = 'Sample mail'
    body = 'A test for python smtplib.'
    msg = f"Subject:{subject}\n\n{body}\n\n{footerMsg}"

    server.sendmail(
        'from@gmail.com',
        'thisispratikkabade@gmail.com',
        msg
    )
    print('Mail has been sent')
    print(footerMsg)
    input()


send_mail()
