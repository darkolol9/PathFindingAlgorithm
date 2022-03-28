from tkinter import *



class App:
    def __init__(self,w,h):

        #consts
        self.SIZE = 40

        #root settings
        self.h,self.w = h,w
        self.root = Tk()
        self.root.title("Path finding algorithm visualization")
        self.root.geometry(f'{w}x{h}')


        #the maze canvas
        self.cv = Canvas(self.root,width=self.w,height=self.w,bg='black')
        self.cv.pack()


        self.grid = [[0] * 8 for _ in range(8)]
        self.tiles = [[] for _ in range(8)]

        for i in range(0,self.SIZE*8,self.SIZE):
            for j in range(0,self.SIZE*8,self.SIZE):
                tile = self.cv.crea
                self.tiles[i].append()

        


    def drawMaze(self):
        #needs editing
        for i in range(0,self.SIZE*8,self.SIZE):
            for j in range(0,self.SIZE*8,self.SIZE):
                tile = self.cv.crea
                self.tiles[i].append()





    def run(self):
        self.root.mainloop()
        return self






if __name__ == "__main__":
    app = App(600,700).run()