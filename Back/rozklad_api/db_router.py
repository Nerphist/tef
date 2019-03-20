class RozkladRouter:
    def db_for_read(self, model, **hints):
        from django.conf import settings
        if 'rozklad' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'rozklad_api':
            return 'rozklad'
        return None

    def db_for_write(self, model, **hints):
        from django.conf import settings
        if 'rozklad' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'rozklad_api':
            return 'rozklad'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        from django.conf import settings
        if 'rozklad' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'rozklad_api' or obj2._meta.app_label == 'rozklad_api':
            return True
        return None

    def allow_syncdb(self, db, model):
        from django.conf import settings
        if 'rozklad' not in settings.DATABASES:
            return None
        if db == 'rozklad':
            return model._meta.app_label == 'rozklad_api'
        elif model._meta.app_label == 'rozklad_api':
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'lesson':
            if db == 'rozklad':
                return True
            else:
                return False
        if db == 'rozklad':
            return False
        return None
