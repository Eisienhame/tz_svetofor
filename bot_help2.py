import time
import random
from threading import Thread
from queue import Queue


#https://docs-python.ru/standart-library/modul-queue-python/

class TrafficLight:
    def __init__(self, id, is_pedestrian):
        self.id = id
        self.is_pedestrian = is_pedestrian
        self.state = 'red'
        self.queue = Queue()
        self.timer = None

    def set_state(self, state):
        self.state = state
        print(f"Traffic light {self.id} is now {self.state}")

    def process_event(self, event):
        # Обработка событий, приходящих от других светофоров
        if self.is_pedestrian:
            # Логика обработки событий для пешеходных светофоров
            pass
        else:
            # Логика обработки событий для автомобильных светофоров
            pass

    def handle_timer(self, event):
        self.queue.put(event)

    def start(self):
        # Запуск обработки событий в отдельном потоке
        Thread(target=self.process_events, daemon=True).start()

    def process_events(self):
        while True:
            if not self.queue.empty():
                event = self.queue.get()
                if event['type'] == 'timer':
                    self.handle_timer(event)
                else:
                    self.process_event(event)
            time.sleep(0.1)

class Intersection:
    def __init__(self):
        self.traffic_lights = []

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def send_event(self, from_id, to_id, event):
        # Отправка события от одного светофора другому
        for light in self.traffic_lights:
            if light.id == to_id:
                light.queue.put(event)

def main():
    intersection = Intersection()
    # Создание и добавление светофоров
    # ...

    # Запуск светофоров
    for light in intersection.traffic_lights:
        light.start()

    # Логика обработки событий на перекрестке
    while True:
        # Анализ ситуации на перекрестке и отправка событий светофорам
        # ...

        time.sleep(5)  # Пауза для имитации времени смены состояний

if __name__ == "__main__":
    main()
