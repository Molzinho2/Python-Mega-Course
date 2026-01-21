import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 587 
    
    username = "igor.mol2013@gmail.com"
    password = "aveprugsfihwahhv"  # Use an app password for Gmail
    
    receiver = "igor-mol@hotmail.com"
    ##context = ssl.create_default_context()
    
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message)