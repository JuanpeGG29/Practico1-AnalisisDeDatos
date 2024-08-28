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

    duplicados = data.duplicated().sum()
    porcentaje_duplicados = (duplicados / filas) * 100
    print(f"\nCantidad de filas duplicadas: {duplicados}")
    print(f"Porcentaje de filas duplicadas: {porcentaje_duplicados:.2f}%")

    # d. Evaluar posibles motivos de datos faltantes
    print("\nEvaluacion de posibles motivos de datos faltantes:")

    # Aqui podrias anadir un analisis mas detallado dependiendo del contexto de las columnas

    '''
    for columna in datos_faltantes.index[datos_faltantes > 0]:
        print(f"\nColumna: {columna}")
        # Ver distribucion de datos faltantes
        print(data[columna].value_counts(dropna=False))
    '''

    # e. Valores unicos de variables discretas
    # Lista de variables discretas categóricas seleccionadas
categoricas = [
    'Permit Type Definition', 'Street Suffix', 'Current Status',
    'Structural Notification', 'Voluntary Soft-Story Retrofit', 'Fire Only Permit',
    'Existing Use', 'Proposed Use', 'TIDF Compliance',
    'Existing Construction Type Description', 'Proposed Construction Type Description',
    'Site Permit', 'Supervisor District', 'Neighborhoods - Analysis Boundaries'
]

print("\nValores únicos de las variables discretas categóricas:")

# Imprimir solo los valores únicos de las columnas categóricas seleccionadas
for columna in categoricas:
    print(f"\nColumna: {columna}")
    print(data[columna].unique())


# f. Cuantificar valores unicos y realizar histogramas
n = 20  # Número máximo de valores únicos a mostrar
print("\nCuantificacion de valores unicos y generacion de histogramas:")
for columna in data.select_dtypes(include=['object']).columns:
    print(f"\nColumna: {columna}")
    unique_values = data[columna].value_counts()
    # Mostrar solo los primeros n valores únicos
    print(unique_values.head(n))

    plt.figure(figsize=(10, 5))
    sns.countplot(y=columna, data=data, order=unique_values.head(n).index)
    plt.title(f'Frecuencia de valores en {columna}')

    plt.show()

# g. Evaluar la existencia de datos inconsistentes
print("\nEvaluacion de datos inconsistentes:")
# Aqui puedes anadir chequeos adicionales, por ejemplo, verificar si existen valores fuera de un rango esperado
# o valores que no tienen sentido dentro del contexto de las variables.
