from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg


def subir_solucion(sudoku):
    for row in sudoku:
        for ele in row:
            pg.press(str(ele))
            pg.press("right")
        pg.press("down")
        pg.press("left", presses=8)
        
    print("Ya todo esta listo")
    return
    


#RESOLVER SUDOKU
def leer_ny_sudoku(dificultad="hard"):
    
    driver = webdriver.Chrome()
    url = "https://www.nytimes.com/puzzles/sudoku/" + dificultad
    print(f"Leyendo SUDOKU desde {url}")
    driver.get(url)
    
    sudoku_dict = {}
    grid = driver.find_elements(By.CLASS_NAME, 'su-board')
    for el in grid:
        cells = el.find_elements(By.TAG_NAME, "div")
        for cell in cells:
            cell_number = cell.get_attribute("data-cell")
            cell_value = cell.get_attribute("aria-label")
            if cell_number is not None and cell_value is not None:
                sudoku_dict[int(cell_number)] = 0 if cell_value == "empty" else int(cell_value)
    #print(sudoku_dict)



    #Pasarlo a la estructura de datos que necesitamos
    sudoku = []
    x = 0
    y = 0
    for i in range(81):
        if x == 9:
            y +=1
            x = 0
        if x == 0:
            sudoku.append([])
            
        sudoku[y].append(sudoku_dict[i])
        x += 1
    print_sudoku(sudoku)
    print()
    return sudoku


def sudoku_manual():
     sudoku = [[0,0,1,3,0,2,0,0,0],
          [0,0,0,8,1,0,0,4,2],
          [0,9,0,0,0,0,3,0,0],
          [3,0,7,6,9,8,1,2,0],
          [1,0,6,2,0,5,4,7,9],
          [5,0,9,0,4,0,0,0,0],
          [0,1,0,0,0,6,0,9,3],
          [0,6,4,0,0,0,2,5,0],
          [0,0,2,0,8,0,0,0,0]]
     return sudoku


def print_sudoku(sudoku):
    for l in sudoku:
        print(l)

def encontrar_coordenad_grid(val):
    if val <=2:
        return 0
    elif val <=5:
        return 1
    else:
        return 2

def obtener_grid_para_celda(x, y, sudoku):
    subgrid_col = encontrar_coordenad_grid(x)
    subgird_fila = encontrar_coordenad_grid(y)
    
    
    grid = []
    for fila in sudoku[subgird_fila *3: subgird_fila *3 + 3]:
        for col in fila[subgrid_col *3: subgrid_col *3 +3]:
            grid.append(col)    

    return grid

def es_posible(x, y, v, sudoku):
    #revisar la fila
    if v in sudoku[y]:
        return False
    #revisar la columna
    col =[fila[x] for fila in sudoku]
    if v in col:
        return False
    #revisar sub grid 3x3
    grid3x3 = obtener_grid_para_celda(x, y, sudoku)
    if v in grid3x3:
        return False
    
    
    return True
    
    


def resolver_sudoku(sudoku):
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0:
            
                for valor in range(1,10):
                    
                   if es_posible(columna, fila, valor, sudoku):
                       sudoku[fila][columna] = valor
                       resuelto =resolver_sudoku(sudoku)
                       if resuelto:
                           return True
                       sudoku[fila][columna] = 0 
                
                return False
    # print("Esta es la solución a tu SUDOKU")
    # print_sudoku(sudoku)
    return True
                    
# leer_ny_sudoku()
sudoku = leer_ny_sudoku()
            
resuelto =resolver_sudoku(sudoku)
if resuelto:
    print("Solución encontrada:")
    print_sudoku(sudoku)
    subir_solucion(sudoku)
else:
    print("No pudo solucionarlo, verifique si su internet esta funcionando")
# es_posible(6, 8, 3, sudoku)