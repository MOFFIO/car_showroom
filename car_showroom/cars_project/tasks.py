from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from django.core.mail import mail_admins
from cars_project.models import RequestInfo

logger = get_task_logger(__name__)

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="2", minute="*", day_of_week="*")))
def admin_mail_send():
    logger.info("Start task")
    count = RequestInfo.objects.count()
    logger.info("Task finished: result = %i" % count)
    mail_admins('Subject here', 'Request Info', fail_silently=False,  html_message=str("RequestInfo elements = %i" % count))


@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def test():
   print "is works!"