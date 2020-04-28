import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# API токен сообщества
mytoken='ваш токен'

# Функция посылающая сообщение
def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text

            # Логика формирования ответа бота
            if('Привет' in request):
                otvet='Ну привет, если не шутишь!'
            else:
                otvet='Я только на "Привет" реагирую'
                
            write_msg(event.user_id, otvet)
