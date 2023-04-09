from OpenGL.GL import *
from OpenGL.GLUT import *

from math import * 
import math as mth


#vector fields
from vector_fields import _3d_vector_field as _3dvf


# Globals
windowWidth = 800
windowHeight = 800
lastMouseX = 0
lastMouseY = 0
rotateX = 0.0
rotateY = 0.0




#coordinate transformations

def cartesian_to_polar(x, y, z):
    r = sqrt(x**2 + y**2 + z**2)
    theta = atan2(sqrt(x**2 + y**2), z)
    phi = atan2(y, x)
    return r, theta, phi

def polar_to_cartesian(r, theta, phi):
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return x, y, z




def draw_vector(x, y, z, r, g, b, size):

    glColor3f(r, g, b)
    scale=2.0
    scale_=1/100.0

    for i in range(_3dvf.N):
        for j in range(_3dvf.N):
            for k in range(_3dvf.N):
                [x,y,z]=scale_*_3dvf.vectors[i,j,k] + [i/scale, j/scale, k/scale]
                #[i_,j_,k_]= [i,j,k]


              

                glBegin(GL_LINES)
                glVertex3f(i/scale, j/scale, k/scale)        # start point at origin

                #print(i/scale_, j/scale_, k/scale_)
                glVertex3f(x, y, z)        # end point at (x, y, z)
                glEnd()

                glBegin(GL_POINTS)
                glVertex3f(i/scale, j/scale, k/scale)  # set point coordinates
                glEnd()
                
    

                [r,theta,phi]=cartesian_to_polar(x,y,z)

    
    
                #Draw arrowhead

                #glRotatef(mth.atan2(y, x) * 180 /mth. pi, 0, 0, 1)

                r=r-size
                phi1=phi-pi/20.0
                phi2=phi+pi/20.0

                [x1,y1,z1]= polar_to_cartesian(r,theta, phi1)
                [x2,y2,z2]= polar_to_cartesian(r,theta, phi2)

                glPushMatrix()
                glTranslatef(size/10.0,size/10.0,size/10.0)
                glBegin(GL_TRIANGLES)
                glVertex3f(x, y, z)
                glVertex3f(x1,y1,z1)
                glVertex3f(x2,y2,z2)
                glEnd()

                glPopMatrix()
   


def draw_line():
    glLineWidth(2.0)          # set line width to 3.0
    glBegin(GL_LINES)
    

    # x - axis
    glColor3f(1.0, 0.0, 0.0)  # set color to red
    
    glVertex3f(0.0, 0.0,0.0)  # start point
    glVertex3f(0.2, 0.0,0.0)  # end point

    #y - axis
    glColor3f(0.0, 1.0, 0.0)  # set color to red
    glVertex3f(0.0, 0.0,0.0)  # start point
    glVertex3f(0.0, 0.2,0.0)  # end point

    #z - axis
    glColor3f(0.0, 0.0, 1.0)  # set color to red
    glVertex3f(0.0, 0.0,0.0)  # start point
    glVertex3f(0.0, 0.0,0.2)  # end point
    
    glEnd()





def display():
    global rotateX, rotateY, camera_z
    
    glClear(GL_COLOR_BUFFER_BIT )
    

    # Apply rotation
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(rotateX, 1.0, 0.0, 0.0)
    glRotatef(rotateY, 0.0, 1.0, 0.0)

    glTranslatef(-0.5,-0.5,0.0)
    
    # Draw line
    
    draw_line()

    draw_vector(0.1,0.1,0.1,1,1,1, 0.04)

    glutSwapBuffers()

    glFlush()








def onMouseButton(button, state, x, y):
    global lastMouseX, lastMouseY
    
    # Save last mouse position
    lastMouseX = x
    lastMouseY = y






def onMouseMove(x, y):
    global lastMouseX, lastMouseY, rotateX, rotateY
    
    # Calculate mouse movement
    deltaX = x - lastMouseX
    deltaY = y - lastMouseY
    
    # Update rotation angles
    rotateX += deltaY
    rotateY += deltaX
    
    # Save last mouse position
    lastMouseX = x
    lastMouseY = y
    
    # Trigger a redraw
    glutPostRedisplay()




if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(windowWidth, windowHeight)
    glutCreateWindow(b"OpenGL vector field")
    glutDisplayFunc(display)
    glutMouseFunc(onMouseButton)
    glutMotionFunc(onMouseMove)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutMainLoop()