from typing import Dict, List, Generator

from .views import MinigamesView, OverallView, SkillsView
from .types import CategoryTypes


def format_data(item):
    if item:
        string = ''.join(v for v in item if v.isalnum()).lower()
        if string.isdigit():
            return int(string)
        return string
    return item


class SkillsModel:

    def __init__(self) -> None:
        self.aslist: List[SkillsView] = list()
        self.asdict: Dict[str, SkillsView] = dict()
        self.__set_defaults_properties()


    def __iter__(self) -> Generator[SkillsView, None, None]:
        for skill in self.aslist:
            yield skill

        
    def __getitem__(self, skill: str) -> SkillsView:
        return self.asdict[skill.title()]


    def __setitem__(self, skill_properties: list) -> None:
        name = skill_properties.pop(0)
        for i, attr in enumerate(['rank', 'level', 'xp']):
            self.asdict[name].__setattr__(attr, format_data(skill_properties[i]))


    def __set_defaults_properties(self) -> None:
        for property in CategoryTypes.SKILLS:

            icon = f'https://www.runescape.com/img/rsp777/hiscores/skill_icon_{format_data(property)}1.gif'

            sk_obj, icon = (OverallView, None) if property == 'Overall' else (SkillsView, icon)
            sk_obj = sk_obj(name=property, icon=icon)

            self.aslist.append(sk_obj)
            self.asdict[sk_obj.name] = sk_obj
        

class MinigamesModel:

    def __init__(self, category: str) -> None:
        self.aslist: List[MinigamesView] = list()
        self.asdict: Dict[str, MinigamesView] = dict()
        self.category = category
        self.__set_defaults_properties()


    def __iter__(self) -> Generator[MinigamesView, None, None]:
        for skill in self.aslist:
            yield skill


    def __getitem__(self, minigame: str) -> MinigamesView:
        return self.asdict[minigame.title()]


    def __setitem__(self, minigame_properties: list) -> None:
        name = minigame_properties.pop(0)

        for i, attr in enumerate(['rank', 'score']):
            self.asdict[name].__setattr__(attr, format_data(minigame_properties[i]))


    def __set_defaults_properties(self) -> None:
        for property in CategoryTypes.get_properties_from_category(self.category):
            icon = f'https://www.runescape.com/img/rsp777/game_icon_{format_data(property)}.png'

            mg_obj = MinigamesView(name=property, icon=icon)
            self.aslist.append(mg_obj)
            self.asdict[mg_obj.name] = mg_obj
