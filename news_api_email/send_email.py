import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 587 
    
    username = "your email"
    password = "your app password"  # Use an app password for Gmail
    
    receiver = "receiver email"
    ##context = ssl.create_default_context()
    
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message)