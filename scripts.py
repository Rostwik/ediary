import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Schoolkid, Commendation, Chastisement, Mark, Lesson, Subject


def get_kid(name):
    kid = Schoolkid.objects.filter(full_name__contains=name).first()
    return kid


def fix_marks(name):
    kid = get_kid(name)
    marks = Mark.objects.filter(schoolkid=kid, points__in=['2', '3'])
    for mark in marks:
        mark.points = '5'
        mark.save()


def remove_chastisements(name):
    kid = Schoolkid.objects.filter(full_name__contains=name).first()
    chasts = Chastisement.objects.filter(schoolkid=kid)
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

    try:
        kid = Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько похожих учеников, уточните искомое знаение.')
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет.')
    else:
        try:
            Subject.objects.get(title=subject, year_of_study=kid.year_of_study)
        except Subject.DoesNotExist:
            print('Такого предмета не существует.')
        else:
            try:
                lesson = Lesson.objects.filter(
                    year_of_study=kid.year_of_study,
                    group_letter=kid.group_letter,
                    subject__title=subject).order_by('-date').first()
            except Lesson.DoesNotExist:
                print('Урока с таким предметом не существует.')
            else:
                is_commendation = Commendation.objects.filter(subject=lesson.subject, created=lesson.date)
                if not is_commendation:
                    Commendation.objects.create(text=random.choice(commendations), created=lesson.date, schoolkid=kid,
                                                subject=lesson.subject, teacher=lesson.teacher)
                else:
                    print('На последнем уроке по этому предмету у тебя уже есть похвала, попробуй другой предмет')
