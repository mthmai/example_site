from abc import ABC, abstractmethod
from flask import Flask


class Routes(ABC):
    def __init__(self):
        self._app = None  #Começa como None
        self.return_query = None
    
    @property
    def app(self):
       if self._app == None:
          self._app = Flask(__name__)
       return self._app

    @abstractmethod
    def validator(self) -> bool:
       ...

    @abstractmethod
    def action(self):
       ...