import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


top_card = dbc.Card(
    [
        dbc.CardImg(src="/static/images/2D.png", top=True),
        dbc.CardBody(
            html.P("DEALER", className="card-text")
        ),
    ],
    style={"width": "18rem"},
)

app.layout = html.Div(children=[
    html.H1(children='Black Jack Simulator'),

    html.Div(top_card)
    
])

if __name__ == '__main__':
    app.run_server(debug=True)