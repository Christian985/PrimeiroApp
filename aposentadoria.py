import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.view import View


# Configuração inicial.
def main(page: ft.Page):
    page.title = 'Aposentadoria'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.WHITE
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
                    input_idade,
                    menu,
                    tempo_contribuicao,
                    media_salarial,
                    ElevatedButton(text='Simular aposentadoria', on_click=lambda _: page.go('/sim_aposentar')),
                    ElevatedButton(text='Regras aposentadoria', on_click=lambda _: page.go('/regras')),
                ],
            )
        )
        if page.route == '/sim_aposentar':
            page.views.append(
                View(
                    '/sim_aposentar',
                    [
                        AppBar(title=Text('Simular Aposentadoria'), bgcolor=Colors.SECONDARY_CONTAINER),
                        ElevatedButton(text='Mostrar resultados', on_click=lambda _: page.go('/resultados')),
                    ],
                )
            )
        elif page.route == '/regras':
            page.views.append(
                View(
                    '/regras',
                    [
                        AppBar(title=Text('Regras da Aposentadoria'), bgcolor=Colors.SECONDARY_CONTAINER),
                        regras
                    ],
                )
            )
        elif page.route == '/sim_resultados':
            page.views.append(
                View(
                    '/sim_resultados',
                    [
                        AppBar(title=Text('Resultados de Aposentadoria'), bgcolor=Colors.SECONDARY_CONTAINER),
                        regras
                    ],
                )
            )
        page.update()

    # Função que configura o botão 'voltar'
    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    menu = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        fill_color=Colors.RED,
        options=[Option(key='Masc', text='Masculino'), Option(key='Fe', text='Feminino'), Option(key='Av', text='Avião')],
    )

    # Primeira Página - Início
    input_idade = ft.TextField(label='Idade', hint_text='Digite sua idade')
    tempo_contribuicao = ft.TextField(label='Tempo de Contribuição', hint_text='Digite seus anos de contribuição')
    media_salarial = ft.TextField(label='Média Salarial', hint_text='Digite sua média salarial')

    # Segunda Página - Simulador de aposentadoria


    # Terceira Página - Regras de Aposentadoria
    regras = ft.Text('Aposentadoria por Idade:\n\nHomens: 65 anos de idade e pelo menos 15 anos de contribuição.\n'
                               'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\nAposentadoria por Tempo '
                               'de Contribuição: Homens: 35 anos de contribuição.\nMulheres: 30 anos de contribuição.\n\n'
                               'Valor Estimado do Benefício:\n\nO valor da aposentadoria será uma média de 60% da média'
                               'salarial informada, acrescido de 2% por ano que exceder o tempo'
                               'mínimo de contribuição.')

    # Quarta Página - Resultados

    # Evento para chamar a função
    page.on_view_pop = voltar

    # Evento para chamar a função que gerencia as rotas.
    page.on_route_change = gerencia_rotas

    page.go(page.route)

ft.app(main)
