import flet as ft

def main(page: ft.Page):
    page.title = "Lista Compra"
    counter = 1
    lista_articulos = ft.ListView()

    def guardar_click(e):
        with open('lista_compra.txt', 'w') as f:
            for row_articulo in lista_articulos.controls:
                if isinstance(row_articulo, ft.Row):
                    nombre_articulo = ', '.join(map(str, row_articulo.controls[0].value))
                    f.write(nombre_articulo + '\n')

    
    
    def add_clicked(e):
        

        def delete_click(e):
            lista_articulos.controls.remove(row_articulo)  # Eliminar el Row del ListView
            page.update()

        row_articulo = ft.Row([ft.Text([compra.value,tipo.value,counter], size=20), ft.IconButton(ft.icons.DELETE, on_click=delete_click)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        lista_articulos.controls.append(row_articulo)
        compra.value = ''
        add_articulo.disabled = True
        compra.focus()
        page.update()

    
    
    def check_value(e):
        add_articulo.disabled = compra.value == ''
        page.update()

    def subtract_click(e):
        nonlocal counter
        counter -= 1
        texto_contador.value = str(counter)
        page.update() # Actualizamos la vista 

    def add_click(e):
        nonlocal counter
        counter += 1
        texto_contador.value = str(counter)
        page.update() # Actualizamos la vista      


    
    compra = ft.TextField(
        hint_text="Articulo", width=300, on_change=check_value, expand=True)
    tipo = ft.Dropdown(
        options=[
            ft.dropdown.Option("Alimentacion"),
            ft.dropdown.Option("Higiene"),
            ft.dropdown.Option("Limpieza"),
            ft.dropdown.Option("Oficina"),
            ft.dropdown.Option("Otros"),
        ],
    )

    texto_contador = ft.Text(str(counter))
    contador = ft.Row([ft.IconButton(ft.icons.REMOVE, on_click=subtract_click), texto_contador, ft.IconButton(ft.icons.ADD, on_click=add_click)])
    add_articulo = ft.ElevatedButton(
        "Afegir", on_click=add_clicked, disabled=True)
    articulo =ft.Row([compra,tipo,contador, add_articulo], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    boton_guardar = ft.ElevatedButton("GUARDAR", on_click=guardar_click)




    page.add(articulo,lista_articulos, ft.Row([boton_guardar], alignment=ft.MainAxisAlignment.END)) 
    
ft.app(target=main)    