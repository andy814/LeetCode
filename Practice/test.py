def getAnswer():
    for i in range(1,10**5):
        for j in range(1,10**5):
            if i<j*0.9 and i+0.1>j*0.9:
                print(i,j)
                return

getAnswer()