class bird:
    def __init__(self):
      print ("bird is ready")
    def whoisthis(self):
       print ("bird")
    def swim (self):
       print("swim faster")
class pei (bird):
   def __init__(self):
      super().__init__()
      print ("peinguin is ready")
   def whoisthis(self):
       print ("peinguin")
   def run(self):
      print("run")
peppy = pei()
peppy.whoisthis()
peppy.swim()
peppy.run