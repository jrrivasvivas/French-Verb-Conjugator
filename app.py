import dash
from dash import dcc, html, callback, Input, Output, State
from src.game.game_logic import ConjugationGameLogic
from src.game.player import Player
from src.logging.logger import ErrorLogger

app = dash.Dash(__name__)

# Crear instancias de clases para el juego, jugadores y registro de errores
error_logger = ErrorLogger("2023-11")
player1 = Player("jose")
player2 = Player("Jugador2")
game_logic = ConjugationGameLogic([player1, player2], error_logger)

# Página principal del juego
game_layout = html.Div([
    html.H1("Jeu de Conjugaison de Verbes !"),
    html.Div(id='verb-details'),
    dcc.Input(id='user-name-input', type='text', placeholder='Entrez votre prénom'),
    dcc.Input(id='user-input', type='text', placeholder='Entrez la conjugaison (pronom verbe)'),
    html.Button('Soumettre', id='submit-button', n_clicks=0),
    html.Div(id='result-message'),  # Para mostrar el resultado de la ronda y el score
])

# Definir la función de callback
@app.callback(
    [Output('result-message', 'children'), Output('verb-details', 'children')],
    [Input('submit-button', 'n_clicks')],
    [State('user-name-input', 'value'), State('user-input', 'value')]
)
def update_output(n_clicks, user_name, user_input):
    if n_clicks > 0:
        try:
            # Jugar una ronda con la entrada del usuario
            result = game_logic.play_round(user_name, user_input)
            output_message = f"Ronda: {result['verb']} {result['pronoun']} {result['tense']} - {result['result']}"
            
            # Detalles del verbo a conjugar
            verb_details = f"Conjugar el verbo '{result['verb']}' con el pronombre '{result['pronoun']}' en tiempo '{result['tense']}'"

            # Mostrar el resultado de la ronda y el score
            return output_message, f"Score: {game_logic.get_total_score(user_name)}"
        except ValueError as e:
            return str(e), None

    # Si n_clicks es 0, mostrar la primera pregunta
    verb, pronoun, tense = game_logic.conjugator.generate_random_verb()
    return f"Conjugar el verbo '{verb}' con el pronombre '{pronoun}' en tiempo '{tense}'", None

# Configurar el diseño de la aplicación
app.layout = game_layout

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
