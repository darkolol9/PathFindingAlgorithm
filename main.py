from calendar import c
from textwrap import fill
from tkinter import *



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


        #the maze canvas
        self.cv = Canvas(self.root,width=self.w,height=self.w,bg='black',cursor='dot')
        self.cv.pack()


        self.grid = [[0] * 8 for _ in range(8)]
        self.tiles = [[(None,None)]*8 for _ in range(8)]

        for i in range(8):
            for j in range(8):
                self.tiles[i][j] = self.cv.create_rectangle(i*self.SIZE,j*self.SIZE,i*self.SIZE + self.SIZE,j*self.SIZE + self.SIZE
                ,fill='beige'),(i,j)

                

        for i in range(8):
            for j in range(8):
                ob = self.tiles[i][j]
                self.cv.tag_bind(ob[0],"<Button-1>",self.color)
                

        
    def drawMaze(self):
        #needs editing
        for i in range(0,self.SIZE*8,self.SIZE):
            for j in range(0,self.SIZE*8,self.SIZE):
                tile = self.cv.crea
                self.tiles[i].append()


    def color(self,event,color='brown'):
        current = event.widget.find_withtag("current")[0]
        event.widget.itemconfig(current, fill=color)

        col = round((current - 0.001)//8)
        row = current%8

        if row == 0:
            row = 8

        row -= 1


        print(row,col)
        self.grid[row][col] = 'W'
       

        for r in self.grid:
            print(r)


        
     


    def run(self):
        self.root.mainloop()
        return self






if __name__ == "__main__":
    app = App(600,700).run()