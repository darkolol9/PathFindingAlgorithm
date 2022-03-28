from calendar import c
from textwrap import fill
from time import sleep
from threading import Thread
from tkinter import *


example = [[0,0,0,0,0,0,0,0],
            [[0,0,0,0,0,0,0,0]]]





def findPath(grid,i,j,app):
    
    if (i,j) == (7,7):
        print('solution:')
        grid[i][j] = 'T'
        app.drawMaze()
        return True
    
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    if grid[i][j] == 'W':
        return

    if grid[i][j] == 'T':
        return

    if grid[i][j] == 'H':
        return
    
    for dir in directions:
        grid[i][j] = 'T'
        app.root.after(50,app.drawMaze)
        # color(grid,i,j,'blue')
        if i+dir[0] >= 0 and i+dir[0] <= 7 and j+dir[1] >= 0 and j+dir[1] <= 7:
            if findPath(grid,i+dir[0],j+dir[1],app):
                return True
        else:
            continue

    grid[i][j] = 'H'
    app.root.after(50,app.drawMaze)
    return
    



def buttonClick(grid,app):
    x = Thread(target=lambda x :findPath(grid,0,0,app), args=(1,), daemon=True)
    x.start()


class App:
    def __init__(self,w,h):

        #consts
        self.SIZE = 75
        self.COLOR = None

        #root settings
        self.h,self.w = h,w
        self.root = Tk()
        self.root.title("Path finding algorithm visualization")
        self.root.geometry(f'{w}x{h}')
        self.root.config(bg='dark gray')
        self.butt = Button(self.root,text='findPath',command=lambda : self.root.after(5,lambda :findPath(self.grid,0,0,self)))
        self.butt.pack()


        #the maze canvas
        self.cv = Canvas(self.root,width=self.w,height=self.w,bg='black',cursor='dot')
        self.cv.pack()


        self.grid = [[0] * 8 for _ in range(8)]
        self.tiles = [[(None,None)]*8 for _ in range(8)]

        for i in range(8):
            for j in range(8):
                self.tiles[i][j] = self.cv.create_rectangle(j*self.SIZE,i*self.SIZE,j*self.SIZE + self.SIZE,i*self.SIZE + self.SIZE
                ,fill='beige'),(i,j)

                

        for i in range(8):
            for j in range(8):
                ob = self.tiles[i][j]
                self.cv.tag_bind(ob[0],"<Button-1>",lambda e:self.color(e))
                

        
    def drawMaze(self):
        #needs editing
        # self.cv.delete('all')

        for i in range(8):
            for j in range(8):
                if self.grid[i][j] == 'W':
                    self.cv.create_rectangle(j*self.SIZE,i*self.SIZE,j*self.SIZE + self.SIZE,i*self.SIZE + self.SIZE
                    ,fill='brown')
                elif self.grid[i][j] == 'T':
                    self.cv.create_rectangle(j*self.SIZE,i*self.SIZE,j*self.SIZE + self.SIZE,i*self.SIZE + self.SIZE
                    ,fill='green')
                elif self.grid[i][j] == 'H':
                    self.cv.create_rectangle(j*self.SIZE,i*self.SIZE,j*self.SIZE + self.SIZE,i*self.SIZE + self.SIZE
                    ,fill='orange')
                else:
                    self.cv.create_rectangle(j*self.SIZE,i*self.SIZE,j*self.SIZE + self.SIZE,i*self.SIZE + self.SIZE
                    ,fill='beige')


    def color(self,event,color='brown'):
        current = event.widget.find_withtag("current")[0]
        event.widget.itemconfig(current, fill=color)

        col = int(current - 0.00001)//8
        row = current%8


        if row == 0:
            row = 8


        row -= 1

        self.grid[col][row] = 'W'
       

        


        
     


    def run(self):
        self.root.mainloop()
        return self






if __name__ == "__main__":
    app = App(600,700).run()