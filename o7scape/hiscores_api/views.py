from dataclasses import dataclass
from math import floor, pow


@dataclass
class BaseView:
    icon: str = None
    name: str = None
    rank: int = None


    def __lt__(self, them) -> bool:
        if isinstance(them, BaseView):
            return self.rank > them.rank
        return False

    
    def __gt__(self, them) -> bool:
        if isinstance(them, BaseView):
            return self.rank < them.rank
        return False


@dataclass
class OverallView(BaseView):
    level: int = None
    xp: int = None


@dataclass
class SkillsView(OverallView):


    def xp_to_next_level(self) -> int:
        next_level = 0
        for level in range(1, self.level + 1):
            next_level += floor(level + 300 * pow(2, level / 7))
        return floor(next_level / 4) - self.xp

    
    def xp_to_99(self) -> int:
        return 13034431 - self.xp

    

@dataclass
class MinigamesView(BaseView):
    score: int = None