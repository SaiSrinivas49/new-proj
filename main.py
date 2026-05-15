class Player:
    def __init__(self,name,country,role):
        self.name = name
        self.country = country
        self.role = role
    def __str__(self):
        return f'Name:{self.name}, Country:{self.country}, Role:{self.role}'
    
class Team:
    def __init__(self,name):
        players = []
        self.players = players
        self.name = name
    def add_player(self,Player):
        self.players.append(Player)
    def remove_player(self,Player):
        self.players.remove(Player)

    def __str__(self):
        return f'Team Name:{self.name}, Players:{[str(player.name) for player in self.players]}'
    