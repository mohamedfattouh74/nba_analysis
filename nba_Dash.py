from dash import Dash
from dash import dcc, html
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from PIL import Image

nba_df = pd.read_csv("C:/Users/LENOVO/Downloads/Data analysis/nba_analysis/nba_data_RS_2022-2014.csv")
nba_logo = Image.open("C:/Users/LENOVO/Downloads/Data analysis/nba_analysis/NBA-new-logo.png")
teams_logo = Image.open("C:/Users/LENOVO/Downloads/Data analysis/nba_analysis/teams.jpg")
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE, dbc_css])
load_figure_template('SLATE')
app.layout = html.Div(
    [
        html.Header(
            style={'display': 'flex',
                   'backgroundColor': '#f5f6f7',
                   'height': '100px',
                   'margin-bottom': '10px'},
            children=(
                [html.Img(
                    src=nba_logo,
                    style={
                        'width': '170px',
                        'height': '100px'
                    }
                ),

                    html.H1(["NBA stats for Regular Seasons ",
                             html.Span("2014-2022",
                                       style={'color': '#1c6bba'})],
                            style={
                                'text-align': "center",
                                'color': 'red',
                                'font-weight': "bold",
                                'margin': 'auto'
                            }),

                    html.Img(
                        src=teams_logo,
                        style={
                            'width': '140px',
                            'height': '100px'
                        }

                    )]
            )
        ),

        dbc.Row([
            dbc.Col([html.Div([
                html.H4("Choose a Team"),
                dcc.Dropdown(id='team-kpis',
                             options=nba_df['team'].unique(),
                             value='Chicago Bulls',
                             className='dbc'),
                html.Br(),
                html.H4("Choose a Season"),
                dcc.Dropdown(id='season-kpis',
                             options=nba_df['year'].unique(),
                             value=2022,
                             className='dbc'), ])], width=2),
            dbc.Col([dbc.Row([dbc.Col(html.H3("Wins")),
                              dbc.Col(html.H3("Losses")),
                              dbc.Col(html.H3("Points")),
                              dbc.Col(html.H3("Assists")),
                              dbc.Col(html.H3("Rebounds"))]),

                     html.Br(),

                     dbc.Row(
                         style={'font-size': '30px',
                                'text-align': 'center',
                                'gap': '11.5%'},
                         children=[
                             dbc.Col(dbc.Card(dbc.Col(id="kpi-1")), width=1),
                             dbc.Col(dbc.Card(dbc.Col(id="kpi-2")), width=1),
                             dbc.Col(dbc.Card(dbc.Col(id="kpi-3")), width=1),
                             dbc.Col(dbc.Card(dbc.Col(id="kpi-4")), width=1),
                             dbc.Col(dbc.Card(dbc.Col(id="kpi-5")), width=1)
                         ])], style={'margin-top': '30px',
                                     'margin-left': '50px'})
        ]),

        html.Br(),
        html.Hr(),
        html.Br(),

        html.Section(
            style={'display': 'flex',
                   'gap': '0.5',
                   'height': '600px'
                   },
            children=[
                html.Div(style={'display': 'block',
                                'margin-right': '20px'},
                         children=[html.H4("Choose Team"),
                                   html.Br(),

                                   dcc.Dropdown(id="team-options",
                                                options=nba_df.team.unique(),
                                                value='Chicago Bulls',
                                                className='dbc',
                                                style={

                                                    'width': '150px'})
                                   ])
                ,
                dcc.Graph(id="wins-chart"),
                dcc.Graph(id="points-chart")
            ]),

        html.Br(),
        html.Hr(),
        html.Br(),

        html.Section(
            style={'display': 'flex',
                   'gap': '0.5'
                   },
            children=[
                html.Div(
                    style={'display': 'block'},
                    children=[
                        html.H4("Choose X axis"),
                        dcc.Dropdown(id="scatterX-options",
                                     options=nba_df.select_dtypes(include='number').columns[1:-1],
                                     value="turnovers",
                                     className='dbc'
                                     ),
                        html.Br(),
                        html.Br(),
                        html.H4("Choose Y axis"),
                        dcc.Dropdown(id="scatterY-options",
                                     options=nba_df.select_dtypes(include='number').columns[1:-1],
                                     value="wins",
                                     className='dbc'
                                     ),
                        html.Br(),
                        html.Br(),
                        html.H4("Choose a Year"),
                        dcc.Dropdown(id="year-options",
                                     options=nba_df['year'].unique(),
                                     value=2022,
                                     className='dbc'
                                     ),
                    ]),

                dcc.Graph(id="scatter-chart",
                          style={'height': '60%',
                                 'width': '65%',
                                 'margin-right': 'auto',
                                 'margin-left': 'auto'}),

            ]),
        html.Br(),
        html.Hr(),
        html.Br(),

        html.Div(style={'display': 'flex'},
                 children=[
                     html.H4("Choose a Year",
                             style={'margin-left': '160px',
                                    'margin-right': '20px'}),
                     dcc.Dropdown(id="year-options-assists",
                                  options=nba_df['year'].unique(),
                                  value=2022,
                                  className='dbc',
                                  style={'margin-right': '450px',
                                         'width': '100px'}
                                  ),
                     html.H4("Choose a Year",
                             style={'margin-right': '20px'}),

                     dcc.Dropdown(id="year-options-wins",
                                  options=nba_df['year'].unique(),
                                  value=2022,
                                  className='dbc',
                                  style={
                                      'width': '100px'}
                                  ),
                 ]),
        html.Br(),
        html.Section(
            style={'display': 'flex',
                   'height': '400px'},
            children=[

                dcc.Graph(id="assists-chart",
                          style={'margin-right': '80px',
                                 'margin-left': '160px',
                                 'width': '600px'
                                 }),

                dcc.Graph(id="topWins-chart",
                          style={'width': '600px'
                                 }
                          )
            ]),

        html.Br(),
        html.Hr(),
        html.Br(),
        html.Div([
            html.Section(style={'display': 'flex'},
                         children=[
                             html.H4("Choose a Year", style={
                                 'margin-left': '280px',
                                 'margin-right': '20px'}),

                             dcc.Dropdown(id="year-options-distribution",
                                          options=nba_df['year'].unique(),
                                          value=2022,
                                          className='dbc',
                                          style={
                                              'width': '100px',
                                              'margin-right': '40px'}
                                          ),

                             dcc.RadioItems(id='distribution-options',
                                            options=[{'label': 'Free throws % ', 'value': 'ft_percent'},
                                                     {'label': 'Wins % ', 'value': 'win_percent'}],
                                            value="ft_percent",
                                            className='dbc',
                                            style={'margin-left': '20px'})])
            ,
            html.Br(),

            dcc.Graph(id='distribution-graph',
                      style={'height': '60%',
                             'width': '65%',
                             'margin-right': 'auto',
                             'margin-left': 'auto'})]
        )

    ]
)


@app.callback(

    Output('kpi-1', 'children'),
    Output('kpi-2', 'children'),
    Output('kpi-3', 'children'),
    Output('kpi-4', 'children'),
    Output('kpi-5', 'children'),
    Output('wins-chart', 'figure'),
    Output('points-chart', 'figure'),
    Output('scatter-chart', 'figure'),
    Output('assists-chart', 'figure'),  # Top 10 assists
    Output('topWins-chart', 'figure'),  # Top 10 wins
    Output('distribution-graph', 'figure'),

    Input('team-kpis', 'value'),
    Input('season-kpis', 'value'),
    Input('team-options', 'value'),
    Input('scatterX-options', 'value'),
    Input('scatterY-options', 'value'),
    Input('year-options', 'value'),
    Input('year-options-assists', 'value'),
    Input('year-options-wins', 'value'),
    Input('year-options-distribution', 'value'),
    Input('distribution-options', 'value')

)
def dash_build(teamKpi, seasonKpi, team, xColumn, yColumn, year, yearAssist, yearWins, yearDistribution,
               distributionType):

    kpi1 = nba_df.query("team==@teamKpi and year==@seasonKpi")["wins"]
    kpi2 = nba_df.query("team==@teamKpi and year==@seasonKpi")["losses"]
    kpi3 = nba_df.query("team==@teamKpi and year==@seasonKpi")["points"]
    kpi4 = nba_df.query("team==@teamKpi and year==@seasonKpi")["assists"]
    kpi5 = nba_df.query("team==@teamKpi and year==@seasonKpi")["rebounds"]
    figure2 = px.bar(nba_df.query("team==@team"),
                     x="year",
                     y="wins",
                     title=f"Wins per year for {team} (2014-2022)"
                     , color_discrete_sequence=["red"])

    figure = px.line(nba_df.query("team==@team"),
                     x="year",
                     y="points",
                     title=f"Points per year for {team} (2014-2022)"
                     , color_discrete_sequence=["red"])

    figure3 = px.scatter(nba_df.query('year == @year'),
                         x=xColumn,
                         y=yColumn,
                         title=f"Scatter plot between {xColumn} and {yColumn} at {year}",
                         color_discrete_sequence=["red"])

    df_fig4 = nba_df.query('year == @yearAssist')
    figure4 = px.bar(df_fig4.sort_values('assists', ascending=False).head(10),
                     x='assists',
                     y='team',
                     orientation='h',
                     title=f"Top 10 teams at assists for {yearAssist}",
                     color_discrete_sequence=["red"])

    df_fig5 = nba_df.query('year == @yearWins')
    figure5 = px.bar(df_fig5.sort_values('wins', ascending=False).head(10),
                     x='wins',
                     y='team',
                     orientation='h',
                     title=f"Top 10 teams at wins for {yearWins}",
                     color_discrete_sequence=["red"])

    df_fig6 = nba_df.query('year == @yearDistribution')
    figure6 = px.histogram(df_fig6,
                           x=df_fig6[distributionType],
                           title=f"Distribution of {distributionType} at {yearDistribution}",
                           labels={"x": distributionType},
                           color_discrete_sequence=["red"]
                           )

    return kpi1, kpi2, kpi3, kpi4, kpi5, figure2, figure, figure3, figure4, figure5, figure6


if __name__ == "__main__":
    app.run_server()
