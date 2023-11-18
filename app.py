import dash
from dash import Dash, dcc, html, callback, Input, Output, State

from src.game import ConjugationGame

app = dash.Dash(__name__)

# Crear una instancia de ConjugationGame sin proporcionar un nombre de usuario
game = ConjugationGame()

# Página principal del juego
game_layout = html.Div([
    html.H1("Jeu de Conjugaison de Verbes !"),
    dcc.Input(id='user-name-input', type='text', placeholder='Entrez votre prénom'),
    dcc.Input(id='user-input', type='text', placeholder='Entrez la conjugaison (pronom verbe)'),
    html.Button('Soumettre', id='submit-button', n_clicks=0),
    html.Div(id='output'),
])

@app.callback(
     Output('output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('user-name-input', 'value'), State('user-input', 'value')]
)
def update_output(n_clicks, user_name, user_input):
    if n_clicks > 0:
        game.user_name = user_name.lower()  # Establecer el nombre de usuario en el objeto de juego
        game.play_round(user_input)
        score = game.get_score()
        return f"Score: {score}"

app.layout = game_layout

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)