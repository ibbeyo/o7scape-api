from typing import List


class AccountTypes:
    NORMAL          : str = 'normal'
    IRONMAN         : str = 'ironman'
    LEAGUES         : str = 'seasonal'
    DEADMAN         : str = 'deadman'
    TOURNAMENT      : str = 'tournament'
    HARDCORE_IRONMAN: str = 'hardcore_ironman'
    ULTIMATE_IRONMAN: str = 'ultimate'


class CategoryTypes:
    CLUESCROLLS : List[str] = [
        "Clue Scrolls (all)", 
        "Clue Scrolls (beginner)", 
        "Clue Scrolls (easy)", 
        "Clue Scrolls (medium)", 
        "Clue Scrolls (hard)", 
        "Clue Scrolls (elite)",
        "Clue Scrolls (master)"
    ]
    BOSSES      : List[str] = [
        "Abyssal Sire",
        "Alchemical Hydra",
        "Barrows Chests",
        "Bryophyta",
        "Callisto",
        "Cerberus",
        "Chambers of Xeric",
        "Chambers of Xeric: Challenge Mode",
        "Chaos Elemental",
        "Chaos Fanatic",
        "Commander Zilyana",
        "Corporeal Beast",
        "Dagannoth Prime",
        "Dagannoth Rex",
        "Dagannoth Supreme",
        "Crazy Archaeologist",
        "Deranged Archaeologist",
        "General Graardor",
        "Giant Mole",
        "Grotesque Guardians",
        "Hespori",
        "Kalphite Queen",
        "King Black Dragon",
        "Kraken",
        "Kree'Arra",
        "K'ril Tsutsaroth",
        "Mimic",
        "Nightmare",
        "Obor",
        "Sarachnis",
        "Scorpia",
        "Skotizo",
        "Tempoross",
        "The Guantlet",
        "The Correupted Guantlet",
        "Theatre of Blood",
        "Thermonuclear Smoke Devil",
        "TzKal-Zuk",
        "TzTok-Jad",
        "Venenatis",
        "Vetion",
        "Vorkath",
        "Wintertodt",
        "Zalcano",
        "Zulrah"
    ]
    MINIGAMES   : List[str] = [
        "League Points",
        "LMS - Rank",
        "Soul Wars Zeal",
        "Bounty Hunter - Rogue",
        "Bounty Hunter - Hunter"
    ] 
    SKILLS      : List[str] = [
        "Overall",
        "Attack",
        "Defence",
        "Strength",
        "Hitpoints",
        "Ranged",
        "Prayer",
        "Magic",
        "Cooking",
        "Woodcutting",
        "Fletching",
        "Fishing",
        "Firemaking",
        "Crafting",
        "Smithing",
        "Mining",
        "Herblore",
        "Agility",
        "Thieving",
        "Slayer",
        "Farming",
        "Runecraft",
        "Hunter",
        "Construction"
    ]


    @classmethod
    def from_property(cls, property: str) -> str:
        all_properties = [cls.CLUESCROLLS, cls.BOSSES, cls.MINIGAMES, cls.SKILLS]
        for ctype, properties in zip(cls.__annotations__, all_properties):
            if property in properties:
                return ctype.lower()

    @classmethod
    def get_properties_from_category(cls, category: str) -> List[str]:
        for ctype in cls.__annotations__:
            if ctype.lower() == category:
                return getattr(cls, ctype)
