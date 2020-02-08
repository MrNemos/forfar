from www.celery import app
from .models import *

from subprocess import check_output


@app.task(bind=True, default_retry_delay=60, max_retries=5)
def create_check_pdf(self, num, type):
    try:
        if type == 'kitchen':
            check_output(f'wkthmltopdf http://lokalhost:8008/check_rend/{num} srv/site/media/pdf/{num}_kitchen; exit 0',
                         shell=True)

            Order.object.id(num).status_kitchen = 'render'
            create_check_pdf(num, 'client').delay()
        else:
            check_output(f'wkthmltopdf http://lokalhost:8008/check_rend/{num} srv/site/media/pdf/{num}_client; exit 0',
                         shell=True)
            Order.object.id(num).status_client = 'render'

    except Exception as e:
        self.retry(e)
