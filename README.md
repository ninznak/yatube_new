# yatube_project
Социальная сеть блогеров

# **Проект учебный YATUBE**

## Учебный проект предназначенный для освоения пакета Django Python

### Порядок работы над проектом

 1. Вначале создаётся в GitHub новый репозиторий и копируется ссылка на него (при создании ставим галку README, в  .gitignore устанавливаем Python) и лицензию устанавливаем BSD3 или MIT
 2. Создаём на диске (желательно без длинного пути) папку для хранения проекта
 3. В GIT идем в нашу рабочую директорию и делаем git clone <ссылка GIT>
 4. Создаем виртуальное окружение для нашего проекта VENV
 5. ***pip install Django==2.2.19*** (но можно и более позднюю версию)
 6. **Для создания базовой структуры проекта:** набираем в GIT -- django-admin startproject <имя проекта>
 7. Для тестирования проекта можно запустить его на упрощенном сервере Django: ***python manage.py  runserver***  и теперь можно открывать адрес: **http://127.0.0.1:8000/**
 8. Исключаем из файлов отправляемых на GitHub файлы VENV и IDE, для этого добавляем .vscode/  и .venv/ в файл .gitignore
 9. Для сохранения специфических программ виртуального окружения, делаем команду записи в файл: ***pip freeze > requirements.txt*** (Linux : pkg-resource==000)
 10.Для запуска проекта на др компьютере, из виртуального окружения делаем ***pip install -r requirements.txt*** 

```
mermaid
graph LR;
A[YaTube] -- LearnProcess --> B((MD file));
A --> C(Creating Progect Folders);
B --> D{Git PUSH};
C --> D;
```

### Автор - Александр К.
### +7(926)668-88-55
