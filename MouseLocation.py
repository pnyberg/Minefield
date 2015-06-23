from tkinter import *
from Mineboard import Mineboard

class MouseLocation():
   def __init__( self, master ):
      self.master = master
      self.frame = Frame(master)
      self.frame.pack( expand = YES, fill = BOTH )
      self.frame.master.title( "Demonstrating Mouse Events" )
      self.frame.master.geometry(  "275x100" )

      self.canvas = Canvas(self.frame, bd=0)
      self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

      self.canvas.bind( "<Button-1>", self.buttonPressed )
      self.canvas.bind( "<ButtonRelease-1>", self.buttonReleased )

      self.update()

   def buttonPressed( self, event ):
      print( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

   def buttonReleased( self, event ):
      print( "Released at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

   def update( self ):
      self.canvas.create_rectangle(50, 20, 150, 80, fill="#476042") 

def main():
   root = Tk()
   assHole = MouseLocation(root)
   root.mainloop()

# I have no idea what I'm doing :D
if __name__ == "__main__":
   main()

