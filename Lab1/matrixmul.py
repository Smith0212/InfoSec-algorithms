import numpy as np

def matrixes(a,b):
    c = np.zeros((a.shape[0],b.shape[1]))
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                c[i][j] += a[i][k]*b[k][j]
    return c

def main():
    a=[]
    b=[]
    
    for i in range(3):
        row = []
        for j in range(3):
            row.append(int(input(f"Enter the element a[{i+1}][{j+1}]:")))
        a.append(row)
    print("Matrix A is:" ,a)

  
    for i in range(3):
        row = []
        for j in range(3):
            row.append(int(input(f"Enter the element a[{i+1}][{j+1}]:")))
        b.append(row)
    print("Matrix B is:" ,b)

    c = matrixes(np.array(a),np.array(b))
    print(c)
if __name__ == "__main__":
    main()


