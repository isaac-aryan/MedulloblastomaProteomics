import pandas as pd
import numpy as np

from ingestion import get_expression_matrix, get_expression_data

# Ingesting data
df = pd.read_excel('../data/raw/proteomics.xlsx')
md = pd.read_excel('../data/raw/metadata.xlsx')

# Processing expression data
expression_data, symbol_mappings = get_expression_data(data=df, isoforms=False)
matrix = get_expression_matrix(expression_data)
