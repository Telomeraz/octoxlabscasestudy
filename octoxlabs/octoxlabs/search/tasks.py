import logging

from celery import shared_task

logger = logging.getLogger("celery")


@shared_task
def log_query(username, query):
    logger.info(f"{username}'s query: {query}")
