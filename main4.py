import flet as ft


# Configuração

def main(page: ft.Page):
    page.title = "Calculadora "
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções

    def somar(e):
        soma = int(num1.value) + int(num2.value)
        txt_resultado.value = f'Resultado = {soma}'
        page.update()


    def subtrair(e):
        subtrai = int(num1.value) - int(num2.value)
        txt_resultado.value = f'Resultado = {subtrai}'
        page.update()



    def multiplicar(e):
        multiplica = int(num1.value) * int(num2.value)
        txt_resultado.value = f'Resultado = {multiplica}'
        page.update()


    def dividir(e):
        divide = int(num1.value) / int(num2.value)
        txt_resultado.value = f'Resultado = {divide}'
        page.update()




    # Botões

    num1 = ft.TextField(label='digite um numero')
    num2 = ft.TextField(label='digite um numero')

    btn_soma = ft.FilledButton(text="Somar",
                               on_click=somar)

    btn_subtrai = ft.FilledButton(text="Subtrair",
                                  on_click=subtrair)

    btn_multiplica = ft.FilledButton(text="Multiplicar",
                                     on_click=multiplicar)

    btn_divide = ft.FilledButton(text="Dividir",
                                 on_click=dividir)


    txt_resultado = ft.Text("")

    # Componentes

    page.add(
        ft.Column(
            [
                num1,
                num2,
                btn_soma,
                btn_subtrai,
                btn_multiplica,
                btn_divide,
                txt_resultado,
            ]
        )
    )


ft.app(main)