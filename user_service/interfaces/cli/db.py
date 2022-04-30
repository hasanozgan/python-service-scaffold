import typer
from alembic import command
from alembic.config import Config

from user_service.infrastructure.settings import current_settings

group_db = typer.Typer()


@group_db.command("version")
def pg_version() -> None:
    typer.echo("pg version")


@group_db.command("init")
def init() -> None:
    alembic_cfg = get_alembic_config()
    command.init(alembic_cfg, "./migrations")


@group_db.command("migrate")
def db_upgrade() -> None:
    alembic_cfg = get_alembic_config()
    command.upgrade(alembic_cfg, "head")


@group_db.command("makemigrations")
def db_make_migrations() -> None:
    alembic_cfg = get_alembic_config()
    command.revision(alembic_cfg, autogenerate=True)


def get_alembic_config() -> Config:
    alembic_cfg = Config("./alembic.ini")
    alembic_cfg.set_main_option("script_location", "./migrations")
    alembic_cfg.set_main_option("sqlalchemy.url", current_settings.pg_dsn)
    return alembic_cfg
