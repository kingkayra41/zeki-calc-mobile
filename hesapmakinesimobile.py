import flet as ft
import math
import re

def main(page: ft.Page):
    page.title = "Zeki Calculator Pro" # Burayı istediğin adla değiştirebilirsin
    page.theme_mode = ft.ThemeMode.DARK
    lang = "TR"
    texts = {"TR": {"error": "Hata", "lang_btn": "TR"}, "EN": {"error": "Error", "lang_btn": "EN"}}
    result_text = ft.Text(value="0", color="white", size=50)

    def button_clicked(e):
        nonlocal lang
        val = e.control.text
        if val in ["TR", "EN"]:
            lang = "EN" if lang == "TR" else "TR"
            e.control.text = texts[lang]["lang_btn"]
        elif val == "C": result_text.value = "0"
        elif val == "=":
            try:
                formula = re.sub(r'(\d)([πe\(])', r'\1*\2', result_text.value)
                formula = formula.replace('π', str(math.pi)).replace('e', str(math.e)).replace('^', '**').replace(',', '.')
                result_text.value = str(round(eval(formula), 6)).replace('.', ',')
            except: result_text.value = texts[lang]["error"]
        else: result_text.value = val if result_text.value == "0" else result_text.value + val
        page.update()

    def btn(text, color):
        return ft.ElevatedButton(text=text, bgcolor=color, color="white", expand=1, on_click=button_clicked)

    page.add(ft.Container(content=result_text, padding=40, alignment=ft.alignment.bottom_right),
        ft.Column(expand=True, controls=[
            ft.Row(controls=[btn("C", "#A5A5A5"), btn("TR", "#5856D6"), btn("^", "#FF9F0A"), btn("/", "#FF9F0A")]),
            ft.Row(controls=[btn("7", "#333333"), btn("8", "#333333"), btn("9", "#333333"), btn("*", "#FF9F0A")]),
            ft.Row(controls=[btn("4", "#333333"), btn("5", "#333333"), btn("6", "#333333"), btn("-", "#FF9F0A")]),
            ft.Row(controls=[btn("1", "#333333"), btn("2", "#333333"), btn("3", "#333333"), btn("+", "#FF9F0A")]),
            ft.Row(controls=[btn("e", "#333333"), btn("0", "#333333"), btn("π", "#333333"), btn("=", "#FF9F0A")])]))

ft.app(target=main)
