import pandas as pd
import numpy as np

from ingestion import get_expression_matrix, process_expression_data

df = pd.read_excel('../data/raw/proteomics.xlsx')
md = pd.read_excel('../data/raw/metadata.xlsx')

# Working on metadata processing
md.columns = md.iloc[0,:]

# Cleaning metadata for this analysis
md = pd.read_excel('data/raw/metadata.xlsx')
md.columns = md.iloc[0,:]
md.drop(index=[0], axis=0)


# Processing expression data
expression_data, symbol_mappings = process_expression_data(data=df, isoforms=False)

expression_data
symbol_mappings

matrix = get_expression_matrix(expression_data)
matrix.head()