import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.dropdown import Option, Dropdown
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
                    AppBar(title=Text('Aposentadoria'), bgcolor=Colors.PRIMARY_CONTAINER),
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
                        input_idade,
                        menu,
                        tempo_contribuicao,
                        media_salarial,
                        tipo_aposentadoria,
                        ElevatedButton(text='Idade', on_click=lambda _: page.go('/sim_resultados_idade')),
                        ElevatedButton(text='Contribuição', on_click=lambda _: page.go('/sim_resultados_contribuicao')),
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
        elif page.route == '/sim_resultados_idade':
            page.views.append(
                View(
                    '/sim_resultados_idade',
                    [
                        AppBar(title=Text('Aposentadoria por Idade'), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value=f'Idade:  {input_idade.value}'),
                        Text(value=f'Gênero: {menu.value}'),
                        Text(value=f'Tempo de Contribuição: {tempo_contribuicao.value}'),
                        Text(value=f'Média Salárial: {media_salarial.value}'),
                        Text(value=f'Tipo de Aposentadoria: {tipo_aposentadoria.value}'),
                        Text(value=f'Resultado : {calcu}'),
                        Text(value=txt_resultado),

                    ],
                )
            )
        elif page.route == '/sim_resultados_contribuicao':
            page.views.append(
                View(
                    '/sim_resultados_contribuicao',
                    [
                        AppBar(title=Text('Aposentadoria por Contribuição'), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value=f'Idade:  {input_idade.value}'),
                        Text(value=f'Gênero: {menu.value}'),
                        Text(value=f'Tempo de Contribuição: {tempo_contribuicao.value}'),
                        Text(value=f'Média Salárial: {media_salarial.value}'),
                        Text(value=f'Tipo de Aposentadoria: {tipo_aposentadoria.value}'),
                        Text(value=f'Resultado gggggggggggg: {calcu}'),

                    ],
                )
            )
        page.update()


    def calcu(e):
        sua_idade = int(input_idade.value)
        genero = menu.value
        contribuicao = int(tempo_contribuicao.value)


        if sua_idade == 65 and contribuicao == 15:
            txt_resultado.value = 5
            page.update()

        elif sua_idade == 62 and contribuicao == 15:
            txt_resultado = 9
            page.update()

    txt_resultado = ""


    # Função que configura o botão 'voltar'
    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    # Configurações de alternativa

    menu = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        fill_color=Colors.RED,
        options=[Option(key='Masculino', text='Masculino'), Option(key='Feminino', text='Feminino')],
    )
    tipo_aposentadoria = ft.Dropdown(
        label="Tipo de Aposentadoria",
        width=page.window.width,
        fill_color=Colors.RED,
        options=[Option(key='Idade', text='Idade'), Option(key='cont', text='Tempo de contribuição')],
    )

    # Segunda Página - Simulador de aposentadoria
    input_idade = ft.TextField(label='Idade', hint_text='Digite sua idade')
    tempo_contribuicao = ft.TextField(label='Tempo de Contribuição', hint_text='Digite seus anos de contribuição')
    media_salarial = ft.TextField(label='Média Salarial', hint_text='Digite sua média salarial de pelo menos 5 anos')

    # Terceira Página - Regras de Aposentadoria
    regras = ft.Text('Aposentadoria por Idade:\n\nHomens: 65 anos de idade e pelo menos 15 anos de contribuição.\n\n'
                               'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n\nAposentadoria por Tempo '
                               'de Contribuição:\n\nHomens: 35 anos de contribuição.\n\nMulheres: 30 anos de contribuição.\n\n'
                               'Valor Estimado do Benefício:\nO valor da aposentadoria será uma média de 60% da média '
                               'salarial informada, acrescido de 2% por ano que exceder o tempo '
                               'mínimo de contribuição.')

    # Quarta Página - Resultados
    txt_resultado = ft.Text("")


    # Evento para chamar a função
    page.on_view_pop = voltar

    # Evento para chamar a função que gerencia as rotas.
    page.on_route_change = gerencia_rotas

    page.go(page.route)

ft.app(main)
