# -*- coding: utf-8 -*-
"""

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def quatro_scatters(df, 
                    coluna_alvo, 
                    col1, col2, col3, col4, size=7, grid=False):

    fig,ax = plt.subplots(ncols=2,nrows=2, figsize=(12,8), tight_layout=True)
    ax[0][0].scatter(df[col1], df[coluna_alvo],s=size)
    ax[0][1].scatter(df[col2], df[coluna_alvo],s=size)
    ax[1][0].scatter(df[col3], df[coluna_alvo],s=size)
    ax[1][1].scatter(df[col4], df[coluna_alvo],s=size)
    ax[0][0].set_title(col1, fontsize=12, fontweight='bold')
    ax[0][1].set_title(col2, fontsize=12, fontweight='bold')
    ax[1][0].set_title(col3, fontsize=12, fontweight='bold')
    ax[1][1].set_title(col4, fontsize=12, fontweight='bold')
    plt.suptitle(coluna_alvo, fontsize=16, fontweight='bold')
    if grid == True:
        ax[0][0].grid()
        ax[0][1].grid()
        ax[1][0].grid()
        ax[1][1].grid()
    plt.show()


def graficos_col_categoricas(base, coluna_alvo, coluna):
    abc = base[coluna].value_counts()
    if len(abc.index) < 7:
        fig, ax = plt.subplots(ncols=2,figsize=(10,3))
        sns.boxplot(data=base,x=coluna,y=coluna_alvo,ax=ax[0],showmeans=True)
        sns.histplot(base[coluna],ax=ax[1])
        a = base[coluna].value_counts()
        for i in range(len(a.index)):
            ax[1].annotate(a.values[i],(a.index[i], a.values[i]+a.values[i]*0.02),ha='center')
        ax[1].yaxis.set_visible(False)
        ax[0].spines[['left','top','right']].set_visible(False)
        ax[1].spines[['left','top','right']].set_visible(False)
        ax[0].set_title(f"Intervalos de {coluna} com {coluna_alvo}", fontsize=10, fontweight='bold')
        ax[1].set_title("Quantidade de valores", fontsize=10, fontweight='bold')
        plt.show()
    else:
        fig, ax = plt.subplots(nrows=2,figsize=(9,7), tight_layout=True)
        sns.boxplot(data=base,x=coluna,y=coluna_alvo,ax=ax[0],showmeans=True)
        sns.histplot(base[coluna],ax=ax[1])
        a = base[coluna].value_counts()
        for i in range(len(a.index)):
            ax[1].annotate(a.values[i],(a.index[i], a.values[i]+a.values[i]*0.02),ha='center')
        ax[1].yaxis.set_visible(False)
        ax[0].spines[['left','top','right']].set_visible(False)
        ax[1].spines[['left','top','right']].set_visible(False)
        ax[0].tick_params(axis='x', rotation=45)
        ax[1].tick_params(axis='x', rotation=45)
        ax[0].set_title(f"Intervalos de {coluna} com {coluna_alvo}", fontsize=14, fontweight='bold')
        ax[1].set_title("Quantidade de valores", fontsize=14, fontweight='bold')
        plt.show()