from threading import Thread
from queue import Queue


class TrafficLight:
    'Класс светофора'
    def __init__(self, id, is_pedestrian=False):
        self.id = id
        self.is_pedestrian = is_pedestrian
        self.state = 'red'
        self.opposite_light = None
        self.timer = 0
        self.queue = Queue()


    def set_state(self, state):
        'настройка какой свет горит'
        self.state = state
        print(f"Traffic light {self.id} is now {self.state}")


    def opposite_connect(self, trafficlight):
        'добавляет какой светофор напротив'
        self.opposite_light = trafficlight.id
        trafficlight.opposite_light = self.id


    def __str__(self):
        return f'светофор {self.id} сейчас горит {self.state}'


class Intersection:
    'класс перекрестка, в который записываются все светофоры'
    def __init__(self):
        self.traffic_lights = []

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def send_event(self, from_id, to_id, event):
        # Отправка события от одного светофора другому
        for light in self.traffic_lights:
            if light.id == to_id:
                light.queue.put(event)