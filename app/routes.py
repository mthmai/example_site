
from typing import Any, List

from flask import Flask, render_template

from app.abstract_classes import Routes

class HomeRoute(Routes):
    def validator(self) -> bool:
        try:
            @self.app.route('/')
            def get_homepage():
                self.return_query = render_template("index.html")
                return self.return_query
            return True
        except Exception as error:
            print('Deu erro na rota: ', error)
            return False
    def action(self):
       return self.app

class LoginRoute(Routes):
    def validator(self) -> bool:
        try:
            @self.app.route('/login')
            def get_login():
                self.return_query = render_template("login_page.html")
                return self.return_query
            return True
        except Exception as error:
            print('Deu erro na rota: ', error)
            return False

    def action(self):
        return self.app

class WorksRoute(Routes):
    def validator(self) -> bool:
        try:
            @self.app.route('/works')
            def get_works():
                self.return_query = render_template("works_page.html")
                return self.return_query
            return True
        except Exception as error:
            print('Deu erro na rota: ', error)
            return False
    def action(self):
        return self.app

      
class IRoutes:
    def __init__(self, strategies: List[Routes]):
        self.strategies = strategies
        self.app = Flask(__name__)
        self._register_routes()
    
    def _register_routes(self):
        for strategies in self.strategies:
            strategies._app = self.app
            strategy = strategies()
            strategy._app = self.app
            if strategy.validator():
                print(f'Route {strategies.__name__} registrada')
            else:
                print(f'Route {strategies.__name__} não foi registrada')

    def action_function(self) -> Any:
        return self.app

if __name__=='__main__':
    instance = IRoutes(strategies=[HomeRoute, LoginRoute, WorksRoute])
    app = instance.action_function()

    app.run(debug=True)