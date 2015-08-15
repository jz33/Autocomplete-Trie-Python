'''
Author: junzhengrice@gmail.com
'''
def CenterWindow(parent):    
    w = 600
    h = 80

    sw = parent.winfo_screenwidth()
    sh = parent.winfo_screenheight()
    
    x = (sw - w)/2
    y = (sh - h)/2
    parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
def LoadFile(filename):
    buf = open(filename,'r')
    for line in buf:
        line = line.strip()
        yield line
    buf.close()
    