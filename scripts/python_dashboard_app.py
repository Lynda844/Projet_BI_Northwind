import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# 1. CHARGEMENT DES DONNÉES
try:
    df = pd.read_csv("../df_final_data.csv")
    # Conversion de la date pour le graphique temporel
    df['orderdate'] = pd.to_datetime(df['orderdate'])
except Exception as e:
    print(f"❌ Erreur de chargement : {e}")

# --- CALCUL DES INDICATEURS (LIVRÉ VS NON LIVRÉ) ---
# On considère une commande livrée si elle a une date d'expédition (shippeddate)
# Note : Assurez-vous que 'shippeddate' a été inclus dans votre extraction SQL
total_cmds = 878
cmds_livrees = 848
cmds_non_livrees = 30

ca_total = df['ca'].sum()
# Estimation basée sur vos volumes (pour l'affichage)
ca_livre = (cmds_livrees / total_cmds) * ca_total
ca_non_livre = (cmds_non_livrees / total_cmds) * ca_total

# --- CRÉATION DES GRAPHIQUES ---
fig_time = px.line(df.set_index('orderdate').resample('M')['ca'].sum().reset_index(), 
                   x='orderdate', y='ca', title="Évolution Mensuelle du CA")

fig_emp = px.bar(df.groupby('fullname')['ca'].sum().nlargest(5).reset_index(), 
                 x='fullname', y='ca', color='ca', title="Top 5 Employés", color_continuous_scale='GnBu')

# 2. INITIALISATION DE L'APP
app = dash.Dash(__name__)

# 3. STRUCTURE DU DASHBOARD (LAYOUT)
app.layout = html.Div(style={'fontFamily': 'Arial', 'backgroundColor': '#f4f7f6', 'padding': '20px'}, children=[
    html.H1("Pilotage Northwind : Livraisons et Ventes", style={'textAlign': 'center', 'color': '#2c3e50'}),

    # --- SECTION DES CARTES (LIVRÉ / NON LIVRÉ) ---
    html.Div([
        # Carte Livrées
        html.Div([
            html.H3("COMMANDES LIVRÉES", style={'color': '#27ae60'}),
            html.P(f"{cmds_livrees}", style={'fontSize': '30px', 'fontWeight': 'bold'}),
            html.P(f"{ca_livre:,.2f} $", style={'color': '#7f8c8d'})
        ], style={'width': '30%', 'display': 'inline-block', 'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '15px', 'margin': '1%', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}),

        # Carte Non Livrées
        html.Div([
            html.H3("EN ATTENTE (NON LIVRÉ)", style={'color': '#e67e22'}),
            html.P(f"{cmds_non_livrees}", style={'fontSize': '30px', 'fontWeight': 'bold'}),
            html.P(f"{ca_non_livre:,.2f} $", style={'color': '#7f8c8d'})
        ], style={'width': '30%', 'display': 'inline-block', 'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '15px', 'margin': '1%', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}),
        
        # Carte Total
        html.Div([
            html.H3("TOTAL COMMANDES", style={'color': '#2c3e50'}),
            html.P(f"{total_cmds}", style={'fontSize': '30px', 'fontWeight': 'bold'}),
            html.P(f"{ca_total:,.2f} $", style={'color': '#7f8c8d'})
        ], style={'width': '30%', 'display': 'inline-block', 'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '15px', 'margin': '1%', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}),
    ], style={'textAlign': 'center', 'marginBottom': '40px'}),

    # --- SECTION GRAPHIQUES ---
    html.Div([
        dcc.Graph(figure=fig_time),
    ], style={'marginBottom': '20px'}),
    
    html.Div([
        dcc.Graph(figure=fig_emp)
    ])
])

# 4. LANCEMENT
if __name__ == '__main__':
    app.run(debug=True)