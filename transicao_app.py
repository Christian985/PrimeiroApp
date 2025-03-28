import flet as ft

# Configuração inicial.
def main(page: Page):
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
                    AppBar(title=Text('Home'), bgcolor=Color.PRIMARY_CONTAINER),
                ],
            )
        )
        page.update()

    # Evento para chamar a função que gerencia as rotas.
    page.on_route_change = gerencia_rotas

    page.go(page.route)