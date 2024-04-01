from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InputFile


#name and date
name = KeyboardButton("Добавить название проекта(обязательно)")
date = KeyboardButton("Добавить дату(обязательно)")
delete = KeyboardButton("Удалить предедуший отчёт")
reply_name = ReplyKeyboardMarkup(resize_keyboard=True).add(name).add(date).add(delete)


#menu

menu = KeyboardButton("Меню")
replymenu = ReplyKeyboardMarkup(resize_keyboard=True).add(menu)

#Назад

exit = KeyboardButton("⬅️Назад в меню")
reply_exit = ReplyKeyboardMarkup(resize_keyboard=True).add(exit)

#кнопки меню

zemwork = KeyboardButton("Земляные работы")
betwork = KeyboardButton("Бетонные работы")
gidwork = KeyboardButton("Гидроизоляционные работы")
metalwork = KeyboardButton("Металлоконструкция")
otdelwork = KeyboardButton("Отделочные работы")
trubowork = KeyboardButton("Трубопроводы")
electwork= KeyboardButton("Электромонтажные работы")
natija = KeyboardButton("Закончил ввод📥")
replywork = ReplyKeyboardMarkup(resize_keyboard=True).add(zemwork).add(betwork).add(gidwork).add(metalwork).add(otdelwork).add(trubowork).add(electwork).add(natija)

#Земляные работы

zem1 = KeyboardButton("Разработка грунта механизированным способом м3")
zem2 = KeyboardButton("Разработка грунта вручную м3")
zem3 = KeyboardButton("Планировка площадей механизированным способом м2")
zem4 = KeyboardButton("Планировка площадей вручную м2")
zem5 = KeyboardButton("Устройство подстилающих слоев из ГПС/Щебня м3")
zem6 = KeyboardButton("Устройство подстилающих слоев из ГПС/щебня вручную м3")
zem7 = KeyboardButton("Устройство подстилающих слоев из песка м3")
zem8 = KeyboardButton("Устройство грунтовой подушки м3")
zem9 = KeyboardButton("Обратная засыпка механизированным способом м3")
zem10 = KeyboardButton("Обратная засыпка вручную м3")
reply_zem_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(zem1).add(zem2).add(zem3).add(zem4).add(zem5).add(zem6).add(zem7).add(zem8).add(zem9).add(zem10).add(exit)

#Бетонные работы

bet1 = KeyboardButton("Устройство бетонной подготовки м3")
bet2 = KeyboardButton("Устройство железобетонного крыльца м3")
bet3 = KeyboardButton("Устройство отмостки м3")
bet4 = KeyboardButton("Опалубочные работы м2")
bet5 = KeyboardButton("Бетонирование фундаментов м3")
bet6 = KeyboardButton("Устройство бетонных полов м3")
bet7 = KeyboardButton("Изготовление арматурных изделий тн")
bet8 = KeyboardButton("Армирование тн")
bet9 = KeyboardButton("Изготовление закладных деталей тн")
bet10 = KeyboardButton("Установка закладных деталей тн")
reply_bet_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(bet1).add(bet2).add(bet3).add(bet4).add(bet5).add(bet6).add(bet7).add(bet8).add(bet9).add(bet10).add(exit)

#Гидроизоляционные работы

gid1 = KeyboardButton("Гидроизоляция обмазочная биткмом/пленка м2")
reply_gid_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(gid1).add(exit)

#Металлоконструкция

metal1 = KeyboardButton("Изготовление металлоконструкций тн")
metal2 = KeyboardButton("Монтаж металлоконструкций каркасов тн")
metal3 = KeyboardButton("Монтаж стеновых сэндвинч панелей м2")
metal4 = KeyboardButton("Монтаж кровельных сэндвинч панелей м2")
metal5 = KeyboardButton("Монтаж стенового профлиста м2")
metal6 = KeyboardButton("Монтаж кровельного профлиста м2")
metal7 = KeyboardButton("Установка металлических оград: Устройство ограждений м")
metal8 = KeyboardButton("Монтаж металлических ворот и калиток шт")
reply_metal_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(metal1).add(metal2).add(metal3).add(metal4).add(metal5).add(metal6).add(metal7).add(metal8).add(exit)


#Отделочные работы

otdel1 = KeyboardButton("Устройство перегородок гипсокартоном м2")
otdel2 = KeyboardButton("Устройство подвесного потолка гипсокартоном м2")
otdel3 = KeyboardButton("Облицовка стен гипсокартоном м2")
otdel4 = KeyboardButton("Шпаклевка стен и потолка м2")
otdel5 = KeyboardButton("Окраска стен и потолка водоэмульсионными составами м2")
otdel6 = KeyboardButton("Устройство пола линолеумом м2")
otdel7 = KeyboardButton("Устройство пола керамической плиткой м2")
otdel8 = KeyboardButton("Облицовка стен керамической плиткой м2")
otdel9 = KeyboardButton("Устройство подвесного потолка пластиком/Армстронгом м2")
otdel10 = KeyboardButton("Установка дверных и оконных блоков м2")
otdel11 = KeyboardButton("Кладка кирпичных перегородок м2")
otdel12 = KeyboardButton("Кладка кирпичных стен м3")
otdel13 = KeyboardButton("Устройство стяжек м3")
otdel14 = KeyboardButton("Установка перегородок из типа Akfa м2")
reply_otdel_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(otdel1).add(otdel2).add(otdel3).add(otdel4).add(otdel5).add(otdel6).add(otdel7).add(otdel8).add(otdel9).add(otdel10).add(otdel11).add(otdel12).add(otdel13).add(otdel14).add(exit)

#Трубопроводы

trubo1 = KeyboardButton("Укладка полиэтиленового трубопровода до D40 м")
trubo2 = KeyboardButton("Укладка полиэтиленового трубопровода до D90 м")
trubo3 = KeyboardButton("Укладка полиэтиленового трубопровода до D160 м")
trubo4 = KeyboardButton("Укладка полиэтиленового трубопровода до D450 м")
trubo5 = KeyboardButton("Монтаж сантехприборов шт")
trubo6 = KeyboardButton("Установка смесителей шт")
trubo7 = KeyboardButton("Установка трапов шт")
reply_trubo_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(trubo1).add(trubo2).add(trubo3).add(trubo4).add(trubo5).add(trubo6).add(trubo7).add(exit)

#Электромонтажные работы

elect1 = KeyboardButton("Прокладка кабеля весом до 1 кг с заделкой м")
elect2 = KeyboardButton("Прокладка кабеля весом до 3 кг с заделкой м")
elect3 = KeyboardButton("Прокладка кабеля весом до 9 кг с заделкой м")
elect4 = KeyboardButton("Монтаж заземляющего проводника м")
elect5 = KeyboardButton("Монтаж прибора: Указатель, Табло шт")
elect6 = KeyboardButton("Монтаж прибора: Светильник, Лампа, Выключатель, Переключатель, Розетка шт")
elect7 = KeyboardButton("Монтаж коробки распаячной, ответвительной шт")
elect8 = KeyboardButton("Монтаж автомата выключателя шт")
elect9 = KeyboardButton("Монтаж электрического щита шт")
elect10 = KeyboardButton("Монтаж пластмассового короба м")
elect11 = KeyboardButton("Прокладка гофрированной трубы до D25 мм м")
reply_elect_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(elect1).add(elect2).add(elect3).add(elect4).add(elect5).add(elect6).add(elect7).add(elect8).add(elect9).add(elect10).add(elect11).add(exit)