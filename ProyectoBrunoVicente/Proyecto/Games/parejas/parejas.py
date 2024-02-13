import flet as ft
import random
import time
import threading
from carta import Carta
import os

class MainMenu:
    def __init__(self, page):
        self.page = page
        page.title = "MEMORY"
        page.vertical_alignment= ft.MainAxisAlignment.CENTER
        page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    def start(self):
        title = ft.Text('MEMORY', size=30, color=ft.colors.RED, weight=ft.FontWeight.BOLD)
        self.page.add(title)
        play_button = self.page.add(ft.ElevatedButton('Jugar', scale=1.2, bgcolor=ft.colors.GREEN, on_click=self.play_game))
        

    def play_game(self, event):
        self.page.clean()
        title = ft.Text('Elige la dificultad', size=30, color=ft.colors.RED, weight=ft.FontWeight.BOLD)
        self.page.add(title)
        easy_button = ft.ElevatedButton('Fácil', scale=1.2, bgcolor=ft.colors.GREEN, on_click=lambda event: self.start_game(8))
        normal_button = ft.ElevatedButton('Normal', scale=1.2, bgcolor=ft.colors.YELLOW, on_click=lambda event: self.start_game(16))
        hard_button = ft.ElevatedButton('Difícil', scale=1.2, bgcolor=ft.colors.RED, on_click=lambda event: self.start_game(24))
        self.page.add(easy_button, normal_button, hard_button)

    def start_game(self, num_cards):
        self.page.clean()
        game = MemoryGame(self.page, num_cards)
        game.start()



class MemoryGame:
    ruta = os.path.abspath(__file__)
    def __init__(self, page, num_cards):
        self.page = page
        self.num_cards = num_cards
        self.ultimas_cartas = []
        self.bloqueo = False
        self.parejas_encontradas = 0

        self.dlg = ft.AlertDialog(
            content=ft.Text("Felicidades, has terminado el juego"),
            actions=[
                ft.TextButton("Volver a jugar", on_click=(lambda event: self.play_again(self.num_cards))),
                ft.TextButton("Inicio", on_click=(lambda event: self.return_menu()))
            ]
        )
 
    def close_dlg(self):
        self.dlg.open = False
        self.page.update()

    def play_again(self,num_cards):
        time.sleep(0.5)
        self.page.clean()
        self.page.update()
        game = MemoryGame(self.page, num_cards)
        game.start()
        self.close_dlg()

    def return_menu(self):
        self.page.clean()
        self.page.update()
        menu = MainMenu(self.page)
        menu.start()
        self.close_dlg()

    def open_dlg(self):
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()
    

    def items(self, count):
        items = []
        valores = list(range(1, count//2 + 1)) * 2
        random.shuffle(valores)
        for valor in valores:
            carta = Carta(valor)
            sw = ft.AnimatedSwitcher(
                ft.Image(src=os.path.join(self.ruta,'/Figuras/tarjeta.png'), width=140, height=200),
                transition=ft.AnimatedSwitcherTransition.SCALE,
                duration=500,
                reverse_duration=500,
                switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
                switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
            )
            
            container = ft.Container(
                content=sw,
                alignment=ft.alignment.center,
                width=140,
                height=200,
                bgcolor=ft.colors.WHITE,
                border_radius=ft.border_radius.all(5),
                border=ft.border.all(10, color=ft.colors.RED_900),
            )
            container.on_click = (lambda sw=sw, carta=carta: lambda event: self.build(sw, carta))()
            items.append(container)
            
        return items

    def build(self, sw, carta):
        if self.bloqueo or carta.revelada:
            return

        if len(self.ultimas_cartas) == 2:
            ultima_carta1, ultima_sw1 = self.ultimas_cartas.pop()
            ultima_carta2, ultima_sw2 = self.ultimas_cartas.pop()
            if ultima_carta1.obtener_valor() != ultima_carta2.obtener_valor():
                def ocultar():
                    time.sleep(0.5)
                    self.ocultar_cartas(ultima_carta1, ultima_sw1, ultima_carta2, ultima_sw2)
                threading.Thread(target=ocultar).start()
            else:
                carta.revelar()
                sw.content = ft.Image(
                    src=os.path.join(f"/Figuras/{carta.obtener_valor()}.png"), width=140, height=200
                )
                self.ultimas_cartas.append((carta, sw))
                self.page.update()
        else:
            carta.revelar()
            sw.content = ft.Image(
                src=os.path.join(f"/Figuras/{carta.obtener_valor()}.png"), width=140, height=200
            )
            self.ultimas_cartas.append((carta, sw))
            self.page.update()
            if len(self.ultimas_cartas) == 2:
                self.bloqueo = True 
                def ocultar():
                    time.sleep(0.5)
                    ultima_carta1, ultima_sw1 = self.ultimas_cartas.pop()
                    ultima_carta2, ultima_sw2 = self.ultimas_cartas.pop()
                    if ultima_carta1.obtener_valor() == ultima_carta2.obtener_valor():
                        self.parejas_encontradas += 1
                        if self.parejas_encontradas == self.num_cards // 2:  
                            self.open_dlg()
                            
                    else:
                        self.ocultar_cartas(ultima_carta1, ultima_sw1, ultima_carta2, ultima_sw2)
                    self.bloqueo = False 
                threading.Thread(target=ocultar).start()

    def obtener_parejas_encontradas(self):
        return self.parejas_encontradas
    
    def ocultar_cartas(self, carta1, sw1, carta2, sw2):
        carta1.ocultar()
        carta2.ocultar()
        sw1.content = ft.Image(
            src=os.path.join(os.path.join(self.ruta,'../Figuras/tarjeta.png')), width=140, height=200
        )
        sw2.content = ft.Image(
            src=os.path.join(os.path.join(self.ruta,'../Figuras/tarjeta.png')), width=140, height=200
        )
        self.page.update()

    def start(self):
        row = ft.Row(
            wrap=True,
            spacing=10,
            run_spacing=10,
            controls=self.items(self.num_cards),
            width=self.page.window_width,
        )

        self.page.add(row)

def main(page: ft.Page):
    menu = MainMenu(page)
    menu.start()

ft.app(target=main)