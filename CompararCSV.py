import pandas as pd

def find_unique_elements(list1, list2):
    unique_in_list1 = set(list1).difference(list2)
    unique_in_list2 = set(list2).difference(list1)

    return list(unique_in_list1), list(unique_in_list2)

def main():
    # Listas de ejemplo con diferentes tamaños
    datos1 = pd.read_csv("Prueba1.csv")

    datos2 = pd.read_csv("Prueba2")

    lista1 = datos1["Version"].values.tolist()
    
    lista2 = datos2["Version"].values.tolist()

    # Encontrar elementos únicos en cada lista
    unique_in_list1, unique_in_list2 = find_unique_elements(lista1, lista2)

    # Crear DataFrames con los resultados
    unique_in_list1_df = pd.DataFrame({'Elementos Únicos en Lista 1': unique_in_list1})
    unique_in_list2_df = pd.DataFrame({'Elementos Únicos en Lista 2': unique_in_list2})

    # Guardar los DataFrames en archivos CSV
    unique_in_list1_df.to_csv('Prueba1.csv', index=False)
    unique_in_list2_df.to_csv('unique_in_Prueba2.csv', index=False)

if __name__ == "__main__":
    main()
