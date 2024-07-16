# Sudoku Solver
Este proyecto es una aplicación que resuelve automáticamente los sudokus del New York Times utilizando Selenium para la automatización del navegador, y pyautogui para la entrada de datos. La solución se implementa en Python y resuelve el Sudoku utilizando un algoritmo de backtracking.

### Características Principales
Funcionalidad de la Aplicación
Lectura del Sudoku desde NY Times:

La función leer_ny_sudoku(dificultad) usa Selenium para abrir el navegador y navegar a la página de Sudoku del New York Times en la dificultad especificada (por defecto es "hard").
Extrae la información del tablero utilizando selectores de clase y atributos HTML, y construye una estructura de datos (una lista de listas) que representa el Sudoku.
Solución del Sudoku:

La función resolver_sudoku(sudoku) implementa un algoritmo de backtracking para resolver el Sudoku. Esta función intenta llenar cada celda vacía (representada por 0) con un número del 1 al 9 que no rompa las reglas del Sudoku (números únicos en cada fila, columna y subcuadrícula de 3x3).
La función es_posible(x, y, v, sudoku) verifica si un valor puede colocarse en una celda dada sin violar las reglas del Sudoku.
Subir la Solución:

La función subir_solucion(sudoku) utiliza pyautogui para simular la entrada del teclado y llenar el tablero de Sudoku en el navegador con la solución obtenida.
Descripción de las Funciones
leer_ny_sudoku(dificultad="hard"): Abre la página de Sudoku del New York Times y lee el tablero. Devuelve una lista de listas que representa el Sudoku.
print_sudoku(sudoku): Imprime el Sudoku en un formato legible.
encontrar_coordenad_grid(val): Devuelve el índice de la subcuadrícula 3x3 para un valor dado.
obtener_grid_para_celda(x, y, sudoku): Devuelve la subcuadrícula 3x3 que contiene la celda en (x, y).
es_posible(x, y, v, sudoku): Verifica si es posible colocar el valor v en la celda (x, y) sin violar las reglas del Sudoku.
resolver_sudoku(sudoku): Implementa el algoritmo de backtracking para resolver el Sudoku.
subir_solucion(sudoku): Usa pyautogui para llenar el tablero de Sudoku en el navegador con la solución obtenida.
sudoku_manual(): Proporciona un tablero de Sudoku de ejemplo para pruebas manuales.
### Flujo del Programa
El programa comienza leyendo un Sudoku desde la página del New York Times con leer_ny_sudoku().
Luego, intenta resolver el Sudoku usando resolver_sudoku(sudoku).
Si se encuentra una solución, se imprime en la consola y se sube al navegador usando subir_solucion(sudoku).
### Cómo Ejecutarlo
Requisitos Previos:

Python 3.x
Selenium
WebDriver para el navegador que prefiera (por defecto se usa Chrome)
pyautogui
Instalación de Dependencias:

bash
Copiar código
pip install selenium pyautogui
Ejecución del Programa:

Asegúrese de que el WebDriver (por ejemplo, chromedriver) esté en su PATH o en el mismo directorio que el script.
Ejecute el script principal:
bash
Copiar código
python sudoku_solver.py
Configuración del Navegador:

Asegúrese de que el navegador Chrome esté instalado y que el WebDriver sea compatible con su versión de Chrome.
Puede cambiar el navegador o la configuración del WebDriver modificando la parte de inicialización en leer_ny_sudoku.
