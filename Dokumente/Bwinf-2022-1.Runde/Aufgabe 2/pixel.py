
class Pixel(object):
    def __init__(self):
        self.__active = False
        self.__color = None
        self.__pos_x = None
        self.__pos_y = None
        self.__neg_x = None
        self.__neg_y = None

    def set_color(self,new_color):
        self.__color=new_color

    def set_pos_x(self,x):
        self.__pos_x = x

    def set_pos_y(self,y):
        self.__pos_y = y

    def set_neg_x(self,x):
        self.__neg_x = x

    def set_neg_y(self,y):
        self.__neg_y = y


    def set_all(self,pos_x,pos_y,neg_x,neg_y,new_color):
        self.__neg_y = neg_y
        self.__neg_x = neg_x
        self.__pos_y = pos_y
        self.__pos_x = pos_x
        self.__color = new_color

    def set_active_true(self):
        self.__active = True
    
    def set_active_false(self):
        self.__active = False
            
    def get_active(self):
        return self.__active
    

    def get_color(self):
        return self.__color
    
    def get_pos_x(self):
        return self.__pos_x

    def get_pos_y(self):
        return self.__pos_y

    def get_neg_x(self):
        return self.__neg_x

    def get_neg_y(self):
        return self.__neg_y 

    def get_growth(self):
        return self.__growth

    def get_all(self):
        return self.__neg_y, self.__neg_x, self.__pos_y, self.__pos_x, self.__color,self.active
