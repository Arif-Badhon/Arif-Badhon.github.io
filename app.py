from dash import Dash, html, dcc



app = Dash(__name__)


app.layout = html.Div(children=[html.H1(children="KIKIS VOCAL DIARY")])


if __name__ == '__main__':
    app.run_server(debug=True)