import typer

from user_service.interfaces.cli.db import group_db
from user_service.interfaces.cli.service import group_service

cli = typer.Typer()
cli.add_typer(group_db, name="db")
cli.add_typer(group_service, name="service")
