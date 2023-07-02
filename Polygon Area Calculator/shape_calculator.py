class Rectangle:

  def __init__(self,width,height):
    self.width = width
    self.height = height 
    self.shap = ""
  def __str__(self) -> str:
    return f"Rectangle(width={self.width}, height={self.height})"


  def set_height(self, height):
    self.height = height

  def set_width(self, width):
    self.width = width
    
  def get_area(self):
    return self.height * self.width
    
  def get_perimeter(self):
    return  2* self.height + 2*self.width

  def get_diagonal(self):
    return  ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width >50 or self.height >50:
      return "Too big for picture."
    else:
      for i in range (0,self.height):
        self.shap += "*" * self.width +"\n"

    return self.shap    
     
        

  def get_amount_inside(self , object):
    height_counter,width_counter, total_counter = 0 ,0 ,0


    if self.width < object.width  or self.height < object.width:
      return 0 
    else :
      width_counter = int(self.width / object.width)
      height_counter = int(self.height / object.height)
      total_counter = width_counter * height_counter
      return total_counter

    
    


class Square(Rectangle):


  def __init__(self,side):
    self.height = int(side) 
    self.width = int(side)
    self.shap = ""

  def __str__(self) -> str:
    return  f"Square(side={self.width})"
  

  def set_side(self, side):
    self.height = int(side) 
    self.width = int(side)

  
