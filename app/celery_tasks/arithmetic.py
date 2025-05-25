from app.config.celery_app import celeryapp

@celeryapp.task(name="app.celery_tasks.arithmetic.add")  # Explicitly naming the task
def add(x, y, z):
    return x + y + z
