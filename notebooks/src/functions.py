from plistlib import InvalidFileException
from time import time

import pandas as pd


def leer(path, limit=250):
    '''
    Parameters

    path La ruta del archivo excel
    limit Hasta que universidad tomara

    Returns

    Un dataframe con todos los años

    '''
    inicio = time()
    df_raw = pd.DataFrame()
    for i in range(2011, 2022):
        try:
            df_raw = pd.concat([df_raw, pd.read_excel(
                path, sheet_name=str(i)).head(limit)])
        except FileNotFoundError:
            print('Archivo no encontrado')
            return None
        except KeyboardInterrupt:
            print(
                f"Detuviste la lectura, pasaron: {time()-inicio:.2f} segundos")
            return None
    print(f'Lectura exitosa, tiempo total: {time()-inicio:.2f} segundos')
    return df_raw


def limpiar(path, limite=250):
    '''
    Parameters

    path La ruta del archivo excel
    limite Hasta que universidad tomara

    Returns

    Un dataframe limpio

    '''
    df = leer(path, limite)
    try:
        # Limpiar los rangos
        df['Rank'] = df['Rank'].fillna(method='ffill')
        df['O_Rank'] = pd.to_numeric(df['O_Rank'], errors='coerce')
        df['O_Rank'] = df['O_Rank'].fillna(method='ffill')
        df['AR Rank'] = pd.to_numeric(df['AR Rank'], errors='coerce')
        df['AR Rank'] = df['AR Rank'].fillna(method='ffill')
        df['ER Rank'] = pd.to_numeric(df['ER Rank'], errors='coerce')
        df['ER Rank'] = df['ER Rank'].fillna(method='ffill')
        df['FS Rank'] = df['FS Rank'].fillna(method='ffill')
        df['CF Rank'] = df['CF Rank'].fillna(method='ffill')
        df['IF Rank'] = df['IF Rank'].fillna(method='ffill')
        df['IS Rank'] = df['IS Rank'].fillna(method='ffill')
        # Limpiar las reputaciones
        df['Academic Reputation'] = df['Academic Reputation'].fillna(
            df['Academic Reputation'].mean)
        df['Employer Reputation'] = pd.to_numeric(
            df['Employer Reputation'], errors='coerce')
        df['Employer Reputation'] = df['Employer Reputation'].fillna(
            df['Employer Reputation'].mean())
        # Limpiar faculty
        df['Faculty Student'] = pd.to_numeric(
            df['Faculty Student'], errors='coerce')
        df['Faculty Student'] = df['Faculty Student'].fillna(
            df['Faculty Student'].median())
        df['Citations per Faculty'] = df['Citations per Faculty'].fillna(
            df['Citations per Faculty'].median())
        df['International Students'] = df['International Students'].fillna(
            df['International Students'].median())
        df['International Faculty'] = pd.to_numeric(
            df['International Faculty'], errors='coerce')
        df['International Faculty'] = df['International Faculty'].fillna(
            df['International Faculty'].median())
        # Limpiar el overall
        df['Overall Score'] = df['Overall Score'].fillna(
            df['Overall Score'].mean())
        df = df.replace('601+', int(601))
    except TypeError:
        print('Error en la lectura')
        return None
    return df
