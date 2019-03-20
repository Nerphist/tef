from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


class RozkladScheduler:
    scheduler = BackgroundScheduler()

    @staticmethod
    def start_rozklad_sync():
        from .service import sync_with_kpi_rozklad
        # for j in RozkladScheduler.scheduler.get_jobs():
        #     if j.name == 'sync_with_kpi_rozklad':
        #         return None
        # RozkladScheduler.scheduler.add_job(sync_with_kpi_rozklad, trigger='cron', second='*/5')
        RozkladScheduler.scheduler.add_job(sync_with_kpi_rozklad, trigger='cron', minute='1')
        print(RozkladScheduler.scheduler.get_jobs())
        RozkladScheduler.scheduler.start()
