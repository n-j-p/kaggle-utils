def xvarplot(df):
    '''cross-variable correlation plot'''
    import matplotlib.pyplot as plt
    
    nr, nc = df.shape

    nc -= 1
    plt.figure(figsize=(16,16))
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=FutureWarning)

        # Plot column histograms
        for i in range(1,nc+1):
            a2=plt.subplot(nc+1,nc+1,i)
            ax = sns.histplot(data=df,
                              x=df.columns[i], 
                              legend=False)
            ax.set_ylabel('')
            ax.set_yticks([])
            ax.set_xlabel(df.columns[i])
            ax.xaxis.set_label_position('top') 

        # Plot row histograms
        for j in range(nc):
            plt.subplot(nc+1,nc+1,(nc+1)*(j+2))
            ax = sns.histplot(data=df,
                              y=df.columns[j],
                              legend=False)
            ax.set_xlabel('')
            ax.set_ylabel(df.columns[j])
            ax.yaxis.set_label_position('right') 

        # Plot above-diagonal scatterplots
        for i in range(1,nc+1):
            for j in range(nc):
                if j > i-1: 
                    continue
                plt.subplot(nc+1,nc+1,(nc+1)*(j+1)+i)
                ax3 = sns.scatterplot(data=df,
                                      s=0.5,
                                      x=df.columns[i],
                                      y=df.columns[j], legend=False)
                ax3.set_xlabel('')
                ax3.set_ylabel('')
                ax3.set_yticklabels('')
                ax3.set_xticklabels('')
