import datetime
from app.config import config
import aiohttp


class TelegramLoggerService:
    def __init__(self):
        self.bot_token = config.TELEGRAM_BOT_TOKEN  # type: str
        self.chat_id = config.TELEGRAM_CHAT_ID  # type: int

    async def _send_message(self, message: str) -> str:
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={message}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()

    async def send_answer(self, user_id: int, answer: str, time: datetime.datetime) -> str:
        message = f"Пользователь {user_id} отправил ответ {answer} в {time}"
        return await self._send_message(message)

    async def send_solve(self, user_id: int, time: datetime.datetime, task_number: int) -> str:
        message = f"Пользователь {user_id} решил задачу {task_number} в {time}"
        return await self._send_message(message)
