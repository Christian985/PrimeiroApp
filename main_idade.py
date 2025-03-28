import flet as ft

import datetime
# Configuração

def main(page: ft.Page):
    page.title = "Verificação de idade"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667



    # Funções

    def mostrar_resultado(e):
        ano_nascimento = num1.value
        mes_nascimento = num2.value
        dia_nascimento = num3.value

        idade_ano = datetime.date.today().year - int(ano_nascimento)
        idade_mes = datetime.date.today().month - int(mes_nascimento)
        idade_dia = datetime.date.today().day - int(dia_nascimento)

        # Ano
        if 0 > idade_ano < 18:
            'Menor de idade.'
            txt_resultado.value = f'Resultado = {idade_ano}'
        elif idade_ano >= 18:
            'Maior de idade.'
            txt_resultado.value = f'Resultado = {idade_ano}'
        else:
            'A idade é inválida.'

        # Mês
        if idade_mes <= 12:
            txt_resultado.value = f'Resultado = {idade_mes}'
        elif idade_mes >= 12:
            'Mês inválido.'

        # Dia
        if idade_dia <= 30:
            txt_resultado.value = f'Diferença em dias = {idade_dia}'
        elif idade_dia >= 30:
            'Dia Inválido.'


        page.update()



    # Fields

    num1 = ft.TextField(label="Digite seu ano de nascimento" )
    num2 = ft.TextField(label="Digite seu mês de nascimento" )
    num3 = ft.TextField(label="Digite seu dia de nascimento" )
    btn_enviar = ft.FilledButton(text="Calcular",
                                 width=page.window.width,
                                 on_click=mostrar_resultado,
                                 )

    txt_resultado = ft.Text("")



    # Componentes

    page.add(
        ft.Column(
            [
                num1,
                num2,
                num3,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)