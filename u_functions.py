import matplotlib.pyplot as plt

def get_axis_limits(ax, scale=.9):
    return ax.get_xlim()[1]*scale, ax.get_ylim()[1]*scale



def showplot(x_train,y_train,labels,rows=10,cols=10):

    fig=plt.figure(figsize=(40, 40))
    columns = 10
    rows = 10
    for i in range(1, columns*rows +1):
        img = x_train[i]
        ax1 = fig.add_subplot(rows, columns, i)
        ax1.annotate(labels[y_train[i][0]],xy=get_axis_limits(ax1))
        plt.imshow(img)
    plt.show()
