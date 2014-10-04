import sys

class Queen:
    x = []

    @staticmethod
    def check(self,k,i):
      for j in range(k):
          if(self.x[j]==i or abs(self.x[j]-i)==abs(j-k)):
              return False
      return True


    def queen(self,k,n):
      for j in range(n):
          if(self.check(k,j)):
              self.x[k]=j
              if(k==n):
                  print "Done!!!"
              else:
                  k = k+1
                  self.queen(k,n)


var= Queen()
var.queen()