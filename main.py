from flet import *


def main(p: Page):

    # page setttings
    p.title = "LAB №4"
    p.vertical_alignment = "center"
    p.horizontal_alignment = "center"

    # perimetr
    def Perimetr(e):
        a = float(_a.value)
        b = float(_b.value)
        h = float(_h.value)
        perimetr = a+b+2*((h**2+((a-b)/2)**2)**0.5)
        _t.text = f"Perimetr={perimetr}"
        p.update()

    # yuza
    def Yuza(e):
        a = float(_a.value)
        b = float(_b.value)
        h = float(_h.value)
        yuza = (a+b)*0.5*h
        _t.text = f"Yuza={yuza}"
        p.update()

    # trapetsiya sozlamalari
    _h = TextField(label="Trapetsiya balandligi",
                   width=300,
                   hint_text="Trapetsiya balandligini kiriting")
    _a = TextField(label="Trapetsiya pastki asosi",
                   width=300,
                   hint_text="Trapetsiya pastki asosini kiriting")
    _b = TextField(label="Trapetsiya yuqori asosi",
                   width=300,
                   hint_text="Trapetsiya yuqori asosini kiriting")
    _P = ElevatedButton(text="Perimetr", on_click=Perimetr)
    _S = ElevatedButton(text="Yuza", on_click=Yuza)
    _t = ElevatedButton(text=None, width=300, color='BLUE', disabled=True)
    _shart = Text(
        value="Trapetsiyaning asoslari va balandligi berilagan. Uning perimetr va yuzasini hisoblang!", size=22, color="CYAN")
    # ADD
    p.add(Column([_shart],
                 alignment='center'))
    p.add(Column([_a, _b, _h],
                 alignment='center'))
    p.add(Row([_P, _S],
              alignment='center'))
    p.add(Column([_t],
                 alignment='center'))


flet.app(target=main)
