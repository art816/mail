#!/usr/bin/env python3

import smtplib, sys, email.utils, mailconfig
mailserver = mailconfig.smtpservername
# например: smtp.rmi.net
From = 'fizmat39reg.bot@mail.ru'#input('From? ').strip()
To = 'fizmat39reg.bot@mail.ru'#input('To? ').strip()
Tos = 'fizmat39reg.bot@mail.ru'#To.split(';')
Subj = ''#input('Subj? ').strip()
Date = email.utils.formatdate()
# или импортировать из mailconfig
# например: python-list@python.org
# допускается список получателей
# текущие дата и время, rfc2822
# стандартные заголовки, за которыми следует пустая строка и текст
text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To,
Date, Subj))
print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break
    text += line
# серверы могут экранировать
print('Connecting...')
server = smtplib.SMTP_SSL(mailserver, port='465') # соединиться без регистрации
print("Connected\n")
server.login('fizmat39reg.bot@mail.ru', '42210991')
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:
# smtplib может возбуждать исключения
    print('Failed recipients:', failed) # но здесь они не обрабатываются
else:
    print('No errors.')
print('Bye.')
