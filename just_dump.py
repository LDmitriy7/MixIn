@dp.message_handler(regexp="[a-z0-9_-]{10}")
async def release_promo_code(msg: types.Message):
    if msg.text in db.get_all_promo_codes():
        value = db.get_cost_promo_code(msg.text)
        db.incr_user_demo_balance(msg.from_user.id, value)
        db.del_promo_code(msg.text)
        await msg.answer(f'<b>🎁 Вам начислено {value} {config.DEMO_CURRENCY_NAME}🎁</b>')
    else:
        await msg.answer('Этот промокод не действителен')

        
