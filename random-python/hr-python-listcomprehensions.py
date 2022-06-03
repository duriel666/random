if __name__ == '__main__':
    x, y, z, n = 2, 2, 2, 3
    print([[i, j, k] for i in range(x+1) for j in range(y+1)
          for k in range(z+1) if i+j+k != n])
    # testing
    print("testi" if n < 3 else "kakka")
