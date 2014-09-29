sam_addr = 1
 
useleft = 0  
for i in range(17):
    
   
        
    if i ==  (sam_addr - 1):
        print i, 'left' 
    else:
        if i == ( sam_addr ):
            print i, 'sam'
        else:
            if i == ( sam_addr + 1 ):
                print i, 'right', 'left'
                sam_addr = sam_addr + 2
                     
            
                
                    
 