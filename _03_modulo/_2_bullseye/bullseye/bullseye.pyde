w = 250
h = 250
def setup():
    size(500, 500)    
def draw():
    w = 250
    h = 250
    background('#FFFFFF')
    global w,h
    for i in range(6):
        ellipse(250, 250, w, h)
        w-=40
        h-=40        
    # Set the size of your sketch
        if i % 2 == 0:
            fill('#FFFFFF')
        else:
            fill('#FF0505')
            
                
     
    

    

    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    
    # Use an if statement and modulo to alternate the color of your rings
    
    
