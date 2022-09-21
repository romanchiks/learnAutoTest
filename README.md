https://stepik.org/lesson/237240/step/9?unit=209628

!!!
"browser" переименован в "driver", то есть в п.3 "Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр." вместо browser передается driver
!!!

Запуск после скачивания проекта (комманды для windows при условии, что в командной строке открыта корневая папка проекта):

1. mkdir environments
2. cd environments
3. python -m venv selenium_env
4. cd..
5. environments\selenium_env\Scripts\activate.bat
6. pip install -r req_selenium_env.txt

После проделанных шагов можно приступать к проверке задания:

1. pytest --language=es test_items.py
2. (до проверки добавить в test_items.py команду time.sleep(30) после команды driver.get()) pytest --language=fr test_items.py
