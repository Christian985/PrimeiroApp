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
        idade = datetime.date.today() - ano_nascimento
        if 0 > idade < 18:
            'Menor de idade.'
        elif idade >= 18:
            'Maior de idade.'
        else:
            'A idade é inválida.'
        txt_resultado.value = f'Resultado = {idade}'
        page.update()

    # Fields

    num1 = ft.TextField(label="Digite seu ano de nascimento" )
    btn_enviar = ft.FilledButton(text="Enviar",
                                 width=page.window.width,
                                 on_click=mostrar_resultado,
                                 )

    txt_resultado = ft.Text("")

    # Componentes

    page.add(
        ft.Column(
            [
                num1,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)