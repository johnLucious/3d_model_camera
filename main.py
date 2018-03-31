# IF3260: Computer Graphics
# Camera 3D Modelling

# Libraries and Packages
import sys

from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Camera Position
angle = 0.0 			# Camera angle
x = 0.0

z = 0.0					# Camera position
dX = 0.0

dZ = 0.0				# Camera direction


class Camera:
	
	def __init__(self):
		self.position = (0, 0, 0)
		self.rotation = (0, 0, 0)
	
	def translate(self, dx, dy, dz):
		x, y, z = self.position
		self.position = (x + dx, y + dy, z + dz)
		
	def rotate(self, dx, dy, dz):
		x, y, z = self.rotation
		self.rotation = (x + dx, y + dy, z + dz)
		
	def apply(self):
		glTranslate(*self.position)
		glRotated(self.rotation[0], -1, 0, 0)
		glRotated(self.rotation[1], 0, -1, 0)
		glRotated(self.rotation[2], 0, 0, -1)
		
camera = Camera()

# Snowman
def drawSnowMan():
	glColor3f(1.0, 1.0, 1.0)

	#Draw Body
	glTranslatef(0.0 ,0.75, 0.0)
	glutSolidSphere(0.75,20,20)

	#Draw Head
	glTranslatef(0.0, 1.0, 0.0)
	glutSolidSphere(0.25,20,20)

	#Draw Eyes
	glPushMatrix()
	glColor3f(0.0,0.0,0.0)
	glTranslatef(0.05, 0.10, 0.18)
	glutSolidSphere(0.05,10,10)
	glTranslatef(-0.1, 0.0, 0.0)
	glutSolidSphere(0.05,10,10)
	glPopMatrix()

	#Draw Nose
	glColor3f(1.0, 0.5 , 0.5)
	glutSolidCone(0.08,0.5,10,2)

def renderScene():
	global x, z, dX, dZ, angle
	#Clear Color and Depth Buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	#Reset transformations
	glLoadIdentity()
	#Set the camera
	#gluLookAt	(	x, 1.0, z,
	#			x+dX, 1.0,  z+dZ,
	#			0.0, 1.0,  0.0
	#			)
	
	camera.apply()
	
	#Draw ground
	glColor3f(0.9, 0.9, 0.9)
	glBegin(GL_QUADS)
	glVertex3f(-100.0, 0.0, -100.0)
	glVertex3f(-100.0, 0.0,  100.0)
	glVertex3f( 100.0, 0.0,  100.0)
	glVertex3f( 100.0, 0.0, -100.0)
	glEnd()

    #Draw 36 Snowmen
	for i in range (-3,3):
		for j in range(-3,3):
			glPushMatrix()
			glTranslatef(i*10.0,0,j * 10.0)
			drawSnowMan()
			glPopMatrix()

	glutSwapBuffers()
	
def processSpecialKeys(key, xx, yy):
	global x, z, dX, dZ, angle
	fraction = 0.1
	movespeed = 1
	
	if (key == GLUT_KEY_LEFT):
		camera.translate(movespeed, 0, 0)
		#angle -= 0.01
		#dX = sin(angle)
		#dY = -cos(angle)
	elif (key == GLUT_KEY_RIGHT):
		camera.translate(-movespeed, 0, 0)
		#angle -= 0.01
		#dX = sin(angle)
		#dY = -cos(angle)
	elif (key == GLUT_KEY_UP):
		camera.translate(0, 0, movespeed)
		#x += dX * fraction
		#z += dZ * fraction
	elif (key == GLUT_KEY_DOWN):
		camera.translate(0, 0, -movespeed)
		#x -= dX * fraction
		#z -= dZ * fraction

def processNormalKeys(key, x, y):
	if (key == 27):
		exit(0)

def changeSize(w, h):
	#Prevent a divide by zero, when window is too short
	#(you cant make a window of zero width).
	if (h == 0):
		h = 1;
	ratio = w * 1.0 / h

	#Use the Projection Matrix
	glMatrixMode(GL_PROJECTION)

	#Reset Matrix
	glLoadIdentity()

	#Set the viewport to be the entire window
	glViewport(0, 0, w, h)

	#Set the correct perspective.
	gluPerspective(45.0, ratio, 0.1, 100.0)

	#Get Back to the Modelview
	glMatrixMode(GL_MODELVIEW)
		
def main():

	#init GLUT and create window
	glutInit()
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
	glutInitWindowPosition(100,100)
	glutInitWindowSize(800,600)
	glutCreateWindow(b'IF3260: Computer Graphics')

	glMatrixMode(GL_PROJECTION)
	gluPerspective(60, 1, 1.0, 1000.0)
	glMatrixMode(GL_MODELVIEW)
	
	#register callbacks
	glutDisplayFunc(renderScene)
	glutReshapeFunc(changeSize)
	glutIdleFunc(renderScene)
	#glutKeyboardFunc(processNormalKeys)
	glutSpecialFunc(processSpecialKeys)

	#OpenGL init
	glEnable(GL_DEPTH_TEST)

	#enter GLUT event processing cycle
	glutMainLoop()
	
main()
'''# Class
class cameraBase(object):
	def __init__(self):
		self.item = None'''