#!/usr/bin/env python3

#Импорт системных библиотек
#Эти библиотеки используются для создания веб-сервера
import urllib.request

#Переменная содержит запрос к локальному серверу"http://localhost:1234/"
fb = urllib.request.urlopen("http://localhost:1234/")

#encodedContent соответствует закодированному ответу сервера ('index.html')
#decodedContent соответствует раскодированному ответу сервера(т.е. то, что мы хотим вывести на экран)
encodedContent = fb.read()
decodedContent = encodedContent.decode("utf8")

#Выводим содержимое файла, полученного с сервера
print(decodedContent)

#Закрываем соединение с сервером
fb.close()

