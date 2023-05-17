from aiogram import types, Dispatcher, Bot
from aiogram.filters import CommandObject, Command
from aiogram.types import Message
from parser import get_info, get_goroda
from region_parser import region_sl
from interaction_with_db import insertion, check_if_in_table, get_second_part

TOKEN: str = open("tk.txt", 'r').readline()

bot: Bot = Bot(token=TOKEN, parse_mode="HTML")
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(f'{message.from_user.username.capitalize()}, введите номер региона, '
                         f'в котором Вы находитесь после команды /reg (например, для Московской области "/reg 50")')


@dp.message(Command("reg"))
async def reg(message: types.Message, command: CommandObject):
    if command.args:
        if str(command.args) in list(region_sl.keys()):
            number = str(command.args)
            second_part = region_sl[number]
            strlist_of_regions = ''
            strlist_of_regions_1 = ''
            res = get_goroda(f'http://kalendar-rybolova.ru{second_part}')
            number_of_goroda = len(res)
            if number_of_goroda > 100:
                for i in range(len(res[:100])):
                    strlist_of_regions += f'{i + 1}. `{second_part}{res[i]}`\n'

                for i in range(len(res[100:])):
                    strlist_of_regions_1 += f'{i + 101}. `{second_part}{res[i]}`\n'
            else:
                for i in range(len(res)):
                    strlist_of_regions += f'{i}. `{second_part}{res[i]}`\n'
            await message.answer('Выберите населенный пункт для рыбалки (выбранное введите в качестве'
                                 'аргумента функции get, например "/get /moskovskaya-oblast/odincovo.php":\n' +
                                 strlist_of_regions, parse_mode='MARKDOWN')
            if strlist_of_regions_1:
                await message.answer(strlist_of_regions_1, parse_mode='MARKDOWN')
        else:
            await message.answer(f"Извините, прогноз погоды пока недоступен для {command.args} региона")
    else:
        await message.answer('Пожалуйста, введите свой регион после команды /reg!\n'
                             '(например, для Московской области "/reg 50")')


@dp.message(Command("get"))
async def reg(message: types.Message, command: CommandObject):
    if command.args:
        try:
            info = get_info(f'http://kalendar-rybolova.ru/{command.args}')
            n = '\n• '
            res_string = ''.join(
                f"<b>{key.replace(':', ',')}</b>: {value[value.find(':') + 1:].replace('- ', n)}"
                for key, value in info.items()
            )
            insertion(message.from_user.id, command.args)
            await message.answer(f"Прогноз погоды для рыбалки в Вашем населенном пункте:"
                                 f"\n{res_string}")
        except Exception:
            await message.answer(
                'Вероятно, Вы допустили ошибку при вводе фаргумента функции get,'
                'пожалуйста, проверьте правильность написания и попробуйте снова\n'
                'Пример команды: /get /moskovskaya-oblast/yahroma.php')

    else:
        await message.answer(
            'Вероятно, Вы допустили ошибку при вводе фаргумента функции get,'
            'пожалуйста, проверьте правильность написания и попробуйте снова\n'
            'Пример команды: /get /moskovskaya-oblast/yahroma.php')


@dp.message(Command("wfc"))
async def reg(message: types.Message, command: CommandObject):
    if check_if_in_table(message.from_user.id):
        try:
            second_part = get_second_part(message.from_user.id)
            info = get_info(f'http://kalendar-rybolova.ru/{second_part}')
            n = '\n• '
            res_string = ''.join(
                f"<b>{key.replace(':', ',')}</b>: {value[value.find(':') + 1:].replace('- ', n)}"
                for key, value in info.items()
            )
            await message.answer(f"Прогноз погоды для рыбалки в Вашем населенном пункте:"
                                 f"\n{res_string}")
        except Exception as e:
            await message.answer(f"Произошла непредвиденная ошибка")
    else:
        await message.answer(f"Вас нет в базе данных пользователей. Чтобы попасть в нее, введите комнаду"
                             f"/start и следуйте инструкциям")


if __name__ == '__main__':
    dp.run_polling(bot)
