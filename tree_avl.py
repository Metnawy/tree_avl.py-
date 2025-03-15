class tree_avl:

    class tree_node:
        def __init__(self,data,container):
            self.data=data
            self.left=None
            self.right=None
            self.height=1
            self.container=container

        @property
        def data(self):
           return self._data
        @data.setter
        def data(self,data):
            if isinstance(data,(int,float)):
                self._data=data
            else:
                raise TypeError("the input data should be numeric")
            
        def __repr__(self):
            return f"{self.data}"
            
    

    def __init__(self,data=None):
        self.root=self.tree_node(data,self) if  data  else None
        if self.root is None:
            self._size=0
        else:
            self._size=1



    def insert(self,data):
        if not isinstance(data,(int,float)):
            raise TypeError("the ineration should be numeric value")
        else:
            self.root=self._insert(self.root,data)
    def _insert(self,node,data):
          
          if not node:
            node=self.tree_node(data,self)
            self._size+=1
           
            return node
          if data<node.data:
             node.left=self._insert(node.left,data)
             self.height_node(node.left)
        
          elif  data >node.data:
              node.right=self._insert(node.right,data)
              self.height_node(node.right)
          else:
              return node 
          
          length_factor=self.height_node(node.left)-self.height_node(node.right)

          if length_factor>1 and data<node.left.data:
              node=self._rotate_right(node)
              
          elif length_factor>1 and data>node.left.data:
                node.left=self._rotate_left(node.left)
                node=self._rotate_right(node)

          elif length_factor<-1 and data<node.right.data:
              node.right=self._rotate_right(node.right)
              node=self._rotate_left(node)

          elif length_factor<-1 and data>node.right.data:
             node=self._rotate_left(node)

              
          node.height=self.height_node(node)
          return node 


    def _rotate_right(self,node):
        #tracking all concerned & critical points
        old_root=node
        new_root=node.left
        shifting_part=new_root.right

        new_root.right=old_root
        old_root.left=shifting_part

        self.height_node(new_root)
        self.height_node(old_root)

        return new_root


    def _rotate_left(self,node):
        #tracking all concerned & critical points 
        old_root=node
        new_root=node.right
        shifting_part=new_root.left 

        new_root.left=old_root
        old_root.right=shifting_part

        self.height_node(new_root)
        self.height_node(old_root)

        return new_root

    def height_node(self,node):
        if isinstance(node,(tree_avl.tree_node,type(None))) :
            if not node :
                return 0
            else:
              node.height=1+max(self.height_node(node.left),self.height_node(node.right))
      
            return node.height 
        else:
            raise TypeError
    
                  
    def delete(self,data):
        
        def _delete(pre_node,node,data):
            
            if not node:
                return
            
            if node.data==data:
                self._size-=1
                node_to_delete=node
                if node.right:
                    if node.right.left:
                        _smallest_of_larger(pre_node,node,node_to_delete)
                        length_factor=self.height_node(node.left)-self.height_node(node.right)
                        if length_factor>1 :
                           node=self._rotate_right(node)
                           self.height_node(node)
                        elif length_factor<-1:
                            node=self._rotate_left(node)
                            self.height_node(node)
                    else:
                        concerned=node.right
                        node_to_delete.data=concerned.data
                        concerned=None###
                        node.right=None
                        length_factor=self.height_node(node.left)-self.height_node(node.right)
                        if length_factor>1 :
                           node=self._rotate_right(node)
                        self.height_node(node)
                elif node.left:
                    if node.left.right:
                        _largest_of_smaller(pre_node,node,node_to_delete)
                        length_factor=self.height_node(node.left)-self.height_node(node.right)
                        if length_factor>1 :
                           node=self._rotate_right(node)
                           self.height_node(node)
                        elif length_factor<-1:
                            node=self._rotate_left(node)
                            self.height_node(node)
                    else:
                        concerned=node.left
                        node_to_delete.data=concerned.data
                        concerned=None##
                        node.left=None
                        length_factor=self.height_node(node.left)-self.height_node(node.right)
                        if length_factor<-1 :
                           node=self._rotate_right(node)
                        self.height_node(node)
                else:
                
                    
                    if pre_node:
                        if pre_node.right==node:
                           pre_node.right=None
                        else:
                           pre_node.left=None
                        

                        length_factor=self.height_node(pre_node.left)-self.height_node(pre_node.right)
                        if length_factor<-1 :
                           pre_node=self._rotate_left(pre_node)
                        elif length_factor>1:
                             pre_node=self._rotate_right(pre_node)
                        self.height_node(pre_node)
                    else:
                        self.root=None
                        self.height_node(self.root)
                     

                 
            elif data<node.data:
                _delete(node,node.left,data)
                length_factor=self.height_node(node.left)-self.height_node(node.right)
                if length_factor<-1 :
                    node=self._rotate_left(node)
                elif length_factor>1:
                    node=self._rotate_right(node)
                self.height_node(node)
            elif data>node.data:
                _delete(node,node.right,data)
                length_factor=self.height_node(node.left)-self.height_node(node.right)
                if length_factor>1 :
                    node=self._rotate_right(node)
                elif length_factor<-1:
                    node=self._rotate_left(node)
                self.height_node(node)

        def _smallest_of_larger(pre_node,node_concerned,node_to_delete):

            def recusrsion_through(pre_node,node_concerned,node_concerned_left,node_to_delete):
                
                if node_concerned_left:
                   recusrsion_through(node_concerned,node_concerned_left,node_concerned_left.left,node_to_delete)
                   #re_balancing 
                   
                else:
                    required_data=node_concerned.data
                    node_to_delete.data=required_data
                    if node_concerned.right:
                       pre_node.left=node_concerned.right
                  
                       length_factor=self.height_node(pre_node.left.left)-self.height_node(pre_node.left.right)
                       if length_factor<-1 :
                          pre_node.left=self._rotate_left(pre_node.left)
                          self.height_node(pre_node.left)
                       elif length_factor>1:
                            pre_node.left=self._rotate_right(pre_node.left)
                       self.height_node(node_concerned)

                    else:
                         pre_node.left=None
          
              
                length_factor=self.height_node(pre_node.left)-self.height_node(pre_node.right)
                if length_factor<-1 :
                       pre_node=self._rotate_left(pre_node)
                       self.height_node(pre_node)
                elif length_factor<-1:
                    pre_node=self._rotate_right(pre_node)
                    self.height_node(pre_node)
          

            recusrsion_through(pre_node,node_concerned,node_concerned.right,node_to_delete)

        def _largest_of_smaller(pre_node,node_concerned,node_to_delete):

            def recusrsion_through(pre_node,node_concerned,node_concerned_right,node_to_delete):

                if node_concerned_right:
                   recusrsion_through(node_concerned,node_concerned_right,node_concerned_right.right,node_to_delete)
                   #re_balancing 
                   
                else:
                    required_data=node_concerned.data
                    node_to_delete.data=required_data
                    if node_concerned.left:
                       pre_node.right=node_concerned.left

                       length_factor=self.height_node(pre_node.right.left)-self.height_node(pre_node.right.right)
                       if length_factor<-1 :
                          pre_node.right=self._rotate_left(pre_node.right)
                          self.height_node(pre_node.right)
                       elif length_factor>1:
                            pre_node.right=self._rotate_right(pre_node.right)
                       self.height_node(pre_node.right)
                    else:
                         pre_node.right=None
                
              
                
                length_factor=self.height_node(pre_node.left)-self.height_node(pre_node.right)
                if length_factor>1 :
                      pre_node=self._rotate_right(pre_node)
                      self.height_node(pre_node)

                elif length_factor<-1:
                    pre_node=self._rotate_left(pre_node)
                    self.height_node(pre_node)
             
            recusrsion_through(pre_node,node_concerned,node_concerned.left,node_to_delete)

        _delete(self.root,self.root,data)
        

    def size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def search(self,data):
        if isinstance(data,(int,float)):
            pass
        else:
            raise TypeError

        def _search(node,data):
            concerned=None
            if not node:
                return concerned
            
            if node.data==data:
                concerned=node
                return node
            elif data<node.data:
                concerned=_search(node.left,data)
                return concerned

            else:
                concerned=_search(node.right,data)
                return concerned

            

        return _search(self.root,data)

    def in_order_traversal(self,node):
      if isinstance(node,tree_avl.tree_node) and node.container==self:
            pass
      else:
            raise TypeError
      l=[]
      def _in_order_traversal(node,l):
        
        if not node:
            
            return 
        _in_order_traversal(node.left,l)
        l.append(node.data)
        _in_order_traversal(node.right,l)

      _in_order_traversal(node,l)
      return l

    def pre_order_traversal(self,node):
        if isinstance(node,tree_avl.tree_node) and node.container==self:
            pass
        else:
            raise TypeError
        the_list=[]
        def _pre_order_traversal(node,the_list):
            if not node:
                return
            the_list.append(node.data)
            _pre_order_traversal(node.left,the_list)
            _pre_order_traversal(node.right,the_list)

        _pre_order_traversal(node,the_list)
        return the_list 

    def post_order_traversal(self,node):
        if isinstance(node,tree_avl.tree_node) and node.container==self:
            pass
        else:
            raise TypeError
        the_list=[]
        def _post_order_traversal(node,the_list):
            if not node:
                return 
            _post_order_traversal(node.left,the_list)
            _post_order_traversal(node.right,the_list)
            the_list.append(node.data)
        _post_order_traversal(node,the_list)
        return the_list


    def level_traversal(self,node):
        if not (isinstance(node,tree_avl.tree_node) and node.container==self):
            raise TypeError

        nodes_list=[node]
        data_list=[]
        while nodes_list:
            concerned=nodes_list.pop(0)
            data_list.append(concerned.data)
            if concerned.left:
                nodes_list.append(concerned.left)
            if concerned.right:
                nodes_list.append(concerned.right)
        return data_list

    def __repr__(self) -> str:
        curser=self.root
        def helper(node,level,prefix,factor):
            if not node:
                return 
            print(" "*factor*level+prefix+":"+str(node.data))
            helper(node.left,level+1,"L",factor+1)
            helper(node.right,level+1,"R",factor+1)
        helper(self.root,1,"ROOT",1)
        return""

        

    def min(self):
        curser=self.root
        while curser.left:
              curser=curser.left
        return curser.data
    
    def max(self):
        curser=self.root
        while curser.right:
            curser=curser.right
        return curser.data

    def __len__(self):
        return self._size

    def __iter__(self):
        node=self.root
        nodes_list=[node]
        
        while nodes_list:
            concerned=nodes_list.pop(0)
            yield concerned.data
            if concerned.left:
                nodes_list.append(concerned.left)
            if concerned.right:
                nodes_list.append(concerned.right)
        

import random 
random_list = []
for _ in range(10):
    random_number = random.randint(1,100)
    if random_number not in random_list:
       random_list.append(random_number)
  
print(random_list)

new_tree=tree_avl()



for i in random_list:
    new_tree.insert(i)
print("\n")
print(new_tree.in_order_traversal(new_tree.root))
print(new_tree.pre_order_traversal(new_tree.root))
print(new_tree.post_order_traversal(new_tree.root))
print(new_tree.size())
print(new_tree.height_node(new_tree.root))
print(new_tree.max(),new_tree.min())
print(new_tree.search(5))
print(new_tree.level_traversal(new_tree.root))
for i in new_tree:
    print(i)
x=random_list[0]
print(new_tree)
print(x)
print(new_tree._size)
new_tree.delete(x)
print(new_tree)
print(new_tree._size)
def validation(s):
    if isinstance(s,str) and 1<=len(s)<=100:
      
        counter=0
        length=len(s)
        if length <2:
            return "valid"
        for i in s:
            if i  in ("}",")","]"):
                if   counter==0:
                     return "invalid"

            
            if  i=="}":
                if s[counter-1]=="{":
                   counter+=1
                elif s[(length-(counter+1))]=="{":
                    counter+=1
                else:
                    return "invalid"
            elif i==")":
                if s[counter-1]=="(":
                    counter+=1
                elif s[(length-(counter+1))]=="(":
                    counter+=1
                else:
                    return "invalid"
            elif i=="]":
                 if s[counter-1]=="[":
                    counter+=1
                 elif s[(length-(counter+1))]=="[":
                    counter+=1
                 else:
                    return "invalid"
    
            elif i=="{":
                 if s[counter+1]=="}":
                    counter+=1
                 elif s[-1*(counter+1)]=="}":
                    counter+=1
                 else:
                    return"invalid"

            elif i=="(":
                 if s[counter+1]==")":
                    counter+=1
                 elif s[-1*(counter+1)]==")":
                    counter+=1
                 else:
                    return"invalid"

              
            else:
                if s[counter+1]=="]":
                    counter+=1
                
                elif s[-1*(counter+1)]=="]":
                    counter+=1
                else:
                    return "invalid"

        return f"{s} is valid string according the constraints"


    else:
        raise Exception 

def unique_consective_lists(the_list,limit,divisor):

    if isinstance(the_list,list) and isinstance(limit,int) and isinstance(divisor,int):
        if 1<=len(the_list)<=200 and 1<=divisor<=200 and 1<=limit<=len(the_list):
            uniquness_no=0
            limit_counter=0
            sublist_count=0

            for i in the_list:
                if isinstance(i,int) :
                  if limit_counter<=limit and i%divisor==0:
                    limit_counter+=1
                    sublist_count+=1
                    
                    uniquness_no+=sublist_count
                    print(limit_counter,sublist_count,uniquness_no)
                    if limit_counter>limit:
                        limit_counter=0
                        sublist_count=0
                
                  else:
                    limit_counter=0
                    sublist_count=0
                else:
                    raise TypeError("the list should have intgers only") 

            return uniquness_no

        else:
            raise IndexError
    else:
        raise TypeError



    print(i*7+3481)

import copy
class sorted_list_array:
    # sorted list of numeric (intgers,float)

    def __init__(self):
        
        self._list=[]
        self.the_list=[]
    @property
    def the_list(self):
            return self._list
    @the_list.setter
    def the_list(self,data):
            if isinstance(data,list):
            
                if all( isinstance(i,(int,float)) for i in data):
                    self._list=data
                else:
                   raise TypeError("all elements of the list you asign as whole bunch of data to self._list should be numeric ")
            else:
                raise TypeError("it must be list to do direct assigning ")

        

    def insert_first(self,data):
        if isinstance(data,(int,float)):
            self._list.append(0)
            x=len(self)
            for i in range(1,x+1):
              if i!=x: 
                self._list[-i]=self._list[-(i+1)]
              else:
                self._list[-i]=data
        else:
            raise TypeError

    def insert_last (self,data):
        if isinstance(data,(int,float)):
            self._list.append(data)

        else:
            raise TypeError

    def insert_index(self,data,index):
        if isinstance(data,(int,float)) and isinstance(index,int):
          if 0<=index<=len(self):
             self._list.append(0)

             x=len(self._list[index:])

             for i in range(1,x+1):
                if i!=x:
                    self._list[-i]=self._list[-(i+1)]
                else:
                    self._list[-i]=data

          else:
            raise IndexError   
        else:
            raise TypeError

    def insert_before_data(self,data,new_data):
        if isinstance(data,(int,float)):
           index=self.search(data)
           if index or index==0: 
               self.insert_index(new_data,index)

           else:
               raise ValueError("this value doesn't exist in the array to use as refernce")

        else:
            raise TypeError("the data we should use as reference to insert ..should be int,float")

    def insert_after_data(self,data,new_data):
        if isinstance(data,(int,float)):
           index=self.search(data)
           if index or index==0:
               if index==len(self)-1:
                  self._list.append(new_data)
               else:
                  self.insert_index(new_data,index)

           else:
               raise ValueError("this value doesn't exist in the array to use as refernce")

        else:
            raise TypeError("the data we should use as reference to insert ..should be int,float")
    

    def delete_index(self,index):
        x=len(self)
        if x==0:
            print("the list already empty nothing to delete")
            return 
   
        if isinstance(index,int) and 0<=index<=x-1:
            new_list=[]
            for i in  range(x):
                if i!=index:
                    new_list.append(self._list[i])
            self._list=new_list
        else:
            print(f"revise the index {index}..it should be intger between o and {x} ")

    def delete_data(self,data):
        to_delete_index=self.search(data)
        if to_delete_index or to_delete_index==0:
           self.delete_index(to_delete_index)

    def delete_before_data(self,data):
        to_delete_index=self.search(data)
        if to_delete_index :
           self.delete_index(to_delete_index-1)
        


    def delete_after_data(self,data):
        to_delete_index=self.search(data)
        if to_delete_index or to_delete_index==0:
           if to_delete_index+1<=len(self)-1:
              self.delete_index(to_delete_index+1)
           else:
               print("we can't delete anything after the last element")
        else:
            print("this datat doesn't exist")
    
    def search(self,data):
        #this method return the index if exits ..else retun none
        if isinstance(data,(int,float)):
            if len(self)==0:
                return None
            else:
                
                x=len(self)

                for i in range(x):
                    if self._list[i]==data:
                        return i
                return None

        else:
            return None

    def search_by_index(self,index):
        '''
        objective: searching specific data ..return it using the indecies ...return none if it was empty list or index out of range 
        '''
        x=len(self)
        if x==0:
            return None
        if isinstance(index,int) and 0<=index<=x-1:
           return self._list[index]
        else:
            return None 

    def merge_without_change(self,second):

        if isinstance(second,sorted_list_array):
            first_list=copy.deepcopy(self._list)
            second_list=copy.deepcopy(second._list)
            new=first_list+second_list
            return new
        else:
            raise TypeError


    def __add__(self,second):
        if isinstance(second,sorted_list_array):
            first_list=copy.deepcopy(self._list)
            second_list=copy.deepcopy(second._list)
            new=first_list+second_list
            return new 
        else:
            raise TypeError

    def merge_with_changes(self,second):
        #merging the sorted_list_bubble objects with changing the self.list 
        if isinstance(second,sorted_list_array):
            the_second=copy.deepcopy(second._list)
            self._list=self._list+the_second
            return self._list

        else:
            raise TypeError

    def swap_elements_by_index(self,indx1,indx2):
        '''
        objectives:swapping elements usin indices as references to that elements
        '''
        if isinstance(indx1,int) and isinstance(indx2,int):
            x=len(self)
            if 0<=indx1<=x-1 and 0<=indx2<=x-1:
                first=self._list[indx1]
                second=self._list[indx2]
                self._list[indx1],self._list[indx2]=second,first

            else:
                raise IndexError

        else:
            raise TypeError

    def sort_ascending(self):
        def helper(self,index):
            if index==0:
                return
            else:
               
                
                while index>0:
                    if self._list[index]<self._list[index-1]:
                        self._list[index],self._list[index-1]=self._list[index-1],self._list[index]
                        index-=1
                    else:
                        return
        x=len(self)
        if x==0:
            return self
        if x==1:
            return self
        for i in range(x):
            
            if i!=(x-1):
                if self._list[i]>self._list[i+1]:
                    self._list[i],self._list[i+1]=self._list[i+1],self._list[i]
                    helper(self,i)
                  
        return self

    def sort_descending(self):
        
        def helper(self,index):
            if index==0:
                return
            else:
               
                
                while index>0:
                    if self._list[index]>self._list[index-1]:
                        self._list[index],self._list[index-1]=self._list[index-1],self._list[index]
                        index-=1
                    else:
                        return
        x=len(self)
        if x==0:
            return self
        if x==1:
            return self
        for i in range(x):
            
            if i!=(x-1):
                if self._list[i]<self._list[i+1]:
                    self._list[i],self._list[i+1]=self._list[i+1],self._list[i]
                    helper(self,i)
                  
        return self

    def reverse_with_changes(self):
        x=len(self)//2

        for i in range(x):
            self._list[i],self._list[-(i+1)]=self._list[-(i+1)],self._list[i]

        return self
           

    def reverse_no_changes(self):
        the_list=copy.deepcopy(self._list)
        x=len(the_list)//2

        for i in range(x):
            the_list[i],the_list[-(i+1)]=the_list[-(i+1)],the_list[i]

        return the_list


    def no_elements_existance(self):
        the_list={}
        for i in self._list:
            if i in the_list.keys():
                the_list[i]=the_list[i]+1
            else:
                the_list[i]=1
        return the_list 

    def sort_ascending_recursive(self):
        if 0<=len(self)<=1:
            return self
        
        def swap_merge(list,left_side,right_side):
                def swap_left(list,left_cursor,right_cursor):
                  if left_cursor==right_cursor:
                    return 
                  else:
                    if list[right_cursor-1]<list[right_cursor]:
                        return
                    else:
                        list[right_cursor-1],list[right_cursor]=list[right_cursor],list[right_cursor-1]
                        swap_left(list,left_cursor,right_cursor-1)
                        swap_right(list,right_cursor,right_last)
                        
                def swap_right(list,left_cursor,right_cursor):
                    if left_cursor==right_cursor:
                        return
                    else:
                        if list[left_cursor]<=list[left_cursor+1]:
                            return 
                        else:
                            list[left_cursor],list[left_cursor+1]=list[left_cursor+1],list[left_cursor]
                            swap_right(list,left_cursor+1,right_last)
                            swap_left(list,left_first,left_cursor)
                if isinstance(left_side,int):
                    left_first,left_last=left_side,left_side
                    
                else:
                    left_first,left_last=left_side[0],left_side[1]
                    
                if isinstance(right_side,int):
                    right_first,right_last=right_side,right_side
                else:
                    
                   right_first,right_last=right_side[0],right_side[1]
              
                
                if list[left_last]>list[right_first]:
                    list[left_last],list[right_first]=list[right_first],list[left_last]
                    swap_right(list,right_first,right_last)
                    swap_left(list,left_first,left_last)
                    
                x=[left_first,right_last]
                
                return x
          
        def dividing(list,first_index,last_index,size):
            if first_index==last_index:
               
                
                return first_index
            else:
              mid=(first_index+last_index)//2
              
              left_side=dividing(list,first_index,mid,(mid-first_index)+1)
              right_side=dividing(list,mid+1,last_index,last_index-mid)
            
            
            return  swap_merge(list,left_side,right_side)

        
        dividing(self._list,0,len(self)-1,len(self))
        return self

    def sort_descending_recursive(self):
        if 0<=len(self)<=1:
            return self
        
        def swap_merge(list,left_side,right_side):
                def swap_left(list,left_cursor,right_cursor):
                  if left_cursor==right_cursor:
                    return 
                  else:
                    if list[right_cursor-1]>=list[right_cursor]:
                        return
                    else:
                        list[right_cursor-1],list[right_cursor]=list[right_cursor],list[right_cursor-1]
                        swap_left(list,left_cursor,right_cursor-1)
                        swap_right(list,right_cursor,right_last)
                        
                def swap_right(list,left_cursor,right_cursor):
                    if left_cursor==right_cursor:
                        return
                    else:
                        if list[left_cursor]>=list[left_cursor+1]:
                            return 
                        else:
                            list[left_cursor],list[left_cursor+1]=list[left_cursor+1],list[left_cursor]
                            swap_right(list,left_cursor+1,right_last)
                            swap_left(list,left_first,left_cursor)
                if isinstance(left_side,int):
                    left_first,left_last=left_side,left_side
                    
                else:
                    left_first,left_last=left_side[0],left_side[1]
                    
                if isinstance(right_side,int):
                    right_first,right_last=right_side,right_side
                else:
                    
                   right_first,right_last=right_side[0],right_side[1]
              
                
                if list[left_last]<list[right_first]:
                    list[left_last],list[right_first]=list[right_first],list[left_last]
                    swap_right(list,right_first,right_last)
                    swap_left(list,left_first,left_last)
                    
                x=[left_first,right_last]
                
                return x
          
        def dividing(list,first_index,last_index,size):
            if first_index==last_index:
               
                
                return first_index
            else:
              mid=(first_index+last_index)//2
              
              left_side=dividing(list,first_index,mid,(mid-first_index)+1)
              right_side=dividing(list,mid+1,last_index,last_index-mid)
            
            
            return  swap_merge(list,left_side,right_side)

        
        dividing(self._list,0,len(self)-1,len(self))
        return self

    #info 

    def is_epmty(self):
        return len(self)==0

    def __len__(self):
        return len(self._list)

    def __iter__(self):

       for i in range(len(self)):
           yield self._list[i]

    def __repr__(self):
        
        return f"{self._list}"

    def first(self):
        return self._list[0]

    def last(self):
        return self._list[-1]

    def max(self):
        return max(self._list)
    
    def min(self):
        return min(self._list)

    def sum(self):
        return sum(self._list)
    
    def mean(self):
        return self.sum()/len(self)

    def median(self):
        the_list=copy.deepcopy(self._list)
        x=sorted(the_list)
        if len(x)%2==0:
            median_index=len(x)//2
            median=(x[median_index-1]+x[median_index])/2
        else:
            median_index=len(x)//2
            median=x[median_index]
        return median

    def mood(self):
        
        if len(self)==0:
            return None

        if len(self)==1:
            return self
        dict_of_elements=self.no_elements_existance()
        max_value=max(dict_of_elements.values())
        mood=[]
        for i in dict_of_elements.keys():
            if dict_of_elements[i]==max_value:
                mood.append(i)

        return mood 
    

linked=sorted_list_array()
linked.the_list=[11,2,3,4,"kk"]
print(linked)
linked.insert_first(100)
print(linked)

linked.insert_index(500,3)
print(linked)
print(linked.search(500))
print(linked.search(-1))
linked.insert_before_data(500,101)
print(linked)
linked.insert_after_data(5,5.5)
print(linked)
print(linked.list)
linked.delete_index(1)
print(linked)
linked.delete_after_data(5.5)
print(linked)
linked2=sorted_list_array()
linked2.list=[0,0,0]
print("\n")
print(linked+linked2)
print(linked2+linked)
print(linked.merge_without_change(linked2))
print(linked)
print(linked2)
print("\n")
print(linked.merge_with_changes(linked2))
print(linked)
print(linked2)

linked.swap_elements_by_index(0,len(linked)-1)
print(linked)
print(linked.reverse_with_changes())
print("nnnn")
print(linked)
print(linked.sort_ascending_recursive())
print(linked.sort_descending_recursive())
print("nnnnn")
print(linked.sort_descending())
linked.insert_last(522)
linked.insert_last(500)
linked.insert_first(500)
print(linked)
print(linked.max(),linked.min())
print(linked.sum())
print(linked.no_elements_existance())

print(linked.mean(),linked.median(),linked.mood())
class sorted_linked_bubble:
      
      class node:
            def __init__(self):
                ...

      def __init__(self):
          ...

print(3.5//2)


print("\n\n")
failing_test_cases = [
        [2, 1, 3],  # Simple case where incorrect merge is likely
        [5, 1, 4, 2, 8], # Slightly larger list to show more complex merges.
        [1, 5, 2, 8, 3, 9], # Interleaved larger and smaller numbers
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], # Reverse sorted (larger)
        [1, 3, 5, 7, 9, 8, 6, 4, 2, 0], # Almost sorted, with a few out of place
        [1, 1, 1, 2, 2, 1, 1, 2],  # More duplicates to highlight duplicate handling problems
        [5, 2, 8, 1, 9, 4, 7, 3, 6, 0], # More complex arrangement for merge issues
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # larger ordered list
        [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], # larger reversed list
        random.sample(range(-50, 50), 20) # Random list with negative numbers
    ]
import copy 
for i in failing_test_cases:
    cop=copy.deepcopy(i)
    sort=sorted_list_array()
    sort.the_list=cop 
    print(i,sort.sort_ascending_recursive(),sorted(i))
    print("\n")


for i in range(5,0,-1):
    print(i)


google_test=sorted_list_array()
google_test.the_list=[1 , 3, 2,  "abc"]
print(sorted([1 , 3, 2,  "abc"]))
print(google_test.sort_ascending_recursive())
print(sorted([1 , 3, 2,  "abc"],reverse=True))
print(google_test.sort_descending_recursive())