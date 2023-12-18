import pyxel

class Ball:
    speed=3
    def move(self):
        self.x += self.vx*Ball.speed
        self.y += self.vy*Ball.speed
        if self.x>=90 or self.x<-90:
            self.vx=self.vx*-1
    def restart(self):
        self.x = pyxel.rndi(0, 199)-100    #0から画面の横幅-1の間
        self.y = 0
        angle = pyxel.rndi(30, 150)    #30度から150度の間
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)


class pad:
    def __init__(self):
        self.padx = pyxel.mouse_x
    def catch(self,ball):
        if  ball.y>195 and self.padx<ball.x+120 and self.padx>ball.x+80:
            return True
        else:
            return False

class App:
    def __init__(self):
        pyxel.init(200,200)
        pyxel.sound(0).set(notes='A2C3',tones='TT',volumes='33',effects='NN',speed=10)
        pyxel.sound(1).set(notes='B1A1G1',tones='TT',volumes='33',effects='NN',speed=10)
        self.padx = 100
        self.score=0
        self.fail=0

        self.balls=[Ball()]
        self.balls[0].restart()
        self.b=Ball()
        self.p=pad()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.p=pad()
        if self.fail>=10:
            return
        for i in self.balls:
            i.move()
            if  self.p.catch(i):
            
                pyxel.play(0,0)
                self.score=100+self.score
                Ball.speed+=0.2
                i.restart()
                if self.score>=1000 and self.score%1000==0 :
                    self.balls.append(Ball())
                    self.balls[-1].restart()
                    Ball.speed=3
                
            elif i.y>195:
                Ball.speed+=0.2
                self.fail+=1
                pyxel.play(0,1)
                i.restart()
            
    def draw(self):
        if self.fail>=10:
            pyxel.text(85,100,"GameOver",0)
            return

        pyxel.cls(7)
        for i in self.balls:
            pyxel.circ(i.x+100,i.y, 10, 6)

        pyxel.rect(self.p.padx-20, 195, 40, 5, 14)
        pyxel.text(10,30,"Score "+str(self.score),0)
        pyxel.text(10,40,"Miss "+str(self.fail),0)

App()