import pandas as pd
import numpy as np

df = pd.read_excel('../data/raw/proteomics.xlsx')
md = pd.read_excel('../data/raw/metadata.xlsx')

df = df.drop(['entry_name', 'accession_number'], axis=1)

df
md.columns = md.iloc[0,:]

# Cleaning metadata for this analysis
md = pd.read_excel('data/raw/metadata.xlsx')
md.columns = md.iloc[0,:]
md.drop(index=[0], axis=0)

