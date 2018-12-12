import requests
import config
import telebot
import datetime
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.access_token)
week_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
week_list_rus = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
    'Пятница', 'Суббота', 'Воскресенье']
def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule(web_page, day):

    soup = BeautifulSoup(web_page, "html5lib")
    date = ''
    if day in week_list:
        date = str(week_list.index(day) + 1) + 'day'
    # Получаем таблицу с расписанием
    schedule_table = soup.find("table", attrs={"id": date})

    # Время проведения занятий
    try:
        times_list = schedule_table.find_all("td", attrs={"class": "time"})
    except AttributeError:
        return None
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations = [room.span.text for room in locations_list]
    rooms = [room.dd.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations, rooms, lessons_list


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    day, week, group = message.text.split()
    web_page = get_page(group, week)
    schedule = parse_schedule(web_page, day[1:])
    if schedule is None:
        resp = 'В этот день занятий нет!'
    else:
        times_lst, locations_lst, rooms_lst, lessons_lst = schedule
        resp = ''
        for time, location, room, lession in zip(times_lst, locations_lst, rooms_lst, lessons_lst):
            resp += '<b>{}</b>, {}, {}, {}\n'.format(time, location, room, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    # PUT YOUR CODE HERE
    pass


@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    """ Получить расписание на следующий день """
    _, group = message.text.split()
    today = int(datetime.datetime.today().weekday())
    if today == 6:
        week = int(datetime.datetime.now().isocalendar()[1]) % 2
        today = 0
    else:
        today += 1
        week = (int(datetime.datetime.now().isocalendar()[1]) + 1) % 2 
    web_page = get_page(group, week)
    schedule = parse_schedule(web_page, week_list[today])
    if schedule is None:
        resp = 'В этот день занятий нет!'
    else:
        times_lst, locations_lst, rooms_lst, lessons_lst = schedule
        resp = ''
        for time, location, room, lession in zip(times_lst, locations_lst, rooms_lst, lessons_lst):
            resp += '<b>{}</b>, {}, {}, {}\n'.format(time, location, room, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')
    pass


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    _, week, group = message.text.split()
    web_page = get_page(group, week)
    for day in range(7):
        schedule = parse_schedule(web_page, week_list[day])
        resp = '\n' + '\n' + "<b>{}:</b>".format(week_list_rus[day]) + '\n' + '\n'
        if schedule is None:
            resp += 'В этот день занятий нет!'
        else:
            times_lst, locations_lst, rooms_lst, lessons_lst = schedule
            for time, location, room, lession in zip(times_lst, locations_lst, rooms_lst, lessons_lst):
                resp += '<b>{}</b> {} {} {}\n'.format(time, location, room, lession)
        bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)

