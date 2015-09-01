
# Build Minesweeper game
#
# 
# Created by: Dr.Akshay P
# Last modified: 08/31/15
# Copyright (c) 2015 Dr. Akshay P. All rights reserved.
# Please contact me at github for questions
#

import numpy
import random

def buildMineSweeper():
    """
    rows,cols,mines can be used to take input from user,
    uncomment next 3 lines if required
    for now its fixed bcs of nature of this IDE
    """
    
    rows = input('Please provide # of rows in minesweeper array:')
    cols = input('Please provide # of cols in minesweeper array:')
    mines = input('Please provide # of mines in minesweeper array:')
    
    #comment above lines which read user input and uncomment next 3 lines
    #if you want to test with fixed values

    #rows=5
    #cols=9
    #mines=10

    cood=[]
    
    matrix = numpy.zeros((rows, cols))
    mine_arr=random.sample(xrange(0,rows*cols),mines)
    print 'mines are located at foll.: '
    print mine_arr
    print '\n'
    for x in mine_arr:
        getCord(x,cood,cols)
        updateMines(matrix,cood,cols,rows)
        cood=[]
    print 'final minesweeper array is as follow: '
    print matrix

def getCord(x,cood,cols):
    """
    maps random mine number into app. co-od
    co.od[0] has row identifier
    co.od[0] has col. identifier
    """
    
    cood.append(x/cols)
    cood.append(x%cols)
    
def updateMines(matrix,cood,cols,rows):
    """
    this fx, updates the 2D array as follows:
    updates -1 where there is a mine.
    increments rest of cells to indiciate mines in adjoining 8 locations
    boundary conditions are verified here
    """
    cnt=0
    matrix[cood[0]][cood[1]]=-1
    if (cnt != 8):
        for i in xrange(cood[0]-1,cood[0]+2):
            for j in xrange(cood[1]-1,cood[1]+2):
                cnt+=1
                if (0<=j<cols and 0<=i<rows):
                    if (matrix[i][j]!=-1):
                        matrix[i][j]+=1
                        

buildMineSweeper()
