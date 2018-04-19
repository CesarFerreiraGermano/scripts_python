import smtplib
from email.mime.text import MIMEText

remetente = 'email_origem@gmail.com' # Tem que ser gmail, nesse caso
destinatario = ['email_destino@gmail.com'] # Não precisa ser, necessariamente, gmail

mensagem="""\
    <html>
        <head></head>
        <body>
            <img src="https://d2yty0x2cuh2al.cloudfront.net/uploads/image/file/650790/regular_faa03d9f895d3b3d896c1943b62ab80d.png" STYLE="width:420$
            <font color=orange size="4"><b>Saudações!</b></font><br><br>
            <font color=black><b>Texto em negrito</b></font><br><br>
            <i>Texto em itálico</i>
        </body>
    </html>
    """
msg = MIMEText(mensagem,'html','utf-8')
msg['From'] = remetente
msg['To'] = ', '.join(destinatario)
msg['Subject'] = 'Assunto do e-mail'

raw = msg.as_string()

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('email_origem@gmail.com', 'senha_email_origem') # Autenticação de e-mail
smtp.sendmail(remetente, destinatario, raw) # Envio de e-mail
smtp.quit()
