# Dockerfile всегда начинается с импорта базового образа
# С помощью FROM импортируем базовый образ python с DockerHub
# Имя образа - python, версия - latest
FROM python:latest

# Для того чтобы запустить код в контейнере, нужно импортировать файлы server.py и index.html
# server.py - имя импортируемого файла, /server/ - от куда импортируем(папка)
ADD server.py /server/
ADD index.html /server/

# Далее меняем рабочую директория образа, где будут выполняться все команды
WORKDIR /server/
