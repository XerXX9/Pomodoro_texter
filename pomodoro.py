# Pomodoro Timer

# Import necessary libraries
from email.message import EmailMessage
import smtplib
import time as t

# Gmail account credentials (You should replace these with your own credentials)
user = "textav7@gmail.com"
pw = "qemj nchb bamn pfyo "
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"

website_list =  ["www.youtube.com","youtube.com", "https://www.youtube.com/", "https://www.instagram.com/","www.instagram.com", "instagram.com", "https://www.twitch.tv/", "twitch.tv", "www.twitch.tv"] 

def email_alert(subject, body, to):
    """
    Sends an email alert using a Gmail account.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to (str): The recipient's email address.

    Returns:
        None
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, pw)
    server.send_message(msg)
    server.quit()
    return
    

def countdown(h=0, m=50):
    """
    Starts a countdown timer for studying.

    Args:
        h (int): The number of hours to study.
        m (int): The number of minutes to study.

    Returns:
        None
    """
    total_seconds = 3600 * h + 60 * m 
    while total_seconds >= 0:
        if total_seconds == 0:
            countdown_break(ask_break_min)
            break
        else:
            if total_seconds > 3600:
                print(total_seconds // 3600, "Hour/s", (total_seconds - ((total_seconds // 3600) * 3600)) // 60, "Minute/s", total_seconds % 60, "Second/s")
            else:
                print(round(total_seconds // 60), "Minute/s", total_seconds % 60, "Second/s")
            t.sleep(1)
            total_seconds -= 1

        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in website_list: 
                if website not in content: 
                    file.write(redirect + " " + website + "\n") 

def countdown_break(m=10):
    """
    Starts a countdown timer for a break.

    Args:
        m (int): The number of minutes for the break.

    Returns:
        None
    """
    p = input("Press enter to start your break:")
    total_seconds = 60 * m
    while total_seconds > 0:
        if total_seconds == 1:
            print(round(total_seconds // 60), "Minute/s", total_seconds % 60, "Second/s")
            email_alert("Break time has Elapsed", "Your 10 mins of Break time has elapsed", user)
            return
        else:
            print(round(total_seconds // 60), "Minute/s", total_seconds % 60, "Second/s")
            t.sleep(1)
            total_seconds -= 1
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line) 
  
            file.truncate() 
     

# Get user input for study duration and break duration
ask_hour = int(input("Enter the number of hours to study: "))
ask_min = int(input("Enter the number of minutes to study: "))
ask_break_min = int(input("Enter the number of minutes of break: "))

# Start the countdown timer for studying
countdown(ask_hour, ask_min)
