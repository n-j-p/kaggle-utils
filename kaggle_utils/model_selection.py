def show_scv_results(cv_results_obj):
    try:
        param_names = cv_results_obj.param_distributions.keys()
    except AttributeError:
        try:
            param_names = cv_results_obj.param_grid.keys()
        except AttributeError:
            raise ValueError('cv_results_obj must be gscv or rscv')
    plt.figure(figsize=(18,12))
    for i, param_name in enumerate(param_names):
        plt.subplot(2,len(param_names),i+1)
        plt.plot(cv_results_obj.cv_results_['param_'+param_name].data,
                 -cv_results_obj.cv_results_['mean_test_score'],'o')
        plt.subplot(2,len(param_names),i+1+len(param_names))
        plt.semilogx(cv_results_obj.cv_results_['param_'+param_name].data,
                 -cv_results_obj.cv_results_['mean_test_score'],'o')
        plt.title(param_name)
