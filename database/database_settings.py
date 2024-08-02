from string import Template

from utils.settings import Settings


class DBSettings:
    CONNECT_STRING = Template(
        "sqlite+aiosqlite:///$file_path"
    )

    @classmethod
    def get_url(cls) -> str:
        URL = cls.CONNECT_STRING.substitute(
            file_path = Settings.get_database_path())
        return URL