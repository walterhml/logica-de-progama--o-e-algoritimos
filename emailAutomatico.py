import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'walthersouza144@gmail.com'
password = '10062004*'
from_addr = 'walthersouza144@gmail.com'
to_addr = 'karinasouzadasilva25@gmail.com'

# Cria a mensagem
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Mensagem automática'
body = 'ola testando email com python'
msg.attach(MIMEText(body, 'plain'))

# Envia a mensagem
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.quit()

print('Mensagem enviada com sucesso!')
