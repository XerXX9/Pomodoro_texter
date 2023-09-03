# pomodoro timer
import time as t
from email.message import EmailMessage
import smtplib
sepoch = t.time()
local = list(t.localtime(sepoch))
hour, min, sec = local[3], local[4], local[5]

user = "textav7@gmail.com"
pw = "karcblxfjsbskmhr"

def email_alert(sub, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = sub
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
            countdown_break(askbm)
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
            email_alert("Break time has Elapsed", "Your 10 mins of Break time has elapsed", "9972815243@airtelmail.com")
            total_seconds -= 1
        else:
            print(round(total_seconds//60), "Minute/s", total_seconds % 60, "Second/s")
            t.sleep(1)
            total_seconds -= 1
    

askh = int(input("Enter the number of hours to study: "))
askm = int(input("Enter the number of minutes to study: "))
askbm = int(input("Enter the number of minutes of break: "))
countdown(askh, askm)


