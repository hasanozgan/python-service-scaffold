from user_service.infrastructure.settings.logging import init_logging
from user_service.infrastructure.settings.settings import Settings


def create_settings() -> Settings:
    s = Settings()
    init_logging(s)
    return s


current_settings = create_settings()
