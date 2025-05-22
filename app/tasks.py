from app.celery_app import celeryapp

@celeryapp.task(name="app.tasks.add")  # Explicitly naming the task
def add(x, y):
    return x + y
