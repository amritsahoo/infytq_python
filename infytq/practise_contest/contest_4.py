'''
Created on Apr 26, 2020

@author: amrit
'''
import sys
INF=sys.maxsize
N=4
def youngify(mat,i,j):
    if(i+1<N):
        below_value=mat[i+1][j]
    else:
        below_value=INF
    if(j+1<N):
        right_value=mat[i][j+1]
    else:
        right_value=INF
    if(below_value==INF and right_value==INF):
        return 
    if(below_value<right_value):
        mat[i][j]=below_value
        mat[i+1][j]=INF
        youngify(mat, i+1, j)
    else:
        mat[i][j]=right_value
        mat[i][j+1]=INF
        youngify(mat, i, j+1)
def extractMin(mat):
    small_value=mat[0][0]
    mat[0][0]=INF
    youngify(mat,0,0)
    return small_value
def printSorted(mat):
    i=0
    while(i<N*N):
        print(extractMin(mat),end=" ")
        i+=1
if __name__=="__main__":
    mat=[[10, 20, 30, 40],
         [15, 25, 35, 45],
         [17, 27, 29, 41],
         [19, 28, 37, 43]]
    printSorted(mat)