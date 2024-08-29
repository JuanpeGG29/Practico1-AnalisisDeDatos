import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('permisos_construccion_2.csv')  # 43 columnas

if __name__ == "__main__":

    # Parte 2
    print(data.info())

    # a. Calcular y mostrar la cantidad de filas y columnas
    filas, columnas = data.shape
    print(f"Cantidad de filas: {filas}")
    print(f"Cantidad de columnas: {columnas}")

    # b. Observar y mostrar las primeras 5 filas
    print("\nPrimeras 5 filas del dataset:")
    print(data.head())

    # c. Datos faltantes y duplicados
    datos_faltantes = data.isnull().sum()
    porcentaje_faltantes = (datos_faltantes / filas) * 100
    print("\nDatos faltantes por columna:")
    print(datos_faltantes[datos_faltantes > 0])
    print("\nPorcentaje de datos faltantes por columna:")
    print(porcentaje_faltantes[porcentaje_faltantes > 0])

    #fias duplicadas
    total_filas = len(data)
    duplicados = data.duplicated()
    numero_duplicados = duplicados.sum()
    porcentaje_duplicados = (numero_duplicados / total_filas) * 100
    print(f"Número total de filas: {total_filas}")
    print(f"Número de filas duplicadas: {numero_duplicados}")
    print(f"Porcentaje de filas duplicadas: {porcentaje_duplicados:.2f}%")

    if numero_duplicados > 0:
        print(data[duplicados].head())


    # d. Evaluar posibles motivos de datos faltantes
        print("\nEvaluacion de posibles motivos de datos faltantes: Los datos con mayor faltante en porcentualmente son: treet Number Suffix  ")

    # Aqui podrias anadir un analisis mas detallado dependiendo del contexto de las columnas
    
    '''
    for columna in datos_faltantes.index[datos_faltantes > 0]:
        print(f"\nColumna: {columna}")
        # Ver distribucion de datos faltantes
        print(data[columna].value_counts(dropna=False))
    '''




    # g. Evaluar la existencia de datos inconsistentes
    print("\nEvaluacion de datos inconsistentes:")
    # Verifica el tipo de datos de cada columna
    print(data.dtypes)
    #verificacion de datos numericos
    for col in data.select_dtypes(include=['number']).columns:
        print(f"Resumen de valores en la columna {col}:")
        print(data[col].describe())  # Esto te da un resumen estadístico para detectar posibles outliers o valores erróneos
        print("\n")
    print('pete')
    #Revision de valores unicos 
    for col in data.select_dtypes(include=['object']).columns:
        print(f"Valores únicos en la columna {col}:")
        print(data[col].value_counts())
        print("\n")





    #4.
    # Aqui puedes anadir chequeos adicionales, por ejemplo, verificar si existen valores fuera de un rango esperado
    #Respecto a las columnas con muchos datos faltantes, decidimos eliminarlas ya que la informacion que tienen es poco util
    # Columnas a eliminar debido a datos faltantes
    columnas_a_eliminar = ['Street Number Suffix', 'Unit Suffix', 'Voluntary Soft-Story Retrofit', 'Fire Only Permit', 'TIDF Compliance', 'Site Permit']
    data = data.drop(columns=columnas_a_eliminar)
    print(data.columns)
    #faltaria decidir que hacer en el caso de que los datos faltantes sean pocos pero igualmente significativos


    # Eliminar espacios al principio y al final de las cadenas en las columnas relevantes para reducir incosistencias
    data['Permit Type Definition'] = data['Permit Type Definition'].str.strip()
    data['Existing Construction Type Description'] = data['Existing Construction Type Description'].str.strip()
    # Normalizar los nombres de calles a un formato consistente para reducir inconsistencias
    data['Street Name'] = data['Street Name'].str.lower()
    # Corregir valores en la columna 'Supervisor District' 
    data['Supervisor District'].replace({'quince': 15, 'veinte': 20, 'diez': 10}, inplace=True)
    #normalizar
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = data[col].str.strip()  # Eliminar espacios al principio y al final
        data[col] = data[col].str.lower()  # Convertir todo a minúsculas (opcional)

    total_filas = len(data)
    duplicados = data.duplicated()
    numero_duplicados = duplicados.sum()
    porcentaje_duplicados = (numero_duplicados / total_filas) * 100
    print(f"Número total de filas: {total_filas}")
    print(f"Número de filas duplicadas: {numero_duplicados}")
    print(f"Porcentaje de filas duplicadas: {porcentaje_duplicados:.2f}%")


    # o valores que no tienen sentido dentro del contexto de las variables.
