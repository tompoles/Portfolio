import pandas as pd
data = pd.ExcelFile('resultxlm.xlsx')

def ReshapeFunc(excel_obj, i):
    tabnames = data.sheet_names
    assert i < len(tabnames), "Your tab index exceeds the number of available tabs, try a lower number"
    # parse and clean columns
    df = excel_obj.parse(sheetname=tabnames[i], skiprows=0)
    cols1 = list(df.columns)
    cols1 = [str(x)[:21] for x in  cols1]
    df.columns = cols1
    df = df.drop(['lists/3/name','lists/3/rank','meta/ceo', 'meta/industry',
              'meta/previousRank', 'meta/rank', 'tables/0/data/0/name',
              'tables/0/data/1/name','tables/0/data/2/name', 'tables/0/data/3/name',
              'tables/0/data/4/name', 'tables/0/data/5/name', 'tables/0/data/6/name',
              'tables/0/name','tables/1/data/0/name','tables/1/data/0/value','tables/1/data/1/name',
              'tables/1/data/1/value', 'tables/1/data/2/name','tables/1/data/2/value','tables/1/data/3/name',
              'tables/0/data/6/value','tables/1/name', 'tables/2/data/0/name', 'tables/2/data/1/name',
              'tables/2/data/2/name', 'tables/2/name'
              ], axis=1).iloc[0:,:].rename(columns=
                                                {'highlights/0/value': 'Revenues ($M)',
                                                 'highlights/1/value': 'Revenue Change',
                                                 'highlights/2/value': 'Profits ($M)',
                                                 'highlights/3/value': 'Assets ($M)',
                                                 'highlights/4/value': 'Profit Change',
                                                 'highlights/5/value': 'Total employees',
                                                 'tables/0/data/0/value':'CEO',
                                                 'tables/0/data/1/value':'Sector',
                                                 'tables/0/data/2/value':'Industry',
                                                 'tables/0/data/3/value':'HQ Location',
                                                 'tables/0/data/4/value':'Website',
                                                 'tables/0/data/5/value':'Years on Global 500 List',
                                                 'tables/1/data/3/value':'Total Stockholder Equity ($M)',
                                                 'tables/2/data/0/value':'Profit as % of Revenues',
                                                 'tables/2/data/1/value':'Profits as % of Assets',
                                                 'tables/2/data/2/value':'Profits as % of Stockholder Equity',
                                                 'title':'Company name'})
    to_remove = [c for c in df.columns if 'descript' in c]
    to_remove_2 = [c for c in df.columns if 'title' in c]
    # to_change = [c for c in df.columns if 'title' in c]
    df.drop(to_remove, axis=1, inplace=True)
    df.drop(to_remove_2, axis=1, inplace=True)
    # for c in to_change:
    #     df[c] = df[c].apply(lambda x: pd.to_numeric(x))

    idx = ['Company name','Industry','Sector']
    multi_indexed_df = df.set_index(idx)
    stack_df = multi_indexed_df.stack(dropna=False)

    # long_df = stack_df.reset_index()
    # df_final = long_df

    return(stack_df)
check_df = ReshapeFunc(data, 0)
print(check_df)


# Concate and Save
dfs_list = [ReshapeFunc(data, i) for i in range(1)]
concat_dfs = pd.concat(dfs_list)
concat_dfs.to_excel('reshaped_data.xlsx')



