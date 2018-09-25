import jwt


class Game:
    def __init__(self, owner):
        self.owner = owner
        self.id = jwt.encode({'name':self.owner}, 'secret', algorithm='HS256').decode("utf-8")
        self.second_player = None
        self.j = ''
        self.j2 = ''
        self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
        lv = 'livre'
        self.pos1, self.pos2, self.pos3, self.pos4, self.pos5, self.pos6, self.pos7, self.pos8, self.pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
        self.jogada = 0
        self.turnos = 1
        self.vencedor = ''

    def to_json(self):
        return {
            'owner': self.owner,
            'id': self.id,
            'second_player': self.second_player
        }

    def make_play(self, numero_quadrado, player):
        if player == 1:
            return self.atualizar_jogadas_j1(int(numero_quadrado))
        else:
            return self.atualizar_jogadas_j2(int(numero_quadrado))

    def atualizar_jogadas_j1(self, jogada):
        if jogada == 1:
            self.p1 = self.owner
            self.pos1 = 'ocupada'
        elif jogada == 2:
            self.p2 = self.owner
            self.pos2 = 'ocupada'
        elif jogada == 3:
            self.p3 = self.owner
            self.pos3 = 'ocupada'
        elif jogada == 4:
            self.p4 = self.owner
            self.pos4 = 'ocupada'
        elif jogada == 5:
            self.p5 = self.owner
            self.pos5 = 'ocupada'
        elif jogada == 6:
            self.p6 = self.owner
            self.pos6 = 'ocupada'
        elif jogada == 7:
            self.p7 = self.owner
            self.pos7 = 'ocupada'
        elif jogada == 8:
            self.p8 = self.owner
            self.pos8 = 'ocupada'
        elif jogada == 9:
            self.p9 = self.owner
            self.pos9 = 'ocupada'

        ganhou = self.checar_vencedor()
        if ganhou:
            return ganhou
        else:
            return [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9]

    def atualizar_jogadas_j2(self, jogada):
        if jogada == 1:
            self.p1 = self.second_player
            self.pos1 = 'ocupada'
        elif jogada == 2:
            self.p2 = self.second_player
            self.pos2 = 'ocupada'
        elif jogada == 3:
            self.p3 = self.second_player
            self.pos3 = 'ocupada'
        elif jogada == 4:
            self.p4 = self.second_player
            self.pos4 = 'ocupada'
        elif jogada == 5:
            self.p5 = self.second_player
            self.pos5 = 'ocupada'
        elif jogada == 6:
            self.p6 = self.second_player
            self.pos6 = 'ocupada'
        elif jogada == 7:
            self.p7 = self.second_player
            self.pos7 = 'ocupada'
        elif jogada == 8:
            self.p8 = self.second_player
            self.pos8 = 'ocupada'
        elif jogada == 9:
            self.p9 = self.second_player
            self.pos9 = 'ocupada'

        ganhou = self.checar_vencedor()
        if ganhou:
            return ganhou
        else:
            return [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9]

    def checar_vencedor(self):
        if self.p1 == self.owner and self.p2 == self.owner and self.p3 == self.owner or \
                self.p1 == self.owner and self.p4 == self.owner and self.p7 == self.owner or \
                self.p1 == self.owner and self.p5 == self.owner and self.p9 == self.owner or \
                self.p2 == self.owner and self.p5 == self.owner and self.p8 == self.owner or \
                self.p3 == self.owner and self.p5 == self.owner and self.p7 == self.owner or \
                self.p3 == self.owner and self.p6 == self.owner and self.p9 == self.owner or \
                self.p4 == self.owner and self.p5 == self.owner and self.p6 == self.owner or \
                self.p7 == self.owner and self.p8 == self.owner and self.p9 == self.owner:
            return True

        if self.p1 == self.second_player and self.p2 == self.second_player and self.p3 == self.second_player or \
                self.p1 == self.second_player and self.p4 == self.second_player and self.p7 == self.second_player or \
                self.p1 == self.second_player and self.p5 == self.second_player and self.p9 == self.second_player or \
                self.p2 == self.second_player and self.p5 == self.second_player and self.p8 == self.second_player or \
                self.p3 == self.second_player and self.p5 == self.second_player and self.p7 == self.second_player or \
                self.p3 == self.second_player and self.p6 == self.second_player and self.p9 == self.second_player or \
                self.p4 == self.second_player and self.p5 == self.second_player and self.p6 == self.second_player or \
                self.p7 == self.second_player and self.p8 == self.second_player and self.p9 == self.second_player:
            return True
        return False
