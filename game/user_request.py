import pygame
from tower.towers import Tower, Vacancy

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start new wave":
            if model.enemies.is_empty():
                model.enemies.add(10)
                model.wave += 1


class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_cost()
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "upgrade" and model.selected_tower.level < 5:
            if model.money >= model.selected_tower.get_cost():
                model.money -= model.selected_tower.get_cost()
                model.selected_tower.level += 1
            # if the money > upgrade cost of the selected tower , level+1
            # use model.selected_tower to access the selected tower data
            # use model.money to access to money data


class TowerMove:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "move":
            temp = model.selected_tower.name
            model.towers.remove(model.selected_tower)
            model.show_moving_tower = True
            previous_x, previous_y = model.selected_tower.rect.center
            if model.selected_plot is not None:
                # build a tower to new position, remove new plot, and append previous plot
                x, y = model.selected_plot.rect.center
                model.plots.remove(model.selected_plot)
                model.selected_plot = None
            # else build a tower at previous position
            else:
                x = previous_x
                y = previous_y
            tower_dict = {"Moon Tower": Tower.moon_tower(x, y), "Fire Totem": Tower.red_fire_tower(x, y),
                          "Ice Totem": Tower.blue_fire_tower(x, y), "Obelisk Tower": Tower.obelisk_tower(x, y)}
            new_tower = tower_dict[temp]
            model.towers.append(new_tower)
            model.selected_tower = None


class TowerProperties:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "properties":
            model.show_tower_info = True


class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["moon", "red fire", "blue fire", "obelisk"]

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                if model.selected_plot is not None:
                    x, y = model.selected_plot.rect.center
                    tower_dict = {"moon": Tower.moon_tower(x, y), "red fire": Tower.red_fire_tower(x, y),
                                  "blue fire": Tower.blue_fire_tower(x, y), "obelisk": Tower.obelisk_tower(x, y)}
                    new_tower = tower_dict[user_request]
                    if model.money > new_tower.get_cost():
                        model.money -= new_tower.get_cost()
                        model.towers.append(new_tower)
                        model.plots.remove(model.selected_plot)
                        model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()

