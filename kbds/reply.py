from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_kb =  ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            
        ],
        [
            KeyboardButton(text='Справка'),
            KeyboardButton(text='Донат на поддержку бота'),
        ]   
    ],
        resize_keyboard=True,
        input_field_placeholder="Чем могу помочь?"
)



menu_kb =  ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text='Получать ответы на интересующие меня вопросы'),
            
        ],
        [
            KeyboardButton(text='Создание текста'),
            KeyboardButton(text='Создание фото'),
        ]   
    ],
        resize_keyboard=True,
        input_field_placeholder="Для какой цели вам нужна нейросеть?"
)

