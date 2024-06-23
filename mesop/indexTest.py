import mesop as me


@me.stateclass
class State:
  sidenav_open: bool


def on_click(e: me.ClickEvent):
  s = me.state(State)
  s.sidenav_open = not s.sidenav_open


SIDENAV_WIDTH = 200


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/sidenav",
)
def app():
  state = me.state(State)
  with me.box(style=me.Style(background="red", padding=me.Padding.all(200))):
    me.text("INGRESA EL NOMBRE")
    me.input(color="primary")
    