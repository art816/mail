#!/usr/bin/env python3

import poplib, getpass, sys, mailconfig

mailserver = mailconfig.popservername # например: 'pop.rmi.net'
mailuser = mailconfig.popusername
# например: 'lutz'
mailpasswd = mailconfig.poppasswdfile
#mailpasswd = getpass.getpass('Password for %s?' % mailserver)
print('Connecting...')

server = poplib.POP3_SSL(mailserver, port=995)
print('connect\n')
server.user(mailuser)
print(mailpasswd, '/n')
server.pass_(mailpasswd)
# соединение, регистрация на сервере
# pass - зарезервированное слово
print("asfadfadfsfadsfasdfasdf\n")
try:
    print(server.getwelcome())
# вывод приветствия
    msgCount, msgBytes = server.stat()
    print('There are', msgCount, 'mail messages in', msgBytes, 'bytes')
    print(server.list())
    print('-' * 80)
    input('[Press Enter key]')
    for i in range(msgCount):
        hdr, message, octets = server.top(i+1, 0)
# octets - счетчик байтов
        for line in message:
            print(line.decode()) # читает, выводит
# все письма
        print('-' * 80)
# в 3.X сообщения - bytes
        if i < msgCount - 1:
# почтовый ящик блокируется
            input('[Press Enter key]') # до вызова quit
finally:
# снять блокировку с ящика
    server.quit()
# иначе будет разблокирован
print('Bye.')
# по тайм-ауту
#M = poplib.POP3_SSL('pop.mail.ru', port='995')
##M.rpop("fizmat39reg.bot@mail.ru")
#M.user("fizmat39reg.bot@mail.ru")
#M.pass_(getpass.getpass())
#numMessages = len(M.list()[1])
#for i in range(numMessages):
#    for j in M.retr(i+1)[1]:
#        print(j)
