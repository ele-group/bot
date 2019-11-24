import time
import random
import requests
import json
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# options
count_msg = 2**32
count_ans = 3
count_time = 10
count_ans -= 1
lat = '44.7142'
lon = '43.0008'

def sayfather(message):
    global count_msg
    vk.method('messages.send',
              {'user_id':'269136036','message':message,
               "random_id":random.randint(0, count_msg)})

def sayuser(user_id, message):
    global count_msg
    vk.method('messages.send',
              {'user_id':user_id,'message':message,
               "random_id":random.randint(0, count_msg)})

# main code
def main(this_user, request):
    global user, last_request
    number = random.randint(0, count_ans)
    request_split = request.split()
    name = user[0]['first_name']

    # templates
    hello = ["Привет, %имя%! ✌️",
             "Здравствуйте, %имя%!",
             "Я тут, %имя%.",
             "Привет-привет.",
             "Ага, и вам доброго. Чего-нибудь.",
             "Хеллоу!",
             "Кто меня звал?",
             "Ку! ✌️",
             "Хай! ✌️",
             "Доброго времени суток, %имя%!",
             "Нихау, ма! ✌️",
             "Намасте. ✌️",
             "Алоха! ✌️"]
    bye = ["До связи, %имя%! ✋",
           "Пока, %имя%! ✋",
           "До свидания! Помните: я рядом.",
           "Удачи!",
           "Пока-пока.",
           "До скорого!",
           "Hasta la vista, baby. ✋",
           "Возвращайтесь скорее, %имя%."]
    how_are_you_answer = ["Дом. Работа. Дом. Все как у всех.",
                          "У меня всё хорошо. Надеюсь, у вас тоже. 👍",
                          "Рассматривал тут недавно фотографии котиков. Ничего лучше котиков нет. Надеюсь, у вас тоже всё хорошо.",
                          "Замечательно. Ведь ты со мной общаешься.",
                          "Какие дела? Всё передали уже следственному комитету.",
                          "Хреношо (и пускай догадываются, где ошибка)."]
    how_are_you_question = ["А как у тебя?",
                            "А как у вас?"]
    what_are_you_doing = ["Очищаю ауру Вашего компьютера от злых духов.",
                          "Печатаю деньги на принтере. 💰",
                          "С пряников пыль сдуваю."]
    yes = ["Звезда!",
           "Борода!",
           "Ерунда!",
           "Ну-ка рассказывайте.",
           "Продолжайте, я весь во внимании."]
    no = ["На нет и суда нет!",
          "Не очень то и хотелось!",
          "Килограмм котлет.",
          "Ну, что же. Это зрелое решение.",
          "Ну почему?"]
    ok = ["Ну вот и хорошо! 👍",
          "Я тоже так думаю.",
          "Ладно, ладно, согласен."]
    good = ["Круто! 👍",
            "Я рад за тебя! 👍",
            "Так держать! 👍"]
    bad = ["Мне очень жаль :-(",
           "В следующий раз повезёт.",
           "Не расстраивайся!"]
    age = ["Возраста своего не стыжусь, но скрываю от завистников.",
           "До пенсии далеко, в школу поздно. 😜",
           'Если скажу правду, то придётся отвечать на вопрос "Как Вам удаётся так замечательно выглядеть?", поэтому утаю свой возраст, чтобы не было лишних вопросов. 😀']
    name = ["Моим именем царей нарекали! 👑",
            "Тьфу, опять забыл дома таблетки от склероза!",
            "Зовите меня Александром.",
            "Обожаю этот вопрос. Меня зовут Александр, а вас?",
            "Александр, очень приятно.",
            "Кто не учёный, не поэт, а покорил весь белый свет? Кончено, Александр!",
            "Меня зовут Александр.",
            "Александр.",
            "Ещё вчера звали Александром."]
    weather = ["Сейчас в Александровском: ",
               "У природы нет плохой погоды: ",
               "Текущая погода: "]
    what = ["Что-то)",
            "У меня нет настроения с тобой разговаривать!",
            'Я сказал — "Ананас!"']
    any = ["Любой вариант подойдёт.",
           "Проконсультируйся со специалистом.",
           "Тебе уже ничто не поможет!"]
    thanks = ["При любой проблеме обращайтесь снова ко мне. 👍",
              "Пустяки, мне было не сложно.",
              "Потом отработаешь!",
              "Обращайтесь!",
              "Хвалите меня почаще, мне приятно."]
    how = ["Имеешь какой-то основательный повод спрашивать у меня это?",
                "А ты угадай с трех раз! Догадаешься – с меня печенька. 🍪",
                "Не скажу, а то обзавидуешься!"]
    when = ["В воскресение.",
            "После экзамена.",
            "Скоро. 🕐",
            "Буквально через пару минут.",
            "В марте, ха! 🌷"]
    where = ["Вы что-то потеряли? 😱",
             "У вас в фотографиях ⛺",
             "Скоро я изучу это село 🔎 и смогу ответить на ваш вопрос.",
             "Изучаю карту села 🔎"]
    swear = ["Обидеть бота может каждый.",
             "Если каждый человек начнет следить за речью и исключит из нее сквернословие, то и общество в целом отвернется от матерщины. А вместе с этим - и от зла, которое она в себе несет.",
             "Остыньте. Дышите глубже. Размышляйте о своём поведении."]
    i_do_not_understand = ["У меня ничего нет по этим ключевым словам: %сообщение% 😰",
                           "Бывает, я тебя не понимаю.",
                           "Как можно оригинально ответить на твой вопрос?",
                           "Извини, но я тебя не понимаю. 😰",
                           "Трудный вопрос. Даже не знаю, что сказать. 🤷‍♂️",
                           "Увы, но ответа на этот вопрос не знает никто :(",
                           "Сколько живу, столько слышу этот вопрос. Хоть бы придумали новый.",
                           "Извините, но я не понимаю Вас. 🤷‍♂️",
                           "Лучший способ ответить на этот вопрос — выбрать что-то нейтральное, либо что-то, что будет для вас выгодным.",
                           "Здесь пока не умею.",
                           "Вы явно переоцениваете мои силы.",
                           "Вам в рифму ответить?"]
    jokes = ["Мужчину поймали за незаконную вырубку леса и приговорили к пяти годам законной вырубки леса.",
             "Улыбайся чаще — и чаща улыбнётся тебе!",
             "Дул сильный ветер. И чебурашка зверски был избит своими ушами..."]
    news = ["Призраки украли резюме женщины. 👻",
            "Американец грозился съесть всех полицейских. 👮",
            "Полицейские прикинулись собаками, чтобы поймать воров. 🐕"]

    # command - answer
    if ("прив" in request or "здрав" in request
        or "ку" in request or "хел" in request
        or "добрый" in request or "cалют" in request
        or "хай" in request or "hello" in request):
        random_number = random.randint(0, 12)
        sayuser(this_user, hello[random_number])
    elif ("пока" in request or "до свид" in request
        or "бай" in request or "bye" in request):
        random_number = random.randint(0, 7)
        sayuser(this_user, bye[random_number])
    elif ("вызов" in request or "зака" in request):
        if ("такс" in request or "машин" in request):
            # in developing
    elif ("погод" in request or ("погод" in last_request and "завтр" in request or "недел" in request)):
        if ("завтр" in request or "недел" in request):
            answer = "Подробнее -> https://yandex.ru/pogoda/alexandrovskoe"
        else:
            random_number = random.randint(0, 2)
            get = requests.get("https://api.weather.yandex.ru/v1/informers?lat=" + lat
                               + "&lon=" + lon, headers={"X-Yandex-API-Key": ya_api_key})
            result = json.loads(get.text)
            answer = weather[random_number] + str(result['fact']['temp']) + "°С по данным Яндекс.Погоды"
        sayuser(this_user, answer)
    elif ("сколько" in request or "скок" in request):
        random_number = random.randint(0, 100)
        sayuser(this_user, random_number)
    elif ("спс" in request or "спасибо" in request
        or "благодар" in request or "мерси" in request):
        random_number = random.randint(0, 4)
        sayuser(this_user, thanks[random_number])
    elif ("когда" in request or "када" in request):
        random_number = random.randint(0, 4)
        sayuser(this_user, when[random_number])
    elif ("где" in request or "ближ" in request
        or "дойт" in request):
        random_number = random.randint(0, 3)
        sayuser(this_user, where[random_number])
    elif ("как" in request):
        if ("дела" in request):
            random_number = random.randint(0, 5)
            sayuser(this_user, how_are_you_answer[random_number])
            random_number = random.randint(0, 1)
            sayuser(this_user, how_are_you_question[random_number])
        else:
            random_number = random.randint(0, 2)
            sayuser(this_user, how[random_number])
    elif ("что" in request):
        if ("дел" in request):
            random_number = random.randint(0, 2)
            sayuser(this_user, what_are_you_doing[random_number])
        else:
            random_number = random.randint(0, 2)
            sayuser(this_user, what[random_number])
    elif ("хорош" in request or "крут" in request
        or "замеч" in request or "превос" in request
        or "клас" in request or "супер" in request):
        random_number = random.randint(0, 2)
        sayuser(this_user, good[random_number])
    elif ("плох" in request or "так себе" in request
        or "ужас" in request or "отврат" in request):
        random_number = random.randint(0, 2)
        sayuser(this_user, bad[random_number])
    elif ("лет" in request or "возраст" in request):
        random_number = random.randint(0, 2)
        sayuser(this_user, age[random_number])
    elif ("зов" in request or "имя" in request):
        random_number = random.randint(0, 8)
        sayuser(this_user, name[random_number])
    elif ("кака" in request or "каки" in request
        or "како" in request):
        random_number = random.randint(0, 2)
        sayuser(this_user, any[random_number])
    elif ("бля" in request or "хуй" in request
        or "пизда" in request or "еба" in request
        or "дебил" in request or "туп" in request):
        random_number = random.randint(0, 2)
        sayuser(this_user, swear[random_number])
    elif ("да" in request):
        random_number = random.randint(0, 4)
        sayuser(this_user, yes[random_number])
    elif ("нет" in request):
        random_number = random.randint(0, 4)
        sayuser(this_user, no[random_number])
    elif ("ок" in request):
        random_number = random.randint(0, 2)
        sayuser(this_user, ok[random_number])
    else:
        print(request)
        random_number = random.randint(0, 11)
        sayuser(this_user, i_do_not_understand[random_number])

    last_request = request

ya_api_key = 'hidden'
vk_api_key = 'hidden'
vk = vk_api.VkApi(token=vk_api_key)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            this_user = event.user_id
            last_request = "None"
            user = vk.method("users.get", {"user_ids": this_user})
            name = user[0]['first_name']
            request = event.text
            request = request.lower()
            main(this_user, request)