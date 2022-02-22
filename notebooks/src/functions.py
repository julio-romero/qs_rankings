def lectura(excel):
    '''
    excel = Nombre de la ruta donde se encuentra este excel
    esta funcion se creo por conveniencia, sino la quieres usar esta bien :
    '''
    import pandas as pd
    df_qs_11 = pd.read_excel(excel, sheet_name='2011')
    df_qs_12 = pd.read_excel(excel, sheet_name='2012')
    df_qs_13 = pd.read_excel(excel, sheet_name='2013')
    df_qs_14 = pd.read_excel(excel, sheet_name='2014')
    df_qs_15 = pd.read_excel(excel, sheet_name='2015')
    df_qs_16 = pd.read_excel(excel, sheet_name='2016')
    df_qs_17 = pd.read_excel(excel, sheet_name='2017')
    df_qs_18 = pd.read_excel(excel, sheet_name='2018')
    df_qs_19 = pd.read_excel(excel, sheet_name='2019')
    df_qs_20 = pd.read_excel(excel, sheet_name='2020')
    df_qs_21 = pd.read_excel(excel, sheet_name='2021')
    df = pd.concat([df_qs_11, df_qs_12, df_qs_13, df_qs_14, df_qs_15,
                    df_qs_16, df_qs_17, df_qs_18, df_qs_19, df_qs_20, df_qs_21])
    return df
