# Краткое руководство

## Описание

Скрипт позволяет редактировать определенные поля в базе данных электронного дневника, что значительно улучшает успеваемость.
Скрипт может:
- Исправлять отметки
- Удалять нарекания со стороны преподавательского состава
- Добавлять поощрения

## Требования к окружению

Скрипт работает совместно с фреймворком Django, определенным образом сконфигурируемым.
Прежде чем использовать скрипт, необходимо развернуть соотвествующее окружение, либо использовать уже готовое решение. (см. далее)
Инструкция ниже написана для пользователей ОС Windows.

## Простой запуск

Чтобы исправить отметки, убрать замечания и добавить похвалу в электронный дневник необходимо:
1. Скачать файл scripts.py по адресу [GitHub](https://github.com/Rostwik/ediary/archive/refs/heads/main.zip), скопировать его в директорию проекта электронного дневника рядом с файлом manage.py
2. Запустить оболочку Shell [Туториал на английском](https://www.csestack.org/open-python-shell-django/)
Открываем командную строку: сочетание клавиш win + r , вводим cmd и нажимаем enter.
Переходим в папку, где расположена БД электронного дневника : так выглядит формат команды Cd [/d] [диск:][путь]. Предположим, что проект развернут в папке "ediary" на диске D:,
в таком случае команда будет выглядеть так : cd D:\ediary. Теперь необходимо в командной строке ввести следующую команду для запуска Shell:
   

```
python manage.py shell
```

Если Вы все сделали правильно, курсор изменится на ">>>"

3. Теперь нужно последовательно ввести следующие команды, завершающиеся enter.
Загрузка в систему данных программы:


```python
from scripts import fix_marks, remove_chastisements, create_commendation
```


Исправление отметок "2" и "3" на отлично(в скобках нужно указать с кавычками свои Фамилию Имя, например "Пупкин Василий"):

```python
fix_marks("Фамилия Имя")
```

Удаление всех замечаний на уроках:

```python
remove_chastisements("Фамилия Имя")
```

Добавление похвалы от учителя на последнем уроке указанной дисциплины(здесь необходимо через запятую указать "Фамилия Имя", "Предмет"):

```python
create_commendation("Фамилия Имя", "Предмет")
```
4. Обязательно читайте, что после enter выводит программа. 
   ####Возможные ответы:
        -"Заполни, пожалуйста, все поля внимательно" - Вы указали в скобках пустые поля
        -"Найдено несколько похожих учеников, уточните искомое знаение" - Ваши Фамилия или Имя написаны неполностью, либо перепутаны с другим учеником 
        -"Такого ученика нет" - Вы допустили ошибки в написании Фамилии или Имени
        -"Такого предмета не существует" - при написании предмета Вы ошиблись, тщательно проверьте все символы
        -"На последнем уроке по этому предмету у тебя уже есть похвала, попробуй другой предмет" если в базе данных уже есть похвала, программа об этом сообщит
    
После указанных выше операций, проверьте результат на сайт электронного дневника - отметки исправлены, исчезли замечания, появидась похвала по указанному предмету.

## Информация для разработчиков

Рабочая конфигурация электронного дневника, а также информация о проекте расположена по адресу: [Ссылка на Github](https://github.com/devmanorg/e-diary/tree/master)


## Цель проекта

Ознакомление с фреймфорк Django. 

