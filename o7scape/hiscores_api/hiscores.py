import requests 
from bs4 import BeautifulSoup

from .models import MinigamesModel, SkillsModel
from .types import AccountTypes, CategoryTypes


USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'


class PersonalHiscores(AccountTypes):

    def __init__(self, username: str, account_type: str = AccountTypes.NORMAL) -> None:
        """Searches a player on the hiscores. The default account type is normal."""

        self.username: str = username
        self._account_type: str = account_type
        self.exists: bool = False

        self.skills: SkillsModel = None
        self.bosses: MinigamesModel = None
        self.minigames: MinigamesModel = None
        self.cluescrolls: MinigamesModel = None

        self.refresh()
        

    @property
    def account_type(self):
        try:
            _type = getattr(AccountTypes, self._account_type.upper())
            if _type:
                self._account_type: str = 'oldschool_' + _type if _type != 'normal' else 'oldschool'
                return self._account_type
        except AttributeError:
            raise Exception(f'Account Mode: "{_type}" does not exists..')


    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    
    def refresh(self):
        self.skills = SkillsModel()
        self.cluescrolls = MinigamesModel(category='cluescrolls')
        self.bosses = MinigamesModel(category='bosses')
        self.minigames = MinigamesModel(category='minigames')

        response = requests.get(
            f'https://secure.runescape.com/m=hiscore_{self.account_type}/hiscorepersonal?',
            params={'user1': self.username},
            headers={'User-Agent': USERAGENT}
        )
        if response.status_code == 200:
            self.exists = self._parse_properties(response.content)


    def _parse_properties(self, html) -> bool:
        table = BeautifulSoup(html, 'html.parser').find('div', id='contentHiscores')

        if table.find('div', attrs={'align': 'center'}):
            return False

        for category in table.find_all('tr')[3:]:
            if category.find('th'):
                continue

            items = []
            for val in category.find_all('td'):
                items.append(val.get_text().strip())

            if items:
                items = list(filter(None, items))
                obj = getattr(self, CategoryTypes.from_property(items[0]))
                obj.__setitem__(items)

        return True

    
    def __lt__(self, them) -> bool:
        if isinstance(them, PersonalHiscores):
            return self.skills['overall'].rank > them.skills['overall'].rank
        return False

    
    def __gt__(self, them) -> bool:
        if isinstance(them, PersonalHiscores):
            return self.skills['overall'].rank < them.skills['overall'].rank
        return False
