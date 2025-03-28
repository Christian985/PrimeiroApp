import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View


# Configuração inicial.
def main(page: ft.Page):
    page.title = 'Exemplo de Rotas'
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.WHITE
    page.window.width = 375
    page.window.height = 667

# Função para gerenciar as telas.
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text('Home'), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text='Navegar', on_click=lambda _: page.go('/segunda')),
                ],
            )
        )
        if page.route == '/segunda':
            page.views.append(
                View(
                    '/segunda',
                    [
                        AppBar(title=Text('Segunda tela'), bgcolor=Colors.SECONDARY_CONTAINER),
                    ],
                )
            )
        page.update()

    # Função que configura o botão 'voltar'
    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Evento para chamar a função
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar


    # Evento para chamar a função que gerencia as rotas.
    page.on_route_change = gerencia_rotas

    page.go(page.route)

ft.app(main)