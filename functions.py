import pandas as pd
import itertools
from collections import ChainMap


def read_in_excel(path_to_sheet):
    
    # Read in excel file
    xls_file = pd.ExcelFile(path_to_sheet) 
    
    # Each sheet should be a treatment.
    treatments = xls_file.sheet_names
    
    # One dataframe per treatment (= sheet)
    df = {treatment: pd.read_excel(path_to_sheet, header=None, sheet_name = treatment) for treatment in treatments}
    return df, treatments

def clean_df1(df):
    """ Removes NA values from dataframe and reset index  """
    
    tmp_df = df.dropna(how='all')
    tmp_df = tmp_df.dropna(axis=1, how='all')
    df = tmp_df.reset_index(drop=True)
    df.columns = range(df.shape[1])

    return df


def getIndexes(df, variable):
    """ Get index positions (column) of the variable in dataframe i.e. df that we created earlier """
 
    listOfPos = list()
    # Get bool dataframe with True at positions where the given variable exists
    result = df.isin([variable])
    # Get list of columns that contains the variable
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where variable exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of variable in the dataframe
    return listOfPos



def clean_df2(df, listofPos):
    """ Extracts the variable of interest and all of its data from the dataframe. """
    
    # The second element in the tuple defines the column where the variable is located
    column_idx = listofPos[0][1]
    new_df = df[[0,column_idx]]
    return new_df


def subs_dataframe(df, listOfPos):
    "Makes a subset for each dataframe there is and stores it in a big nested dictionary."
    
    # Dict that contains all separate dictionaries per treatment
    big_dict = dict()
    
    length_plates = len(listOfPos)
    for i in range(length_plates):
        index,value = listOfPos[i]
        begin = index
    
        #define end of subdataframe
        if  i+1 < length_plates:
            end = listOfPos[i+1][0]
        else:
            end = len(df)
    
        tmp_df = pd.DataFrame()
        tmp_df = df[begin:end]
        
        # Make nested dict with all separate dataframes per treatment
        big_dict[i] = tmp_df

    return big_dict

def restructure_df(df, treatment):
    """ Restructuring the dataframe ready for the transfer to prism format. """
    df = df.reset_index(drop=True)
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])

    # groups
    groups = list(df.iloc[:,0].unique())
    transf = dict()
    for group in groups:
        group_data = []
        for index, row in df.iterrows():
            if row[0] == group:
                group_data.append(row[1])
        transf[group] = group_data

    return transf 



def dict_to_prism_format(dictionary, treatments):
    """
    from dictionary to pandas dataframe where groups (WT,KO, etc) are in one long row
    each treatment is one row
    """
    
    df = pd.DataFrame()
    for i in dictionary.keys():
        data = dictionary[i]

        column_names = []
        values = []

        for key in data.keys():
            tmp_column_names = [key + str(i) for i in range(1, len(data[key]) + 1)]
            column_names.extend(tmp_column_names)
            values.extend(data[key])

        if df.empty:
            df = pd.DataFrame(values, column_names).T
        else: 
            tmp_df = pd.DataFrame(values, column_names).T
            df = df.append(tmp_df, ignore_index = True, sort=False)

            
    #Rename rows & columns
    d = dict(ChainMap(*[{col + str(i): col for i in range(1, len(vals) + 1)} for col, vals in dictionary[treatments[0]].items()]))
    df.columns = pd.MultiIndex.from_tuples([*zip(map(d.get, df), df)])
    
    [df.rename(index = {index:key}, inplace = True) for key, index in zip(dictionary.keys(), range(len(dictionary.items())))]

    return df

def plant_data_prism(dataset, variable, name_excel):
    """
    This function restructures a dataset (excel sheet) into a Prism friendly format:
    Inputs: 
    - dataset: the link to dataset (e.g. "path/to/dataset.xls")
    - variable: values of this parameter will be taken into accou
    In plant datasets the treatments are usually based on the plates where the plants grew.
    ATM you can only have one plate with one treatment but as many treatments as you like. 
    """
    
    # Read excel file
    ori_df, sheets = read_in_excel(dataset)
    
    treatment_df = dict()
    for sheet in sheets:
        tmp_df = ori_df[sheet]
        
        # First cleaning
        df = clean_df1(tmp_df)
        
        # Select indeces of the variable for each dataframe
        listOfPos = getIndexes(df, variable)
        
        # New dataframe with only the groups name (first column) and variable of interest (second column)
        df = clean_df2(df, listOfPos)
        
        # Makes a subset dataframe
        df_dict = subs_dataframe(df, listOfPos)
        
        # Restructuring the data ready to parse
        tmp_df = {i: restructure_df(df_dict[i], variable) for i in range(len(listOfPos))}
        new_df = {}
        for i in tmp_df.keys():
            for key, value in tmp_df[i].items():
                try: 
                    new_df[key].extend(value)
                except KeyError:
                    new_df[key] = value
        # Save each parsing in a dictionary (key = treatment, and value = subdataframe )
        treatment_df[sheet] = new_df
    
    # Reformat of the dictionary to dataframe in the required Prism format
    df = dict_to_prism_format(treatment_df, sheets)
    
    # Write to excel based on name in the (third) input
    df.to_excel(name_excel + ".xlsx")

    return df
