"""
1. Sync, Asynchronous Tasks
Sync operations -> Operations queue => Time = t1 + t2 + t3
Async operations -> Autonomous execution, time Big O => Time = max(t1, t2, t3)

Uses in Django:
User register, send mail, success response with sync code
User register, send main AND return success response = > The mail and the response are autonomous

Img upload, img post processing, response to user with sync
Img upload, img post processing AND response to user with async (image processing executed in background)
2. Celery
- Abstraction on async operations,
- Distributed Task Queue
- Scheduling of tasks

- pip install celery
python -m celery  -A <django_app> worker (-l info)

tasks.py on app level:
import time
from celery import shared_task

@shared_task
def demo_slow_task(param):
    result = 0
    for i in range(param):
        time.sleep(1)
        result += i
    print(result)

3. Redis
- Pub/Sub => Celery
"""

