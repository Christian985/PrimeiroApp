import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View


# Configuração inicial.
def main(page: ft.Page):
    page.title = 'Rota de livro'
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
                    AppBar(title=Text('Cadastrar Livro'), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(text='Navegar', on_click=lambda _: page.go('/segunda')),
                ],
            )
        )
        if page.route == '/segunda':
            page.views.append(
                View(
                    '/segunda',
                    [
                        AppBar(title=Text('Livro Cadastrado'), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value= f'Titulo do livro: {input_nome.value}'),
                        Text(value= f'Descrição do livro: {input_descricao.value}'),
                        Text(value= f'Categoria do livro: {input_categoria.value}'),
                        Text(value= f'Autor do livro: {input_autor.value}'),
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

    page.update()
    input_nome = ft.TextField(label='Nome', hint_text='Digite o nome do livro')
    input_descricao = ft.TextField(label='Descrição', hint_text='Digite a descrição do livro')
    input_categoria = ft.TextField(label='Categoria', hint_text='Digite a categoria do livro')
    input_autor = ft.TextField(label='Autor', hint_text='Digite o autor do livro')

ft.app(main)