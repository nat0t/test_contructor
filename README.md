Используемая версия Python: **3.10.10**

Используемая версия Docker: **23.0.1**

Используемая версия Docker Compose: **2.17.2**

---
Проект состоит из двух основных частей:
- модуль конструирования тестов для проверки знаний персонала;
- модуль тестирования персонала.

---
Для конфигурирования и запуска проекта используются файлы configure.sh и start.sh, находящиеся в корневой директории.
Необходимо дать права на исполнение этих файлов:
```shell
chmod +x configure.sh start.sh
```
и запустить их:
```shell
./configure.sh
./start.sh
```