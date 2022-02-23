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

    limit = 100

    df_qs_11 = df_qs_11.head(limit)
    df_qs_12 = df_qs_12.head(limit)
    df_qs_13 = df_qs_13.head(limit)
    df_qs_14 = df_qs_14.head(limit)
    df_qs_15 = df_qs_15.head(limit)
    df_qs_16 = df_qs_16.head(limit)
    df_qs_17 = df_qs_17.head(limit)
    df_qs_18 = df_qs_18.head(limit)
    df_qs_19 = df_qs_19.head(limit)
    df_qs_20 = df_qs_20.head(limit)
    df_qs_21 = df_qs_21.head(limit)

    df = pd.concat([df_qs_11, df_qs_12, df_qs_13, df_qs_14, df_qs_15,
                    df_qs_16, df_qs_17, df_qs_18, df_qs_19, df_qs_20, df_qs_21])
    return df


def archivo_limpio(file):
    '''
    file = str ruta del excel
    Esta funcion limpia el archivo, ademas de que crea el data frame
    '''
    import pandas as pd
    df = lectura(file)
    # Limpiar los rangos
    df['Rank'] = df['Rank'].fillna(method='ffill')
    df['O_Rank'] = df['O_Rank'].fillna(method='ffill')
    df['AR Rank'] = df['AR Rank'].fillna(method='ffill')
    df['ER Rank'] = df['ER Rank'].fillna(method='ffill')
    df['FS Rank'] = df['FS Rank'].fillna(method='ffill')
    df['CF Rank'] = df['CF Rank'].fillna(method='ffill')
    df['IF Rank'] = df['IF Rank'].fillna(method='ffill')
    df['IS Rank'] = df['IS Rank'].fillna(method='ffill')
    # Limpiar las reputaciones
    df['Academic Reputation'] = df['Academic Reputation'].fillna(
        df['Academic Reputation'].mean)
    df['Employer Reputation'] = df['Employer Reputation'].fillna(
        df['Employer Reputation'].mean)
    # Limpiar faculty
    df['Faculty Student'] = df['Faculty Student'].fillna(
        df['Faculty Student'].median)
    df['Citations per Faculty'] = df['Citations per Faculty'].fillna(
        df['Citations per Faculty'].median)
    df['International Faculty'] = df['International Faculty'].fillna(
        df['International Faculty'].median)
    df['International Faculty'] = df['International Faculty'].fillna(
        df['International Faculty'].median)
    df['International Students'] = df['International Students'].fillna(
        df['International Students'].median)
    # Limpiar el overall
    df['Overall Score'] = df['Overall Score'].fillna(df['Overall Score'].mean)
    df = df.replace('601+', int(601))
    return df


def leer_subjects(path):
    import pandas as pd
    with open('./src/areas.txt', 'r') as f:
        areas = f.readlines()
    df = pd.DataFrame()
    for i in range(len(areas)):
        try:
            df = pd.concat(
                [df, pd.read_excel(path, sheet_name=areas[i].replace('\n', ''))])
        except ValueError:
            print(
                "La hoja ", areas[i], " no fue encontrada, checa el excel o el areas.txt")

    return df
