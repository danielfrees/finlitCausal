""" 
Functions for finlit data cleaning and prep and scoring.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys 
import math
import io
from config import COLUMN_MAP, TREATMENT_COLS, COVARIATES, OUTCOME_VARS

def na_drop(x):
    if type(x) == str:
        return x.strip() == ""
    return False

def load_data(dir = '2021-SxS-Data-and-Data-Info',
              file = 'NFCS_2021_State_Data.csv'):
    """ 
    Load in the financial literacy dataset.

    Map columns to more verbose useful column names.
    """
    DATASET = os.path.join(dir, file)
    df = pd.read_csv(DATASET)
    col_list = list(df.columns)
    col_list = [COLUMN_MAP[col].strip() if col in COLUMN_MAP else col.strip() for col in col_list]
    df.columns = col_list

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace('', np.nan, inplace=True)
    df.replace(np.nan, 4.5, inplace=True)
    df.fillna(4.5, inplace=True)
    df = df.astype(int)
    df.replace(98, 4.5, inplace = True)
    df.replace(99, 4.5, inplace=True)

    assert df.map(lambda x: pd.isna(x)).sum().sum() == 0

    assert (df.values == 98).sum() == 0 
    assert (df.values == 99).sum() == 0 
    
    return df

def get_finhealth_score(df,
                         scale_vals: bool = False):
    """ 
    Given OUTCOME_VARS in df, compute a single score for financial health (higher = better).
    
    Remap col values as appropriate.
    
    Scale col weights for roughly balanced effect of each col relative to its severity.
    """
    # Define mappings for each variable
    mappings = {
        'SATISFACTION_WITH_FINANCIAL_CONDITION': lambda x: x-1,
        'SPENDING_COMPARISON_TO_INCOME': {1: 9, 2: 4.5, 3: 0},
        'DIFFICULTY_COVERING_EXPENSES': {1: 0, 2: 4.5, 3: 9},
        'EMERGENCY_FUNDS': {1: 9, 2: 0},
        'CONFIDENCE_GET_2000': {1: 9, 2: 6, 3: 3, 4: 0},
        'CREDIT_RECORD_RATING': {1: 0, 2: 2.25, 3:4.5, 4:6.75, 5: 9},
        'CHECKING_ACCOUNT': {1: 9, 2: 0},
        'SAVINGS_ACCOUNT': {1: 9, 2: 0},
        'OVERDRAW_CHECKING_ACCOUNT': {1: 0, 2: 9},
        'REGULAR_CONTRIBUTION_TO_RETIREMENT': {1: 9, 2: 0},
        'OTHER_INVESTMENTS': {1: 9, 2: 0},
        'ALWAYS_PAY_CR_FULL_12MO': {1: 9, 2: 0},
        'USED_PAYDAY_LOAN': {1: 9, 2: 3, 3: 2, 4: 1},
        'DEBT_COLLECTED_12MO': {1: 0, 2: 9},
        'TOO_MUCH_DEBT_STRENGTH': {1: 9, 2: 7.5, 3: 6, 4: 4.5, 5: 3, 6: 1.5, 7: 0},
        'D2D_FINANCIAL_SKILL': lambda x: (x - 1) * 1.5,
        'FINANCIAL_KNOWLEDGE_ASSESS': lambda x: (x - 1) * 1.5,
    }

    # Apply mappings to the DataFrame columns
    for varname, mapping in mappings.items():
        if callable(mapping):
            df[varname] = df[varname].apply(lambda x: mapping(x))
        else:
            df[varname] = df[varname].map(mapping).fillna(4.5)

    if scale_vals:
        score_scale_map = {
            'SATISFACTION_WITH_FINANCIAL_CONDITION': lambda x: x * 1,
            'SPENDING_COMPARISON_TO_INCOME': lambda x: x * 1,
            'DIFFICULTY_COVERING_EXPENSES': lambda x: x * 1,
            'EMERGENCY_FUNDS': lambda x: x * 0.5,
            'CONFIDENCE_GET_2000': lambda x: x * 0.5,
            'CREDIT_RECORD_RATING': lambda x: x * 1,
            'CHECKING_ACCOUNT': lambda x: x * 0.25,
            'SAVINGS_ACCOUNT': lambda x: x * 0.25,
            'OVERDRAW_CHECKING_ACCOUNT': lambda x: x * 0.5,
            'REGULAR_CONTRIBUTION_TO_RETIREMENT': lambda x: x * 1,
            'OTHER_INVESTMENTS': lambda x: x * 0.75,
            'ALWAYS_PAY_CR_FULL_12MO': lambda x: x * 1,
            'USED_PAYDAY_LOAN': lambda x: x * 1.25,
            'DEBT_COLLECTED_12MO': lambda x: x * 0.5,
            'TOO_MUCH_DEBT_STRENGTH': lambda x: x * 2,
            'D2D_FINANCIAL_SKILL': lambda x: x * 1,
            'FINANCIAL_KNOWLEDGE_ASSESS': lambda x: x * .5,
        }
        for varname, mapping in score_scale_map.items():
            df[varname] = df[varname].apply(lambda x: mapping(x))


    # Sum the scores for each row
    df['overall_financial_score'] = df[OUTCOME_VARS].sum(axis=1)

    return df['overall_financial_score']


def clean_data(df: pd.DataFrame, 
               write_cols: bool = False, 
               scale_vals: bool = False, 
               treat_type: str = 'hs'):
    """ 
    Subset the data and perform some operations.
    """

    if write_cols: 
        with open('columns.txt', 'wb') as file:
            file.write('\n'.join(df.columns).encode('utf-8'))
    
    def binarize_treat_hs(t):
        if int(t) == 2:
            return 0 
        elif int(t) == 1:
            return 1
        else:
            return 999     #not a treat or control

    def binarize_treat_all(t):
        if int(t) == 2:
            return 1
        elif int(t) == 1 or int(t) == 3:
            return 0
        else:
            return 999     #not a treat or control

    # Use .loc to avoid SettingWithCopyWarning
    
    if treat_type == 'hs':
        df = df[df['FIN_ED_HS'].isin([1, 2])]
        df['Z'] = df.loc[:, 'FIN_ED_HS'].map(binarize_treat_hs)
    elif treat_type == 'all':
        df = df[df['FIN_ED_ALL'].isin([1, 2, 3])]
        df['Z'] = df.loc[:, 'FIN_ED_ALL'].map(binarize_treat_all)
    else:
        print("treat_type must be 'hs' or 'all'")
    df['FIN_HEALTH'] = get_finhealth_score(df, scale_vals=scale_vals)

    all_cols = []
    all_cols.extend(OUTCOME_VARS)
    all_cols.extend(COVARIATES)
    all_cols.extend(TREATMENT_COLS)
    all_cols.append('Z')
    all_cols.append('FIN_HEALTH')
    df = df.loc[:, all_cols]
    
    return df


def visualize_data(df: pd.DataFrame):
    """ 
    Visualize the covariates and the treatment variable distributions.
    """
    num_covariates = len(COVARIATES)
    num_cols = 3  # Number of columns in the subplot grid
    num_rows = math.ceil(num_covariates / num_cols)

    # Create the first figure for covariates
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 15))
    fig.subplots_adjust(hspace=0.5)

    # Visualize covariates with pie charts
    for i, covariate in enumerate(COVARIATES):
        row, col = divmod(i, num_cols)
        ax = axes[row, col]
        df[covariate].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
        ax.set_title(f'{covariate} Distribution')

    # Remove empty subplots if there are extras
    for i in range(num_covariates, num_rows*num_cols):
        row, col = divmod(i, num_cols)
        fig.delaxes(axes[row, col])

    plt.show()

    plt.figure(figsize=(8, 8))

    # Visualize the treatment variable with a pie chart
    ax2 = plt.gca()
    df['Z'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax2)
    ax2.set_title('Treatment Distribution')

    plt.show()

    # Fin health (outcome)
    plt.figure(figsize=(8, 8))

    # Visualize the treatment variable with a pie chart
    ax2 = plt.gca()
    df['FIN_HEALTH'].hist(bins=100)
    ax2.set_title('Outcome Dist')

    plt.show()