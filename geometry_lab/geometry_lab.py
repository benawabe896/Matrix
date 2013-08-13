from mat import *
from vec import *
from image_mat_util import *
import math
from matutil import *

position, color = file2mat("cit.png")

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels, labels), {(x,y):1 for x in labels for y in labels if x == y})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    labels = {'x','y','u'}
    i = identity()
    m = Mat(i.D, {('x', 'u'):x, ('y', 'u'):y})
    #return i + m
    return Mat((labels, labels), { ('x', 'x'): 1, ('x', 'u'): x, ('y','y'): 1, ('y', 'u'): y, ('u', 'u'): 1 })

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    labels = {'x','y','u'}
    return Mat((labels, labels), { ('x', 'x'): a, ('y','y'): b, ('u', 'u'): 1 })

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    labels = {'x','y','u'}
    #return Mat((labels, labels), { ('x','x'): 1, ('y','y'): math.cos(angle), ('y','u'):-math.sin(angle),('u','y'): math.sin(angle), ('u', 'u'): math.cos(angle) })
    #return Mat((labels, labels), { ('x','x'): math.cos(angle), ('x','u'):math.sin(angle), ('y','y'): 1, ('u','x'): -math.sin(angle), ('u', 'u'): math.cos(angle) })
    return Mat((labels, labels), { ('x','x'): math.cos(angle), ('x','y'):-math.sin(angle), ('y','x'): math.sin(angle), ('y','y'): math.cos(angle), ('u', 'u'): 1 })

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y) * rotation(angle) * translation(-x,-y)

t = translation(10,10)
r = rotation(20)
print(t*r)
print(t+r)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    pass

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    pass
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    pass

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    pass   

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


