import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 587 
    
    username = "your email"
    password = "password"  # Use an app password for Gmail
    
    receiver = "email receiver"
    
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message)