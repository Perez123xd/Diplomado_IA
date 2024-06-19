import graphviz

# Crear un nuevo diagrama de flujo
dot = graphviz.Digraph(comment='Proceso de Medición de Humedad en el Invernadero')

# Inicio
dot.node('Inicio', 'Inicio: El programa comienza su ejecución.')

# Leer número de puntos de medición
dot.node('Leer_puntos', 'Leer número de puntos de medición: Se solicita al usuario que ingrese la cantidad de puntos de medición de humedad en el invernadero.')

# Inicializaciones
dot.node('Init_niveles_humedad', 'Inicializar lista niveles_humedad: Se crea una lista vacía llamada niveles_humedad para almacenar los niveles de humedad de cada punto.')
dot.node('Init_necesitan_riego', 'Inicializar necesitan_riego en 0: Se crea una variable llamada necesitan_riego y se inicializa en 0.')
dot.node('Init_i', 'Inicializar i en 0: Se crea una variable i (contador) y se inicializa en 0.')

# Condicional i < num_puntos?
dot.node('Cond_i_num_puntos', 'i < num_puntos?', shape='diamond')

# Leer nivel de humedad
dot.node('Leer_nivel_humedad', 'Leer nivel de humedad del punto i+1: Se lee el nivel de humedad del siguiente punto de medición.')
dot.node('Agregar_nivel_humedad', 'Agregar nivel de humedad a niveles_humedad: El nivel de humedad leído se agrega a la lista niveles_humedad.')

# Condicional humedad < 30?
dot.node('Cond_humedad_30', 'humedad < 30?', shape='diamond')

# Incrementar necesitan_riego
dot.node('Incrementar_necesitan_riego', 'Incrementar necesitan_riego: Se suma 1 a la variable necesitan_riego.')

# Incrementar i
dot.node('Incrementar_i', 'Incrementar i: Se suma 1 al contador i para pasar al siguiente punto de medición.')

# Imprimir resultados
dot.node('Imprimir_resultados', 'Imprimir número de puntos que necesitan riego: Se muestra en pantalla el valor final de la variable necesitan_riego.')

# Fin
dot.node('Fin', 'Fin: El programa termina su ejecución.')

# Definir las conexiones
dot.edge('Inicio', 'Leer_puntos')
dot.edge('Leer_puntos', 'Init_niveles_humedad')
dot.edge('Init_niveles_humedad', 'Init_necesitan_riego')
dot.edge('Init_necesitan_riego', 'Init_i')
dot.edge('Init_i', 'Cond_i_num_puntos')

dot.edge('Cond_i_num_puntos', 'Leer_nivel_humedad', label='Si')
dot.edge('Cond_i_num_puntos', 'Imprimir_resultados', label='No')

dot.edge('Leer_nivel_humedad', 'Agregar_nivel_humedad')
dot.edge('Agregar_nivel_humedad', 'Cond_humedad_30')

dot.edge('Cond_humedad_30', 'Incrementar_necesitan_riego', label='Si')
dot.edge('Cond_humedad_30', 'Incrementar_i', label='No')

dot.edge('Incrementar_necesitan_riego', 'Incrementar_i')
dot.edge('Incrementar_i', 'Cond_i_num_puntos')

dot.edge('Imprimir_resultados', 'Fin')

# Mostrar el diagrama de flujo
dot.render('/mnt/data/diagrama_flujo_humedad', format='png', cleanup=True)
'/mnt/data/diagrama_flujo_humedad.png'
