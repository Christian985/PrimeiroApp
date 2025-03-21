import flet as ft


# Configuração

def main(page: ft.Page):
    page.title = "Verificação de idade"
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções

    def idade_real(e):
        soma = int(num1.value) + int(num2.value)
        txt_resultado.value = f'Resultado = {soma}'
        page.update()


    # def mostrar_resultado(e):
    #
    #     par_impar = int(num1.value) % 2
    #     if par_impar == 0:
    #         txt_resultado.value = f'Número par {num1.value}'
    #     else:
    #         txt_resultado.value = f'Número impar {num1.value}'
    #
    #     page.update()


    num1 = ft.TextField(label="Digite um número" )
    btn_enviar = ft.FilledButton(text="Enviar",
                                 width=page.window.width,
                                 on_click=mostrar_resultado,
                                 )
    txt_resultado = ft.Text(value="")


    # Botões

    nascimento = ft.TextField(label='digite a sua data de nascimento (ex: 23/04/1998')
    idade = ft.TextField(label='digite a sua data de nascimento (ex: 23/04/1998')



    txt_resultado = ft.Text("")

    # Componentes

    page.add(
        ft.Column(
            [
                nascimento,
                idade,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)