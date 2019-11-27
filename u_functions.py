import matplotlib.pyplot as plt

def get_axis_limits(ax, scale=.9):
    return ax.get_xlim()[1]*scale, ax.get_ylim()[1]*scale



def showplot(x_train,y_train,labels,rows=10,cols=10):

    fig=plt.figure(figsize=(24, 24))
    for i in range(1, cols*rows +1):
        img = x_train[i]
        ax1 = fig.add_subplot(rows, cols, i)
        ax1.annotate(labels[y_train[i][0]],xy=get_axis_limits(ax1))
        plt.imshow(img)
    plt.show()


def plot_multiple_imgs(labels,X,y,nrow=10,ncol=10,figsize=(13,7),preds=None,skip=0,):
    fig,ax = plt.subplots(nrows=nrow,ncols=ncol,figsize=figsize)
    fig.subplots_adjust(hspace=0.1, wspace=0.1)
    for i in range(nrow*ncol):
        ax[i//ncol,i%ncol].imshow(X[skip+i],cmap='binary')
        ax[i//ncol,i%ncol].set_xticks([])
        ax[i//ncol,i%ncol].set_yticks([])
        ax[i//ncol,i%ncol].text(0.05, 0.1,labels[y[i][0]], color='blue',transform=ax[i//ncol,i%ncol].transAxes,weight='bold')
    plt.show()
