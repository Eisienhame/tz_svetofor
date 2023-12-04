import time
import random


class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.state = 'red'

    def set_state(self, state):
        self.state = state
        print(f"Traffic light {self.id} is now {self.state}")

    def process_event(self, event):
        # Обработка событий, пришедших от других светофоров, здесь можно обновлять состояние светофора на основе
        # полученных данных
        pass


def main():
    # Инициализация светофоров
    traffic_lights = [TrafficLight(1), TrafficLight(2), TrafficLight(3), TrafficLight(4)]

    while True:
        # Собираем данные о текущей загруженности и времени ожидания
        car_queues = [random.randint(0, 10) for _ in range(4)]
        pedestrian_queues = [random.randint(0, 5) for _ in range(8)]

        # Принятие решения о смене состояния светофоров
        for i, light in enumerate(traffic_lights):
            if car_queues[i] > 5 or pedestrian_queues[i * 2] > 3:
                light.set_state('red')
            else:
                light.set_state('green')

        time.sleep(5)  # Пауза для имитации времени проезда
