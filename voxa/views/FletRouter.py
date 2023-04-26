
import flet as ft
from views.Backside_views import Backside
from views.Index_Avatar import Avatar
from views.settings_view import SettingsView
from views.About_view import AboutView




class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": Avatar(page),
            "/settings": SettingsView(page),
           "/backside":Backside(page),
           "/about":AboutView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
