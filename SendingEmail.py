import smtplib
import speech_recognition as sp
import speak as s

EMAIL_ADDRESS = '' #enter your email address here
EMAIL_PASSWORD = '' #enter password here

def send_mail(subject, msg, mail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, mail, message)
        server.quit()
        print("Sending Email...")
        s.my_speak("Sending Email...")
        print("Email sent successfully. Thank You.")
        s.my_speak("Email sent successfully. Thank You.")

    except Exception as e:
        print(e)
