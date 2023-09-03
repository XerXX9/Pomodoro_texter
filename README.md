# Pomodoro Timer

This is a simple Pomodoro Timer script written in Python. It helps you manage your study and break sessions by setting timers and sending email alerts when your break time is over.

## Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/pomodoro-timer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pomodoro-timer
    ```

3. Open the `pomodoro_timer.py` file and replace the Gmail account credentials with your own:

    ```python
    user = "your_email@gmail.com"
    pw = "your_app_password"
    ```

    To generate an app password for your Gmail account, follow these steps:

    - **Step 1**: Sign in to your Google Account.

    - **Step 2**: Go to [https://myaccount.google.com/security](https://myaccount.google.com/security).

    - **Step 3**: In the "Signing in to Google" section, click on "App passwords." If you do not see this option enable 2FA.

    - **Step 4**: Sign in again if prompted.

    - **Step 5**: In the "App passwords" section, select "App" as the app and "Other (Custom name)" as the device.

    - **Step 6**: Click "Generate."

    - **Step 7**: Google will generate an app password for you. Copy this password and replace `"your_app_password"` in the script with it.

4. Run the script:

    ```bash
    python pomodoro_timer.py
    ```

5. You will be prompted to enter the number of hours and minutes to study, as well as the number of minutes for your break.

6. The timer will start, and you will receive an email alert when your break time is over.

7. Enjoy productive study sessions with scheduled breaks!

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request. We welcome any improvements or feature additions.

## License

This project is licensed under the MIT License 
