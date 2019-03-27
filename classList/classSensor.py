#thinking about doing this as an abstract for temperature and humidity.
from abc import ABC, ABCMeta, abstractmethod

class ClassSensor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def returnValue(self):
        pass



