import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 587 
    
    username = "YOUR EMAIL"
    password = "YOUR PASSWORD"  # Use an app password for Gmail
    
    receiver = "EMAIL RECEIVER"
    ##context = ssl.create_default_context()
    
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message)