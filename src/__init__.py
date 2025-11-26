try:
    from src.config.celery import celery_app
except Exception:  # Celery may be unavailable during tests
    celery_app = None

__all__ = ('celery_app',)
