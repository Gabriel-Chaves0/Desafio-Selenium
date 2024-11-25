import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_paths):

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)

    for attachment_path in attachment_paths:
        with open(attachment_path, 'rb') as attachment:
            file_data = attachment.read()
            file_name = attachment_path.split("/")[-1]
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email enviado com sucesso!")
