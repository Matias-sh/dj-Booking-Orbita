import mesop as me
import requests
import pandas as pd
from dataclasses import field
from flask import Flask

app = Flask(__name__)

@me.stateclass
class State:
    selected_cell: str = "No cell selected."
    data: list = field(default_factory=list)

@me.page()
def organizations_page():
    state = me.state(State)
    if not state.data:
        response = requests.get('http://127.0.0.1:8000/organizations/')
        data = response.json()
        df = pd.DataFrame(data)
        state.data = df.to_dict('list')

    with me.box(style=me.Style(padding=me.Padding.all(10), width=500)):
        # Ensure df is defined before using it here
        if 'df' in locals():
            me.table(
                df,
                on_click=lambda e: on_click(e, df, state),
                header=me.TableHeader(sticky=True),
                columns={key: me.TableColumn(sticky=True) for key in df.columns}
            )
        else:
            me.text("Dataframe not loaded.")

    with me.box(style=me.Style(background="#ececec", margin=me.Margin.all(10), padding=me.Padding.all(10))):
        me.text(state.selected_cell)

def on_click(e: me.TableClickEvent, df: pd.DataFrame, state: State):
    # Check if df is defined
    if 'df' in locals():
        value = str(df.iloc[e.row_index, e.col_index])
        state.selected_cell = f"Selected cell at col {e.col_index} and row {e.row_index} with value {value}"
    else:
        state.selected_cell = "Dataframe is not defined."

# Call the page function to load
with app.app_context():
    # Now you can call your Mesop function that requires the context
    organizations_page()
