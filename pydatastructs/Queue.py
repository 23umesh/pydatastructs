class Queue:
	'''
	Creation of Queue Data Type in python with list prebuilt data type
	------------------------------------------------------------------

	Parameter
	==========
	max_size:
		 type-int.
		 denotes the maximum size of queue.
	

	Raises
	=======
	No particular raisse till now.

	Operations available:
	=====================
	1. initialisation of queue.
	2. Check whether Queue is empty or not.
	3. Appending elements into the queue on a first come first serve basis.
	4. popping elements on first arrival basis.
	5. detecting length of Queue.
	6. Check whether queue is full or not.
	 '''
	
    def __new__(cls):
	obj = object.__new__(cls)
        obj.elements = []
	
    def __len__(self):
        return len(self.elements)
    
    def isEmpty(self):
        return self.elements == []

    def append(self, new_elem):
    	self.elements.append(new_elem)

    def popleft(self):
        if (self.elements==[]):
        	 return "Queue is empty!"
        else self.elements.pop(0)
