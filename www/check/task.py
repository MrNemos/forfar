from www.celery import app
from .models import models

from subprocess import check_output


@app.task(bind=True, default_retry_delay=60, max_retries=5)
def create_check_pdf(self, num):
    try:
        check_output(f'wkthmltopdf http://orders/{num}; exit 0', shell=True)
        Order.object.id(num).status = 'render'
    except Exception as e:
        self.retry(e)
