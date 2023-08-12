from datetime import datetime

from car import Car


class Glissade(Car):
    def needs_service(self):
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date() or super().needs_service()
