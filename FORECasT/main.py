import pandas as pd
import os
import numpy as np
import plotly.express as px

import pearson_correlation as pearson


def indelphi_pcc():
    data = pd.read_pickle('../inDelphi/test_inDelphi.pkl')

    mutation = 'del_features'
    features = pd.DataFrame(data[mutation])
    features_cols = features.columns.tolist()

    if os.path.exists('indelphi_pccs_' + str(mutation) + '.pkl'):
        pearson_ccs = pd.read_pickle('indelphi_pccs_' + str(mutation) + '.pkl')
    else:
        pearson_ccs = pearson.get_pearson_ccs(features_cols, features, mutation, 'indelphi')

    significant_correlations = pearson.get_significant_correlations(pearson_ccs)

    pearson_ccs = {k: v for k, v in significant_correlations.items() if not pd.isna(v)}

    return pearson_ccs


def forecast_pcc():
    data = pd.read_pickle('train/Tijsterman_Analyser/Oligo_38')
    float_data = data.drop(labels=['Indel'], axis=1)
    feature_cols = float_data.columns.tolist()

    if os.path.exists('forecast_pccs.pkl'):
        pearson_ccs = pd.read_pickle('forecast_pccs.pkl')
    else:
        pearson_ccs = pearson.get_pearson_ccs(feature_cols, data, '', 'forecast')

    significant_correlations = pearson.get_significant_correlations(pearson_ccs)

    pearson_ccs = {k: v for k, v in significant_correlations.items() if not pd.isna(v)}

    return pearson_ccs


def heatmap(pccs, model, sliced=False):
    feature_keys = list(pccs.keys())
    feature_1 = [feature_keys[i][0] for i in range(len(feature_keys))]
    feature_2 = [feature_keys[i][1] for i in range(len(feature_keys))]
    feature_1 = list(set(feature_1))
    feature_2 = list(set(feature_2))

    df = pd.DataFrame(np.zeros((len(feature_1), len(feature_2))), index=feature_1, columns=feature_2).astype('float32')
    for key, value in pccs.items():
        df.loc[key[0], key[1]] = value

    if sliced:
        df_row_slices = []
        df_column_slices = []

        if df.shape[0] < df.shape[1]:
            for i in range(df.shape[0]):
                if i % 20 == 0:
                    df_row_slices.append(i)

            df_column_slices = df_row_slices.copy()

        else:
            for i in range(df.shape[1]):
                if i % 20 == 0:
                    df_column_slices.append(i)

            df_row_slices = df_column_slices.copy()

        for i in range(len(df_row_slices) - 1):
            fig = px.imshow(df.iloc[df_row_slices[i]:df_row_slices[i+1], df_column_slices[i]:df_column_slices[i + 1]],
                            labels=dict(x='Feature 2', y='Feature 1', color='Correlation'),
                            color_continuous_scale=px.colors.sequential.Plasma
                            )
            fig.update_layout(title='Pearson Correlation Heatmap of %s Features' % model)
            fig.show()

    else:
        fig = px.imshow(df,
                        labels=dict(x='Feature 2', y='Feature 1', color='Correlation'),
                        color_continuous_scale=px.colors.sequential.Plasma
                        )
        fig.update_layout(title='Pearson Correlation Heatmap of %s Features' % model)
        fig.show()


def main():
    """
    Note that the features for inDelphi are size, homologyLength and homologyGCContent.
    """

    indelphi = False
    forecast = True

    if indelphi:
        indelphi_pccs = indelphi_pcc()
        heatmap(indelphi_pccs, 'inDelphi')

    if forecast:
        forecast_pccs = forecast_pcc()
        heatmap(forecast_pccs, 'FORECasT')


if __name__ == '__main__':
    main()
