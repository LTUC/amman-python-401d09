def insert_shift_array(list, value):
   """
   Insert a value into a list at index of middle of list 

   Args:
     list : list of Integers
     value : Integer 

    return :
     list : list of int with value added to the middle of the list 

   """
   
   if len(list)%2 ==0:
        mid = len(list)//2
   else : 
        mid = len(list)//2 +1

   return list.insert(mid,value)    


   


