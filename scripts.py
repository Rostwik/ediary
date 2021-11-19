import random

from datacenter.models import Schoolkid, Commendation, Chastisement, Mark, Lesson, Subject


def get_kid(name):
    try:
        kid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько похожих учеников, уточните искомое знаение.')
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет.')
    else:
        return kid


def fix_marks(name):
    kid = get_kid(name)
    marks = Mark.objects.filter(schoolkid=kid, points__in=['2', '3'])
    if marks:
        for mark in marks:
            mark.points = '5'
            mark.save()


def remove_chastisements(name):
    kid = get_kid(name)
    chasts = Chastisement.objects.filter(schoolkid=kid)
    if chasts:
        chasts.delete()


def create_commendation(name, subject):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]

    if not subject or not name:
        print('Заполни, пожалуйста, все поля внимательно.')
        return

    kid = get_kid(name)

    try:
        Subject.objects.get(title=subject, year_of_study=kid.year_of_study)
    except Subject.DoesNotExist:
        print('Такого предмета не существует.')
    else:
        try:
            Lesson.objects.get(
                year_of_study=kid.year_of_study,
                group_letter=kid.group_letter,
                subject__title=subject)
        except Lesson.DoesNotExist:
            print('Урока с таким предметом не существует.')
        except Lesson.MultipleObjectsReturned:
            lesson = Lesson.objects.filter(
                year_of_study=kid.year_of_study,
                group_letter=kid.group_letter,
                subject__title=subject).order_by('-date').first()
            is_commendation = Commendation.objects.filter(subject=lesson.subject, created=lesson.date)
            if not is_commendation:
                Commendation.objects.create(text=random.choice(commendations), created=lesson.date, schoolkid=kid,
                                            subject=lesson.subject, teacher=lesson.teacher)
            else:
                print('На последнем уроке по этому предмету у тебя уже есть похвала, попробуй другой предмет')
