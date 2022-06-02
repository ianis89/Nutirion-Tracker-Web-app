from django.apps import AppConfig


class FreeCalorieCounterConfig(AppConfig):
    name = 'FreeCalorieCounter'

    def ready(self):
    	import FreeCalorieCounter.signals