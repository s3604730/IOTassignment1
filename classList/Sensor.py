# thinking about doing this as an abstract for temperature and humidity.
from abc import ABC, ABCMeta, abstractmethod

# abstract method


class ClassSensor(ABC):
    def __init__(self):
        pass
    # abstract method that both the temperature and humidity classes
    # will use
    @property
    @abstractmethod
    def returnValue(self):
        pass
