import flet as ft


def main(page: ft.Page):

    
    opciones = ft.Dropdown(options=[
            ft.dropdown.Option('Valencia'),
            ft.dropdown.Option('Madrid'),
            ft.dropdown.Option('Barcelona'),
            ft.dropdown.Option('Sevilla'),
        ]
    )


    def activate_boton(e):
        boton_login.disabled = caja_texto.value ==''
        page.update()        

        

    def press_button(e):
        if check_box.value:
            login_text.value = 'Logueado con exito' 
        else:    
            login_text.value = "Error tienes que aceptar las condiciones"
  
        page.update()



    check_box = ft.Checkbox()
    caja_texto = ft.TextField(on_change=activate_boton, value='')

    titulo = ft.Text('Formulario registro', width="bold", size=30)
    titulo_dos = ft.Text('Datos personales', width="bold", size=25)
    row_nom_celda = ft.Row([ft.Container(ft.Text('Nombre', size=20)), caja_texto,])
    row_direccion_celda = ft.Row([ft.Container(ft.Text('Direccion', size=20)), caja_texto,])
    row_provincia_combo = ft.Row([ft.Container(ft.Text('Provincia', size=20)), opciones,]) 
    titulo_tres = ft.Text('Datos de acceso', width="bold", size=25)
    usuario = ft.Row([ft.Container(ft.Text('Usuario', size=20)), caja_texto,])
    password = ft.Row([ft.Container(ft.Text('Password', size=20)), ft.TextField(password=True, can_reveal_password=True),])
    condiciones_uso = ft.Row([ft.Container(ft.Text('Acepto las condiciones del servicio ')), check_box])
    boton_login = ft.ElevatedButton(text='Login', on_click=press_button, disabled=True)
    login_text = ft.Text()


    

    page.add(
        titulo,
        titulo_dos,
        row_nom_celda,
        row_direccion_celda,
        row_provincia_combo,
        titulo_tres,
        usuario,
        password,
        condiciones_uso,
        boton_login,
        login_text,
    )
        
    


ft.app(target=main)
