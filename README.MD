Still under construction.

## Hiscores API

###### Importing and Initializing the Hiscores API:
```python
from o7scape import PersonalHiscores
player = PersonalHiscores('zezima', account_type='normal')

# or import AccountModes for ease with built in types

player = PersonalHiscores('zezima', account_type=PersonalHiscores.NORMAL)
```

###### Accessing categories
```python
#Skills
player.skills['agility']

#Bosses
player.bosses['Commander Zilyana']

#Cluescrolls
player.cluescrolls['Clue Scrolls (all)']

#Minigames
player.minigames['soul wars zeal']

```

###### Iter any category
```python

#Skills Views
for skill in player.skills:
    #Attributes
    skill.icon, skill.name, skill.rank, skill.level, skill.xp

    #Functions
    skill.xp_to_99(), skill.xp_to_next_level()


#Minigame Views (Cluescrolls, Minigames, Bosses)
for clue in player.cluescrollls:
    #Attributes
    clue.icon, clue.name, clue.rank, clue.score

```

###### Comparing Players
```python
zezima = PersonalHiscores('zezima', account_type=PersonalHiscores.NORMAL)
hiddy = PersonalHiscores('hiddy', account_type=PersonalHiscores.NORMAL)

#By Overall
zezima > hiddy

#By a specific skill
zezima.skills['crafting'] > hiddy.skills['crafting']

#By a minigame, cluescroll, or boss
zezima.bosses['kraken'] > hiddy.bosses['kraken']

```