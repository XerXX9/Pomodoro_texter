## Pomodoro Timer Documentation

### Introduction
The Pomodoro Timer is a Python script designed to help users manage their study or work sessions effectively using the Pomodoro Technique. This technique involves breaking work into intervals, traditionally 25 minutes in length, separated by short breaks. After a certain number of work intervals, a longer break is taken. The timer script implements this concept by allowing users to set the duration of their study sessions and breaks.

### Dependencies
The script utilizes the following Python libraries:
- `email.message.EmailMessage`: For constructing email messages.
- `smtplib`: For sending emails via SMTP.
- `time`: For implementing the countdown timer.

### Gmail Account Configuration
Before using the script, users need to configure their Gmail account credentials in the script. They should replace the placeholder values with their actual Gmail username and password.

### Usage
To use the Pomodoro Timer script, follow these steps:

1. **Configure Gmail Account**: Replace the placeholder values for the `user` and `pw` variables with your Gmail account credentials.

2. **Set Website Redirection**: The script includes a feature to block distracting websites during study sessions by redirecting them to `127.0.0.1` in the hosts file. Users can customize the `hosts_path` variable to point to their hosts file, typically located at `C:\Windows\System32\drivers\etc\hosts`.

3. **Define Website List**: Specify the list of distracting websites in the `website_list` variable.

4. **Run the Timer**: Execute the script and provide input when prompted for the following:
   - Number of hours to study
   - Number of minutes to study
   - Number of minutes for breaks
   
5. **During Study Session**: The script will display a countdown timer indicating the remaining time for the study session. It will also block access to distracting websites specified in the `website_list`.

6. **During Breaks**: Once the study session ends, the script will prompt the user to start their break by pressing Enter. A countdown timer will display the remaining time for the break. Upon completion, an email alert will be sent to notify the user that the break time has elapsed.

### Functions
The script contains the following functions:

1. `email_alert(subject, body, to)`: Sends an email alert using a Gmail account.
   - `subject`: Subject of the email.
   - `body`: Body of the email.
   - `to`: Recipient's email address.

2. `countdown(h=0, m=50)`: Starts a countdown timer for studying.
   - `h`: Number of hours to study.
   - `m`: Number of minutes to study.

3. `countdown_break(m=10)`: Starts a countdown timer for a break.
   - `m`: Number of minutes for the break.

### Example Usage
```python
# Get user input for study duration and break duration
ask_hour = int(input("Enter the number of hours to study: "))
ask_min = int(input("Enter the number of minutes to study: "))
ask_break_min = int(input("Enter the number of minutes of break: "))

# Start the countdown timer for studying
countdown(ask_hour, ask_min)
```

### Note
- Ensure that the script is run with appropriate permissions to modify the hosts file and send emails via SMTP.
- Customize the script as needed to fit personal preferences or requirements.
