from aiogram import types, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F

import handlers.answers as ANSWERS

from handlers.states import states
from giga_module import giga
from utils.settings import Settings
from database import user_manager as um
from keyboards.reply_keyboards import std_keyboard



router = Router()
bot: Bot

def register_bot(b: Bot):
    global bot
    bot = b

@router.message(Command(commands=["start"]))
async def start(msg: types.Message, state:FSMContext):
    await msg.answer(text = ANSWERS.START_TEXT)
    await state.set_state(states.FIRST)
    
@router.message(states.FIRST)
async def first_question(msg: types.Message, state: FSMContext):
    task = giga.summary_task(msg.text)
    await um.add_user(msg.from_user.id, task)
    await msg.answer(text = ANSWERS.TASK_ANSWER, reply_markup=std_keyboard())
    await state.clear()
    
    
@router.message(F.text == "Получить цитату сейчас")
async def get_quote(msg: types.Message):
    task = await um.get_task(msg.from_user.id)
    await msg.answer(text=giga.get_regular_quote(task))
    
@router.message(F.text == "Изменить интересы")
async def get_quote(msg: types.Message, state: FSMContext):
    await msg.answer(text = ANSWERS.CHANGE_TASK)
    await state.set_state(states.FIRST)
    
    # answer = giga.get_answer(ONE_PROMPT.substitute(situation = ANSWERS.FIRST_QUESTION, answer = msg.text))
    # await msg.answer(text = answer)
    # await state.update_data(FIRST = msg.text)
    # await state.set_state(Questions.SECOND)
    # await msg.answer(text = ANSWERS.SECOND_QUESTION)
