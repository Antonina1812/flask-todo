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

## 3. На гитхабе создала репозиторий и нужно запушить репо с виртуалки в этот удаленный. Выполняю git remote add origin https://github.com/Antonina1812/DevOps.git, git branch -M main, git push -u origin main. Далее просят ввести username и пароль. Ввожу всё правильно, но возникает ошибка: remote: Invalid username or token. Password authentication is not supported for Git operations. fatal: Authentication failed for 'https://github.com/Antonina1812/DevOps.git/'

**РЕШЕНИЕ**
Токены безопаснее паролей, потому что они не дают полный доступ к аккаунту, их можно отозвать по отдельности, и для каждого приложения/устройства можно выпустить свой токен. На гитхабе в настройках находим Developer settings, затем Personal access tokens, затем Tokens (classic) и Generate new token (classic). Выбираем права, которые хотим дать. Копируем и при запросе пароля вставляем этоттокен.