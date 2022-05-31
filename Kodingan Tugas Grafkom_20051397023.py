from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# mendefinisikan titik-titik dengan nilai (20, 30, 40, 60)
def bresenham(x0, y0, x1, y1):
    
    
    # menentukan nilai dx dan dy yakni 20 dan 40
    dx = x1 - x0
    dy = y1 - y0
     
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0
    for x in range(dx+1):
        glVertex2i(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
        # menggambar titik titik nilai dengan menggunakan algoritma bresenham
        if D > 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def display():
    # membersihkan windows
    glClear(GL_COLOR_BUFFER_BIT)
    # memberikan warna biru pada titik
    glColor3f(0.0, 0.0, 1.0)
    #menentukan ukuran titik
    glPointSize (3.0)
    # Memilih mode points
    glBegin(GL_POINTS)
    # membuat nilai titik
    bresenham(20,30,40,60)
    glEnd()
    glFlush()

def main():
    # meng-inisiasi GLUT
    glutInit(sys.argv)
    # meng-inisiasi GLUT Display
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # meng-inisiasi ukuran layar
    glutInitWindowSize(500, 500)
    # meng-inisiasi posisi window
    glutInitWindowPosition(100, 100)
    # meng-inisiasi pembuatan window
    glutCreateWindow(b"Algoritma Bresenham")
    # clear screen windows dan BG color
    glClearColor(0.0, 0.0, 0.0, 0.0)
    #melakukan set origin dari grid
    gluOrtho2D(0, 50, 0, 50)
    # call function
    glutDisplayFunc(display)
    glutMainLoop()

main()