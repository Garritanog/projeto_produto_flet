"""
Anotações: := (Horus),pra poder definir uma variavel dentro de uma estaciação/propriedade  
atribui uma variavel dentro de cada um dos componentes para pegar as propiedades de casa um deles


ft.ResponsiveRow( ---> Para os elementos ficarem lado a lado
"""
import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK  # podendo ser personalizada '#000000'
    page.scroll = ft.ScrollMode.AUTO

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5

        main_image.update()
        options.update()

    product_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            # center, top( mais opções)
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132553_gg.jpg',
                ),

                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132556_gg.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://images.kabum.com.br/produtos/fotos/161470/controle-sem-fio-dualsense-cosmic-red-ps5-pre-venda_1621439350_gg.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                        ft.Container(
                            image_src='https://images.kabum.com.br/produtos/fotos/sync_mirakl/485277/Jogo-EA-Sports-FC-24-Standard-Edition-Playstation-5-M-dia-F-sica_1709396282_gg.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                    ]
                )
            ]
        )
    )
    product_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='VIDEO GAME',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    value='Console Playstation 5 Sony, SSD 825GB, Controle sem fio DualSense, Com Mídia Física, Branco - 1214A',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),

                ft.Text(value='Video game, controle e jogos',
                        color=ft.colors.GREY, italic=True),

                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$3.599,99',
                            color=ft.colors.WHITE,
                            size=30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            spacing=2,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )


                    ]
                ),

                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),

                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Console Playstation 5 Sony, SSD 825GB, Controle sem fio DualSense, Com Mídia Física, Branco ',
                                    color=ft.colors.GREY,
                                )
                            )

                        )
                    ]
                ),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Produto',
                            label_style=ft.TextStyle(
                                color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='Playstion5'),
                                ft.dropdown.Option(text='Controle'),
                                ft.dropdown.Option(text='Jogos'),
                            ]
                        ),

                        ft.Dropdown(
                            col=6,
                            label='Parcelar',
                            label_style=ft.TextStyle(
                                color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} x {"com juros" if num > 9 else "sem juros"}') for num in range(1, 13)
                            ]
                        ),

                    ]
                ),
                ft.Container(expand=True),

                ft.ElevatedButton(
                    width=900,
                    text='Adicionar a lista de desejo',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE),
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.WHITE
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        }
                    )
                ),
                ft.ElevatedButton(
                    width=900,
                    text='Adicionar ao carrinho',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER),
                        },
                        bgcolor={
                            ft.MaterialState.DEFAULT: ft.colors.AMBER,
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        }
                    )
                ),
            ]
        )
    )

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details
            ]

        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
