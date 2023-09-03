# pomodoro timer
from email.message import EmailMessage
import smtplib

user = "Enter your username here"
pw = "Enter your app password here"

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subjectj'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,pw)
    server.send_message(msg)
    server.quit()

def countdown(h=0, m=50):
    total_seconds = 3600*h + 60*m 
    while total_seconds >= 0:
        if total_seconds == 0:
            total_seconds -= 1
            countdown_break(ask_break_min)
        else:
            if total_seconds > 3600:
                print(total_seconds//3600, "Hour/s", (total_seconds - ((total_seconds//3600)*3600))//60, "Minute/s", total_seconds % 60, "Second/s")
            else:
                print(round(total_seconds//60), "Minute/s", total_seconds % 60, "Second/s")
            t.sleep(1)
            total_seconds -= 1
    

def countdown_break(m=10):
    print("Your break starts now:")
    total_seconds = 60*m
    while total_seconds >= 0:
        if total_seconds == 0:
            email_alert("Break time has Elapsed", "Your 10 mins of Break time has elapsed", user)
            total_seconds -= 1
        else:
            print(round(total_seconds//60), "Minute/s", total_seconds % 60, "Second/s")
            t.sleep(1)
            total_seconds -= 1
    

ask_hour = int(input("Enter the number of hours to study: "))
ask_min = int(input("Enter the number of minutes to study: "))
ask_break_min = int(input("Enter the number of minutes of break: "))
countdown(ask_hour, ask_min)


