import flet as ft


def main(page: ft.Page):
    page.title = "Par ou impar"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK👌
    page.window.width = 375
    page.window.height = 667



    def mostrar_resultado(e):
        par_impar = int(num1.value) % 2
        if par_impar == 0:
            txt_resultado.value = f'Número Par: {num1.value}'
        else:
            txt_resultado.value = f'Número Impar: {num1.value}'

        page.update()


    num1 = ft.TextField(label="Digite um número" )
    btn_enviar = ft.FilledButton(text="Enviar",
                                 width=page.window.width,
                                 on_click=mostrar_resultado,
                                 )
    txt_resultado = ft.Text(value="")


    page.add(
        ft.Column(
            [
                num1,
                btn_enviar,
                txt_resultado
            ]
        )
    )


ft.app(main)