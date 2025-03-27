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
        nascimento = int(input(num1.value))
        data_atual = 100
        idade = data_atual - nascimento
        if idade < 0:
            'A idade é inválida.'
        elif 0 > nascimento < 18:
            'Menor de idade.'
        elif nascimento >= 18:
            'Maior de idade.'
        txt_resultado.value = f'Resultado = {idade}'
        page.update()

    # Fields

    num1 = ft.TextField(label="Digite um número" )
    nascimento = ft.TextField(label='Digite o seu ano de nascimento')
    btn_enviar = ft.FilledButton(text="Enviar",
                                 width=page.window.width,
                                 on_click=mostrar_resultado,
                                 )

    txt_resultado = ft.Text("")

    # Componentes

    page.add(
        ft.Column(
            [
                nascimento,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)