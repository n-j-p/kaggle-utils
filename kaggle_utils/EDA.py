def xvarplot(df):
    '''cross-variable correlation plot'''
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    nr, nc = df.shape

    nc -= 1
    plt.figure(figsize=(16,16))
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=FutureWarning)

        # Plot column histograms
        for i in range(1,nc+1):
            a2=plt.subplot(nc+1,nc+1,i)
            # ax = sns.histplot(data=df,
            #                   x=df.columns[i], 
            #                   legend=False)
            plt.hist(df.iloc[:,i])
            ax = plt.gca()
            ax.set_ylabel('')
            ax.set_yticks([])
            ax.set_xlabel(df.columns[i])
            ax.xaxis.set_label_position('top') 

        # Plot row histograms
        for j in range(nc):
            plt.subplot(nc+1,nc+1,(nc+1)*(j+2))
            # ax = sns.histplot(data=df,
            #                   y=df.columns[j],
            #                   legend=False)
            plt.hist(df.iloc[:,j])
            ax = plt.gca()
            ax.set_xlabel('')
            ax.set_ylabel(df.columns[j])
            ax.yaxis.set_label_position('right') 

        # Plot above-diagonal scatterplots
        for i in range(1,nc+1):
            for j in range(nc):
                if j > i-1: 
                    continue
                plt.subplot(nc+1,nc+1,(nc+1)*(j+1)+i)
                # ax3 = sns.scatterplot(data=df,
                #                       s=0.5,
                #                       x=df.columns[i],
                #                       y=df.columns[j], legend=False)
                plt.plot(df.iloc[:,i],df.iloc[:,j], 'k.')
                ax3 = plt.gca()
                ax3.set_xlabel('')
                ax3.set_ylabel('')
                ax3.set_yticklabels('')
                ax3.set_xticklabels('')

def cat_pie(df, catvars, ncols=2):
    '''multi-panel pie chart for categorical variables.'''
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    counts = pd.melt(df[catvars]).groupby('variable').value_counts().reset_index()
    def pie_chart(n, kind, **kwargs):
        plt.pie(x = n, labels = kind)
    g = sns.FacetGrid(counts, 
                      col = 'variable',
                      col_wrap = ncols)
    g.map(pie_chart, 'count', 'value')
