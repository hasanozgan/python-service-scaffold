import typer
import uvicorn

from user_service.infrastructure.setup import current_settings

group_service = typer.Typer()


@group_service.command("start")
def start_service() -> None:
    uvicorn.run(
        "user_service.infrastructure.setup:app",
        host="0.0.0.0",
        port=current_settings.service_port,
        log_level="info",
    )
