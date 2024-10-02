
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP details (for example, Gmail)
SMTP_SERVER = "smtp.chadlim.tech"
SMTP_PORT = 587
SMTP_USER = "chad@chadlim.tech"
SMTP_PASSWORD = "your_email_password"

def send_email_report(report, to_email, from_email, subject):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the report to the message body
    message.attach(MIMEText(report, 'plain'))

    # SMTP session
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USER, SMTP_PASSWORD)
            text = message.as_string()
            server.sendmail(from_email, to_email, text)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# # Example usage
# if __name__ == "__main__":
#     # Report content
#     report_content = """
#     Daily Report:
#     - Task 1: Completed
#     - Task 2: In Progress
#     - Task 3: Pending
#     """

#     # Email details
#     to_email = "recipient@example.com"
#     from_email = "your_email@example.com"
#     subject = "Daily Report"
    


#     send_email_report(report_content, to_email, from_email, subject)

