import mesop as me
import requests


@me.stateclass
class State:
    organization_name: str = ''
    policy: str = ''
    message: str = ''  # Para mostrar mensajes de error o éxito

BOX_WIDTH = 0

def sendData(state: State):
    # Endpoint al que enviar los datos
    url = 'http://127.0.0.1:8000/organizations/'

    # Datos para enviar
    payload = {
        'name': state.organization_name,
        'policy': state.policy
    }

    # Hacer la petición POST
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            state.message = "Datos enviados correctamente."
        else:
            state.message = f"Error al enviar datos: {response.status_code}"
    except Exception as e:
        state.message = str(e)


@me.page()
def app():
    state = me.state(State)
    with me.box(style=me.Style(padding=me.Padding.all(10), width=500, align_items="center", justify_content="center")):
        with me.box():
            me.text("Nombre de la Organización:")
            # Ajuste aquí: Pasar solo el nombre de la función
            me.input(value=state.organization_name, on_input=lambda value: update_state_field(state, 'organization_name', value))

        with me.box():
            me.text("Policy:")
            # Ajuste aquí: Pasar solo el nombre de la función
            me.input(value=state.policy, on_input=lambda value: update_state_field(state, 'policy', value))

        me.button("Enviar", on_click=lambda: sendData(state), type="raised")

        if state.message:
            me.text(state.message)  # Mostrar mensaje de error o éxito

def update_state_field(state, field_name, value):
    # Asegurarse de que se está actualizando correctamente el estado.
    print(f"Updating {field_name} to {value}")  # Puedes eliminar esta línea después de verificar que todo funciona correctamente.
    setattr(state, field_name, value)



  
  
    