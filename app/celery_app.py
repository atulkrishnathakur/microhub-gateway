from celery import Celery

celery_app = Celery(
    "microhub_gateway",
    broker="redis://microhub_celery:6379/0",  # Redis broker
    backend="redis://microhub_celery:6379/1",  # Redis result backend
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)
