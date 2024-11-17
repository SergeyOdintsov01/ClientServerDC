#!/usr/bin/env python3

#Импорт системных библиотек
#Эти библиотеки используются для создания веб-сервера
import http.server
import socketserver

#Переменная handler нужна для обработки запросов клиента серверу
handler = http.server.SimpleHTTPRequestHandler

#Сервер запустится на порте 1234

with socketserver.TCPServer(("", 1234), handler) as httpd:
    #Сервер будт работать постоянно, ожидая запросов отклиентов
    httpd.serve_forever()

