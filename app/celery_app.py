from celery import Celery

celeryapp = Celery(
    "microhub_gateway",
    broker="redis://microhubrediscontainer:6379/0",
    backend="redis://microhubrediscontainer:6379/1"
)

celeryapp.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    result_expires=3600,
    include=["app.tasks"]  # Autodiscovery of tasks
)