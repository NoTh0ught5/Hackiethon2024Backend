from Skills import AttackSkill
class Player_Controller:
    def __init__(self, xCoord, yCoord, HP, direction):
        self.primarySkill =""
        self.secondarySkill = ""
        self.lightAtk = AttackSkill(0, 2, 5, 1, True)
        self.heavyAtk = AttackSkill(2, 4, 10, 2, True)
        
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.moves = []
        self.blocking = False
        self.hp = HP
        
        #current stun duration
        self.stun = 0
        self.midair = False
        #direction player is facing
        self.direction = direction
        
        self.moveNum = 0
        
        #for testing
        #player scripts will append moves to this
        self.moveList = [("move", (1,1)), ("move",(1,1)), ("move", (-1,0)), ("move", (1,0)), 
                         ("attack", "light"), ("attack", "light"), ("attack", "light")]
    def action(self):
        if self.moveNum < len(self.moveList):
            # print(f"{self.moveNum} , {self.moveList[self.moveNum]}")
            return self.moveList[self.moveNum]
        return ("NoMove")