from tkinter import *



class App:
    def __init__(self,w,h):
        #root settings
        self.h,self.w = h,w
        self.root = Tk()
        self.root.title("Path finding algorithm visualization")
        self.root.geometry(f'{w}x{h}')


        #the maze canvas
        self.cv = Canvas(self.root,width=self.w,height=self.w,bg='black')
        self.cv.pack()

        



    def run(self):
        self.root.mainloop()
        return self






if __name__ == "__main__":
    app = App(600,700).run()