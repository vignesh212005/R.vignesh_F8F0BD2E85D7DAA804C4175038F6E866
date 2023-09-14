class Player:
     def play(self):
        print("The player isplaying cricket.")
class Batsman (Player):
  def play(self):
      print("The batsman is batting.")

class Bowler (Player):
  def play(self):
     print("The bowler is bowling.")

#Bowler classes
batsman =Batsman()
bowler =Bowler()

object ()
batsman.play()
bowler.play()