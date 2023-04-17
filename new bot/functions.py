from telegram import Update
from telegram.ext import CallbackContext
from Buttons import *
def start(update:Update, context:CallbackContext):

    update.message.reply_html(f"""Assalomu aleykum <b>{update.effective_user.first_name}</b>!

<b>XALQ TA'LIMI VAZIRLIGI HUZURIDAGI  "BARKAMOL AVLOD"respublika bolalar maktabi botiga xush kelibsiz

 Sizga qaysi hudud bo'yicha malumot beraylik:</b>""", reply_markup=all_regions_button())
    return 'state_region'


def command_region(update:Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    context.user_data['region_id'] = data #malumotlarni saqlash uchun
    query.message.edit_text("Tuman/Shaharlar bo'yicha birini tanlang:", reply_markup=tumans_byregion_button(int(data)))
    return  'state_tuman'

def command_tuman(update:Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    context.user_data['tuman_id'] = data
    if data == 'back':
        query.message.edit_text(f"""Assalomu aleykum <b>{update.effective_user.first_name}</b>!

    <b>  XALQ TA'LIMI VAZIRLIGI HUZURIDAGI  "BARKAMOL AVLOD"  respublika bolalar maktabi botiga xush kelibsiz

         Sizga qaysi hudud bo'yicha malumot beraylik:</b>""", reply_markup=all_regions_button(), parse_mode="HTML")
        return 'state_region'
    elif data.isdigit():
        tuman_id = int(data)
        query.message.edit_text("To'garak yo'nalishlaridan birini tanlang : ", reply_markup=tugarak_bytuman_button(tuman_id))
        return 'state_tugarak'


def command_tugarak(update:Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    context.user_data['kurs_id'] = data
    if data == 'back':
        query.message.edit_text("Tuman/Shaharlar bo'yicha birini tanlang:", reply_markup=tumans_byregion_button(int(context.user_data['region_id'])))
        return 'state_tuman'
    elif data.isdigit():
        tugarak = get_tugarak(int(data))
        context.user_data['kurs_name'] = tugarak[0]
        xabar = f"""
        Bizda to'lovlar oyiga bazaviy hisoblash miqdoriga nisbatan hisoblanadi.
        Tumanlarda----5%
        Shaharlarda----10%
        Viloyatlarda----10%
        Ijtimoiy himoyaga muhtoj oila farzandlari,Mehribonlik uylari va Bolalar shaharchasi tarbiyalanuvchilari,
        imkoniyati cheklangan bolalar   uchun ixtisoslashtirilgan ta’lim muassasalari o‘quvchilari va ichki ishlar
        organlarining profilaktik hisobiga olingan o‘quvchilar «Barkamol avlod» bolalar maktablarida o‘qiganlik uchun ota-onalar to‘lovidan ozod qilinadi.:
        Aloqa nomeri:
        """
        query.message.edit_text(xabar, reply_markup=tugarak_button())
        return "kursga_yozilish"
def command_qabul(update:Update, context:CallbackContext):
    query = update.callback_query
    data = query.data
    if data=="bron":
        query.message.edit_text("Yaxshi a'zo bo'lish  uchun ismingizni kiriting: ", reply_markup=back_button())
        return 'state_name'
    elif data == 'back':
        data = context.user_data['tuman_id']
        tuman_id = int(data)
        query.message.edit_text("Yo'nalishlardan  birini tanlang : ", reply_markup=tugarak_bytuman_button(tuman_id))
        return 'state_tugarak'

def command_back(update:Update, context:CallbackContext):
    data = context.user_data['kurs_id']
    query = update.callback_query
    tugarak = get_tugarak(int(data))
    xabar = f"""
        Bizda to'lovlar oyiga bazaviy hisoblash miqdoriga nisbatan hisoblanadi.
        Tumanlarda----5%
        Shaharlarda----10%
        Viloyatlarda----10%
        Ijtimoiy himoyaga muhtoj oila farzandlari,
        Mehribonlik uylari va Bolalar shaharchasi tarbiyalanuvchilari, imkoniyati cheklangan bolalar
        uchun ixtisoslashtirilgan ta’lim muassasalari o‘quvchilari va ichki ishlar organlarining profilaktik hisobiga
        olingan o‘quvchilar «Barkamol avlod» bolalar maktablarida o‘qiganlik uchun ota-onalar to‘lovidan ozod qilinadi:
        Aloqa nomeri:
            """
    query.message.edit_text(xabar, reply_markup=tugarak_button())
    return "kursga_yozilish"

def command_name(update:Update, context:CallbackContext):
    name = update.message.text
    context.user_data['name'] = name
    update.message.reply_html(f"Hammasi yaxshi <b>{name}</b> endi siz bilan bog'lanish uchun raqamingizni qoldiring", reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Raqam yuborish", request_contact=True)]],resize_keyboard=True, one_time_keyboard=True))
    return 'state_phone'

def command_contact(update:Update, context:CallbackContext):
    phone = update.message.contact.phone_number
    context.bot.send_message(text = f"Kurs nomi: {context.user_data['kurs_name']}\n"
                             f"Ismi: {context.user_data['name']}\n"

                             f"raqami: {phone}", chat_id = -1001619735668)
    update.message.reply_html(f""" Muvaffaqiyatli ro'yxatdan o'tdingiz siz bilan yaqin orada  bog'lanamiz""", reply_markup=all_regions_button())
    return 'state_region'
