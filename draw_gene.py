from turtle import *
import numpy as np

#read file
f=textinput("Input_file_name", "Name of your file:")
temp=np.genfromtxt(f,dtype='<U10,int,int,int')

ll=int(temp[0][0])
scales=ll/1000
ll=1000
reset()
up()
backward(ll/2)
down()
write('0')
forward(ll)
if int(temp[0][0])<1000:
    write(temp[0][0])
else:
    write(str(int(temp[0][0])/1000)+'kb')
setposition(-1*(ll/2),0)
counter_z=0
counter_o=0
for i in range(1,len(temp)):
    forward(temp[i][1]/scales)
    
    if (temp[i][3]==1):
        counter_o+=1
        #print(counter_o)
        color('red')
        begin_fill()
        left(90)
        forward(60)
        
        right(90)
        l=(temp[i][2]-temp[i][1])/scales
        forward(l/2)
        if (counter_o%2==1):
            left(90)
            forward(20)
            up()
            left(90)
            forward(5*len(temp[i][0])/2)
            down()
            write(temp[i][0])
            up()  
            backward(5*len(temp[i][0])/2)
            right(90)
            down()
            backward(20)
        else:
            left(90)
            forward(40)
            up()
            left(90)
            forward(5*len(temp[i][0])/2)
            down()
            write(temp[i][0])
            up()           
            backward(5*len(temp[i][0])/2)
            right(90)
            down()
            backward(40)
            
        right(90)
        forward(l/2)
        right(90)
        forward(60)
        left(90)
        end_fill()
        color('black')
    else:
        counter_z+=1
        color('blue')
        begin_fill()
        #write(temp[i][0])
        right(90)
        forward(60)
        left(90)
        l=(temp[i][2]-temp[i][1])/scales
        forward(l/2)
        
        if (counter_z%2==1):
            right(90)
            forward(40)
            up()
            forward(10)
            right(90)
            forward(5*len(temp[i][0])/2)
            down()
            write(temp[i][0])
            up()
            backward(5*len(temp[i][0])/2)
            left(90)
            backward(10)
            down()
            backward(40)
        else:
            right(90)
            forward(10)
            up()
            forward(10)
            right(90)
            forward(5*len(temp[i][0])/2)
            down()
            write(temp[i][0])
            up()
            backward(5*len(temp[i][0])/2)
            left(90)
            backward(10)
            down()
            backward(10)
        left(90)
        forward(l/2)
        left(90)
        forward(60)
        right(90)
        end_fill()
        color('black')
    setposition(-1*(ll/2),0)
setposition(ll/2,0)
done()