import matplotlib.pyplot as plt
# This distance function calculates
# the distance between two points
# on a graph
def dist(A,B):
  Xa = A[0]
  Xb = B[0]
  Ya = A[1]
  Yb = B[1]
  return ( (Xa-Xb)**2 + (Ya-Yb)**2 ) ** 0.5

def perimeter(X,Y):
  num_vertices = len(X)
  perim = 0 # counter variable
  for i in range(num_vertices):
    x_current = int(X[i])
    y_current = int(Y[i])
    x_next    = int(X[ (i+1)%num_vertices ])
    y_next    = int(Y[ (i+1)%num_vertices ])
    perim += dist(
      (x_current, y_current),
      (x_next, y_next)
    )
  return perim

if __name__ == '__main__':
    #X_coords = [1,3,2] # List of X Coordinates of each Vertex
    #Y_coords = [1,1,4] # List of Y Coordinates of each Vertex
    X_coords = input("Enter your X coords with spaces between: ").split(" ")
    Y_coords = input("Enter your Y coords with spaces between: ").split(" ")
    print("X Coordinates:",X_coords)
    print("Y Coordinates:",Y_coords)
    peri_ABC = perimeter(X_coords,Y_coords)

    print("The perimeter of the polygon is", peri_ABC)
    plt.plot(X_coords, Y_coords)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('My first graph!')
    plt.show()
