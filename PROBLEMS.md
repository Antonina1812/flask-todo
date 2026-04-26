Я использовала виртуалку с Arch Linux для поднятия контейнеров на ней и вот с какими проблемами я столкнулась в ходе работы:

## 1. В прометее замечена разница во времени, поэтому данные не собираются
![alt text](<screenshots/Снимок экрана — 2026-04-26 в 22.40.44.png>)

**РЕШЕНИЕ**
Время на виртуалке не синхронизировано время. Для синхронизации выполняем: 
***pacman -S ntp***
***systemctl enable ntpd***
***systemctl start ntpd***
***timedatectl set-ntp true***

## 2. Я забыла логин от Графаны, помню только пароль, сбрасывание пароля не помогает

**РЕШЕНИЕ**
Нужно выполнить запрос к базе данных Графаны, в ней содержатся все логины. Путь к базе данных: **/var/lib/grafana/grafana.db**. Выполняем:
***docker cp flask-todo-grafana-1:/var/lib/grafana/grafana.db ./grafana.db***
***pacman -S sqlite***
***sqlite3 grafana.db "SELECT login, email FROM user;"***