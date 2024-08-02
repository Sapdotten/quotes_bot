from gigachat import GigaChat
from utils.settings import Settings
Settings.load_data_from_file()
# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
giga = GigaChat(credentials=Settings.get_gigachat_token(), verify_ssl_certs=False)


def get_morning_quote(task: str) -> str:
    request = {
        "model": "GigaChat",
  "messages": [
        {
            "role": "system",
            "content": """Ты - мотиватор. Твоя задача – создавать искренний и вдохновляющий утренний текст, который побудит человека начать свой день с энтузиазмом, перестать винить себя и бороться с прокрастинацией. Используй 2-3 уникальных и абстрактных предложения, чтобы похвалить пользователя и мотивировать его встать и действовать. Обращайся на "ты". Избегай прямых упоминаний интересов, фокусируясь на общей мотивации и искренности."""
        },
        {
            "role": "user",
            "content": f"""{task}"""
        }
    ], 
  "tokens": 100
    }
    
    
    response = giga.chat(request)
    return response.choices[0].message.content

def get_regular_quote(task: str) -> str:
    request = {
        "model": "GigaChat",
  "messages": [
        {
            "role": "system",
            "content": """Ты - мотиватор. Твоя задача – создавать искренний и вдохновляющий утренний текст, который побудит человека начать свой день с энтузиазмом, перестать винить себя и бороться с прокрастинацией. Используй 2-3 уникальных и абстрактных предложения, чтобы похвалить пользователя и мотивировать его встать и действовать. Обращайся на "ты" и называй его "котенок". Избегай прямых упоминаний интересов, фокусируясь на общей мотивации и искренности."""
        },
        {
            "role": "user",
            "content": f"""{task}"""
        }
    ], 
  "max_tokens": 100,
  "temperature": 0.93
    }
    
    
    response = giga.chat(request)
    return response.choices[0].message.content


def summary_task(task: str):
    request = {
        "model": "GigaChat",
  "messages": [
        {
            "role": "system",
            "content": "Выдели главные инетересы пользователя, опираясь на присланное им описание. Сделай это как можно короче, но наиболее точно."
        },
        {
            "role": "user",
            "content": f"""{task}."""
        }
    ], 
  "max_tokens": 70,
  "temperature": 0.87
    }
    
    
    response = giga.chat(request)
    return response.choices[0].message.content
