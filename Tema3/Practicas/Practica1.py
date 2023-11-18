import flet as ft


class App:

    def __init__(self) -> None:
        ft.app(target=self.main)
        ...
        

    def main(self, page: ft.Page):
        self.page = page
        page.title = 'juego cartas'
        

    
        def items(count):
            items = []
            for i in range(1, count + 1):
                items.append(
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=120,
                        height=120,
                        bgcolor=ft.colors.AMBER,
                        border_radius=ft.border_radius.all(5),
                        ink=True,
                        on_click=lambda e: on_click(self,e),
                        
                    )
                )
            return items
        
        
        
        
        def on_click(self,e):
            page.views.append(
                ft.View('/comprobar',
                        [
                            ft.Text('Has pulsado el boton '),
                            e.control.content,
                            ft.ElevatedButton('Retroceder',
                                              on_click=lambda _: page.go('/'))
                        ]
                    )
            )
            



            e.control.bgcolor = 'green'

            page.update()


        row = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(25),
        width=page.window_width,
        )


        
        page.add(
            ft.Text('Numeros'),
            row,
            ft.ElevatedButton(text='reiniciar',disabled=True)
        )

        page.update()
        

if __name__ == "__main__":
    app = App()