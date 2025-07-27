import numpy as np
import pandas as pd
from collections import defaultdict

def get_expression_data(
        data:pd.DataFrame,
        isoforms:bool=False
        ) -> pd.DataFrame:
    
    processed = data.drop(['accession_number'], axis=1)

    duplicates = data['geneSymbol'].value_counts()
    duplicate_symbols = duplicates[duplicates > 1].index.tolist()
    print(f'{len(duplicate_symbols)} gene symbols have multiple protein isoforms')

    # Strategy 1 - Keep highest expressed isoform
    if isoforms is False:

        num_cols = processed.columns[2:]
        processed['Average'] = processed[num_cols].mean(axis=1)
        processed = processed.loc[processed.groupby('geneSymbol')['Average'].idxmax()]
        processed = processed.drop(columns=['Average'])
        processed = processed.reset_index(drop=True)
    
    # Strategy 2 - Keep unique isoforms
    else:

        counters = defaultdict(int)
        new_values = []
        
        for symbol in processed['geneSymbol']:
            if symbol in duplicate_symbols:
                counters[symbol] += 1
                new_values.append(f"{symbol}_{counters[symbol]}")
            else:
                new_values.append(symbol)
        
        isoform_series = pd.Series(new_values, index=processed.index)
        processed['geneSymbol'] = isoform_series

    # Symbol to name mappings:
    symbol2name = processed[['geneSymbol', 'entry_name']]
    processed = processed.drop(columns=['entry_name'])

    return processed, symbol2name

def get_expression_matrix(
        expr_data: pd.DataFrame,
        index_col: str='geneSymbol'
) -> pd.DataFrame:
    
    expr_mat = expr_data.set_index(index_col)

    return expr_mat

