import datetime

import aiohttp

from app.config import config


class TelegramLoggerService:
    def __init__(self):
        self.bot_token = config.TELEGRAM_BOT_TOKEN  # type: str
        self.chat_id = config.TELEGRAM_CHAT_ID  # type: int

    async def _send_message(self, message: str) -> str:
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as resp:
                return await resp.text()

    async def send_answer(
        self, user_id: int, answer: str, time: datetime.datetime
    ) -> str:
        message = f"<b>{time}</b>: Пользователь <code>{user_id}</code> отправил ответ <code>{answer}</code>"
        return await self._send_message(message)

    async def send_solve(
        self, user_id: int, time: datetime.datetime, task_number: int
    ) -> str:
        message = f"<b>{time}</b>: Пользователь <code>{user_id}</code> решил задачу <code>{task_number}</code>"
        if task_number == 10:
            message = f"<b>{time}</b>: Пользователь <code>{user_id}</code> решил задачу <code>{task_number}</code>\n"
            message += f"<b>{time}</b>: Пользователь <code>{user_id}</code> решил задачу последнюю задачу. Поздравляем!\n\n"
            message += f"@DragonProd @i_am_oniel @annaseliw"
        return await self._send_message(message)
