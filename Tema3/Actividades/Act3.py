import flet as ft

num_column = int(input('Numero de botones en columna: '))
num_row = int(input('Numero de botones en fila: '))

v = 'V'
h = 'H'

def main(page: ft.Page):


    def num_botones(count, letra):
        num_botones = []
        for i in range(1, count + 1):
            num_botones.append(
                ft.Container(
                    content=ft.Text(value=(letra + str(i))),
                    alignment=ft.alignment.center,
                    width=75,
                    height=75,
                    bgcolor=ft.colors.BLUE,
                )
            )
        return num_botones
    

    
    #column = ft.Column(controls=num_botones(num_column,v))
    #row = ft.Row(controls=num_botones(num_row,h))
    
    page.window_height = num_column * 75 + num_column * 10 + 10
    page.window_width = (num_row + 1) * 75 + num_row * 10 + 20
    

    page.add(
        ft.Row(
            [
                ft.Container(
                    ft.Column(
                        controls=num_botones(num_column,v),
                        #spacing=0,
                        
                        )
                ),
                ft.Container(
                    ft.Row(
                        controls=num_botones(num_row,h),
                        #spacing=0,
                        
                        )
                ),
            ],

        ),
    )
    

ft.app(target=main)