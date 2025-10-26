# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_email(smtp_server, port, sender_email, password, receiver_email, custom_sender_email):
#     # Create a multipart message and set headers
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = "Test Email Subject"

#     # Add HTML body to email
#     html_content = """
#     <html>
#         <body>
#             <h1>This is a test email sent from Python</h1>
#             <p>This email contains HTML content.</p>
#         </body>
#     </html>
#     """
#     message.attach(MIMEText(html_content, "html"))

#     # Connect to SMTP server and send email
#     try:
#         with smtplib.SMTP(smtp_server, port) as server:
#             server.starttls()  # Start TLS encryption
#             server.login(sender_email, password)
#             text = message.as_string()
#             server.sendmail(sender_email, receiver_email, text)
#         print("Email sent successfully from", custom_sender_email, "to", receiver_email)
#         with open('2.txt', 'a+') as f:
#             f.write(f"{smtp_server}|{port}|{sender_email}|{password}\n")
#     except smtplib.SMTPException as e:
#         print(f"Failed to send email from {sender_email}: {e}")

# def main():
#     # Custom sender email
#     custom_sender_email = 'support@netflix.com' 

#     # Read SMTP server information from file
#     with open("working_smtps.txt", "r") as file:
#         for line in file:
#             try:
#                 smtp_server, port, sender_email, password = line.strip().split("|")
#                 port = int(port)
#                 receiver_email = "mxl.him.self@gmail.com"
#                 send_email(smtp_server, port, sender_email, password, receiver_email, custom_sender_email)
#             except ValueError:
#                 print("Invalid line format in smtp_info.txt")

# if __name__ == "__main__":
#     main()



def encode_to_html(text):
    encoded_text = ""
    for char in text:
        encoded_text += "&#x{:02X};".format(ord(char))
    return encoded_text

# Example usage
normal_text = str(input("Entre Your Text: ")) 
encoded_text = encode_to_html(normal_text)
print(encoded_text)
