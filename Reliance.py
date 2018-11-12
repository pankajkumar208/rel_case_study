# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:24:47 2018

@author: admin
"""

import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   # Provides a high level interface for drawing attractive and informative statistical graphics
%matplotlib inline
sns.set()

from subprocess import check_output


cust_profile_data = pd.read_excel("F:/Reliance Assignment/Analytical Interview DATASET.XLSX", sheet_name='Customer Profile Data (DS#1)')
past_purchase_data = pd.read_excel("F:/Reliance Assignment/Analytical Interview DATASET.XLSX", sheet_name='Past Purchase Data (Ds#2)')
campaign_coverage_data = pd.read_excel("F:/Reliance Assignment/Analytical Interview DATASET.XLSX", sheet_name='Campaign Coverage Data (DS#3)')
month_level_cust_data = pd.read_excel("F:/Reliance Assignment/Analytical Interview DATASET.XLSX", sheet_name='Month Level Customer Data (DS#4')
socio_economic_data = pd.read_excel("F:/Reliance Assignment/Analytical Interview DATASET.XLSX", sheet_name='Socio Economic Data (DS#5)')

# checking columns
cust_profile_data.columns
past_purchase_data.columns
campaign_coverage_data.columns
month_level_cust_data.columns
socio_economic_data.columns

# checking missing values in all data

cust_profile_data.isnull().sum()
# Previous_Default_Flag    1082
# Loan_Availed_Flag         116
# Do missing value treatment

past_purchase_data.isnull().sum()
# Customer_ID              1
# Loyalty_Tier             1
# Delete this one row as customer id is NA

campaign_coverage_data.isnull().sum()
# no missing values

month_level_cust_data.isnull().sum()
# no missing values

socio_economic_data.isnull().sum()
# no missing values

pandas_profiling.ProfileReport(cust_profile_data)