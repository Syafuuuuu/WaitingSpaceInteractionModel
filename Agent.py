class Agent:
    def __init__(self, name, agent_X, agent_Y, Ha, Sd, Fe, Ex, Op, Nu, Eh, Nc, Ni, HobbArr, IntArr, LangArr, RaceArr, RelArr) -> None:
        self.name = name
        self.posX = agent_X
        self.posY = agent_Y
        self.Ha = Ha
        self.Sd = Sd
        self.Fe = Fe
        self.Ex = Ex
        self.Op = Op
        self.Nu = Nu
        self.Eh = Eh
        self.Nc = Nc
        self.Ni = Ni
        self.Dh = 0.5
        self.Ds = 0.5
        self.Df = 0.5
        self.Li = 0.5
        self.HobbArr = HobbArr
        self.IntArr = IntArr
        self.LangArr = LangArr
        self.RaceArr = RaceArr
        self.RelArr = RelArr
        
    # def printInfo(self):
    #     print("Name: " , self.name)
    #     print("PosX: " , self.posX)
    #     print("PosY: " , self.posY)
    #     print("Ha: " , self.Ha)
    #     print("Sd: " , self.Sd)
    #     print("Fe: " , self.Fe)
    #     print("Ex: " , self.Ex)
    #     print("Op: " , self.Op)
    #     print("Nu: " , self.Nu)
    #     print("Eh: " , self.Eh)
    #     print("Nc: " , self.Nc)
    #     print("Ni: " , self.Ni)