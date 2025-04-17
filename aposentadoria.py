import flet as ft
from flet.core.app_bar import AppBar
from flet.core.colors import Colors
from flet.core.dropdown import Option, Dropdown
from flet.core.elevated_button import ElevatedButton
from flet.core.image import Image
from flet.core.text import Text
from flet.core.view import View
import datetime

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
                        ElevatedButton(text='Idade', on_click= lambda _:calcu(e)),
                        ElevatedButton(text='Contribuição', on_click=lambda _: calcu_tempo_contribuicao(e)),
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
                        Text(value=f'Média Salarial: {media_salarial.value}'),
                        Text(value=f'Resultado: {txt_resultado.value}'),
                        txt_data_aposentadoria,

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
                        txt_data_aposentadoria,
                        txt_aposentar
                    ],
                )
            )
        page.update()


    # Calculo da idade
    def calcu(e):
        data_atual = datetime.datetime.today().year
        data_aposentadoria = int(input_idade.value) + int(data_atual)
        valor_genero = menu.value
        valor_idade = int(input_idade.value)
        valor_salario = int(media_salarial.value)
        aposentar = "Você já pode se aposentar!"
        # Caso seja masculino e possa aposentar
        if valor_idade > 65 and valor_genero == 'Masculino':
            percentual = 60 + (valor_idade - 15) * 2
            resultado = valor_salario * (percentual / 100)
            print(f"{valor_idade}% de {valor_salario} é {resultado}")
            txt_resultado.value = resultado
            txt_aposentar.value = aposentar

        # Caso seja masculino e não possa aposentar
        elif valor_idade < 65 and valor_genero == 'Masculino':
            percentual = 60 + (valor_idade - 15) * 2
            resultado = valor_salario * (percentual / 100)
            print(f"{valor_idade}% de {valor_salario} é {resultado}")
            txt_resultado.value = resultado
            txt_data_aposentadoria.value = f'Você poderá se aposentar em: {data_aposentadoria}'

        # Caso seja feminino
        elif valor_idade > 62 and valor_genero == 'Feminino':
            percentual = 60 + (valor_idade - 15) * 2
            resultado = valor_salario * (percentual / 100)
            print(f"{valor_idade}% de {valor_salario} é {resultado}")
            txt_resultado.value = resultado
        page.update()
        page.go('/sim_resultados_idade')

    # Calculo do tempo de contribuição
    def calcu_tempo_contribuicao(e):
        valor_genero = menu.value
        valor_contribuicao = int(tempo_contribuicao.value)
        valor_salario = int(media_salarial.value)
        # Caso seja masculino
        if valor_contribuicao > 35 and valor_genero == 'Masculino':
            percentual = 60 + (valor_contribuicao - 15) * 2
            resultado = valor_salario * (percentual / 100)
            print(f"{valor_contribuicao}% de {valor_salario} é {resultado}")
            txt_resultado.value = resultado
        # Caso seja feminino
        elif valor_contribuicao > 30 and valor_genero == 'Feminino':
            percentual = 60 + (valor_contribuicao - 15) * 2
            resultado = valor_salario * (percentual / 100)
            print(f"{valor_contribuicao}% de {valor_salario} é {resultado}")
            txt_resultado.value = resultado
        page.update()
        page.go('/sim_resultados_contribuicao')


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
    txt_data_aposentadoria = ft.Text("")
    txt_aposentar = ft.Text("")


    # Evento para chamar a função
    page.on_view_pop = voltar

    # Evento para chamar a função que gerencia as rotas.
    page.on_route_change = gerencia_rotas

    page.go(page.route)

ft.app(main)
