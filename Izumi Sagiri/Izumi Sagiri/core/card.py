class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        # 實現遊戲的邏輯
        pass

    def calculate_damage(card1, card2):
            damage = 0
            status = ''
            
            if card1 == '火' and card2 == '冰' or card1 == '冰' and card2 == '火':
                    damage = 2  # 基础伤害
                    status = '融化'
                    
            elif card1 == '火' and card2 == '火':
                   damage = 1  # 基础伤害
                   status = '超载'
                   
                   return damage, status

game = Game()
