from datetime import datetime

from car import Car


class Rorschach(Car):
    def needs_service(self):
        service_threshold_date = self.battery.last_service_date.replace(year=self.battery.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date() or super().needs_service()
