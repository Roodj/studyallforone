# Создание бота для пекарни BreadFastBot

## Установка

Вверху страницы найдите кнопку Code, кликните по ней, затем нажмите Download ZIP:
![Untitled](https://github.com/PracticumGrade/telegram-bot-1/assets/13587415/4a427987-b925-4f58-b955-bac1398abdc9)
и распакуйте архив.

В терминале откройте директорию из распакованного архива и выполните команды:

```
# Создать виртуальное окружение 
# Если у вас linux/macOS:
python3 -m venv venv  
# Если у вас Windows:
python -m venv venv

# Активировать виртуальное окружение
# Если у вас linux/macOS
. venv/bin/activate
# Если у вас Windows:
. venv/Scripts/activate

# Установить библиотеку
(venv) ... pip install python-telegram-bot==13.7
```

Обратите внимание, что устанавливается именно python-telegram-bot версии 13.7.

## Тестирование

## Запуск автотестов

Если у вас не активно виртуальное окружение, активируйте его:
```
# Если у вас linux/macOS
. venv/bin/activate
# Если у вас Windows:
. venv/Scripts/activate
```

Запуск тестов:
```
python test.py
```

### Проверка, что всё точно работает

Автотесты могут лишь направить на нужный путь.
Чтобы по-настоящему проверить работу бота, его нужно запустить.

1. Найдите своего бота в Telegram, нажмите кнопку `Start`
2. Если у вас не активно виртуальное окружение, активируйте его:
   ```
   # Если у вас linux/macOS
   . venv/bin/activate
   # Если у вас Windows:
   . venv/Scripts/activate
   ```
3. Запустите скрипт: `python main.py`.

Бот отправит вам сообщение.