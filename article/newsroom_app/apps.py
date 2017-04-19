from django.apps import AppConfig


class NewsroomAppConfig(AppConfig):
    name = 'newsroom_app'

    def ready(self):
        import newsroom_app.signals
