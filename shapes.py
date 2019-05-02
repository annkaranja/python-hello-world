class Circle:
    def __init__(self,r):
	    self.r=r
	
    def area(self):
        return 3.142**self.r

    def perimeter(self): 
        return 2*(3.142*self.r)

    print(area())
    print(perimeter()) 


class Square:
	def __init__(self,a):
		self.a=a

	def area(self):
   		return self.a*self.a

	def perimeter(self):
   		return 4*(self.a)  

	print(area())
	print(perimeter())    	


class Rectangle:
	def __init__(self,w,l):
		self.w=w
		self.l=l
	def area(self):
	    return self.w*self.l

	def perimeter(self):
	    return 2*(self.l+self.w)  

	print(area())
	print(perimeter())  



class Sphere:
	def __init__(self,r):
	    self.r=r
 
	# def surface_area(self):
 #        return 4*(3.142*self.r*self.r) 

	def volume(self):
   		return 4/3*(3.142*self.r*self.r*self.r)     

	print(surface_area()) 
	print(volume())   	
		






