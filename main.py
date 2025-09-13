import pandas as pd
import scipy.stats as stats
import dash
from dash import dcc, html, Input, Output
from dash.dash_table import DataTable
import plotly.express as px

# Load dataset
df = pd.read_excel('data.xlsx')

# Columns to analyze
demographic_cols = [
    "Gender",
    "Age Group",
    "Educational level",
    "Occupation",
    "How long have you lived in Ayeduase-Kotei ?",
    "What is your primary source of water ?", 
    "How long have you been practicing self-supply?",   
    "Who constructed your self-supply source?",
    'What are the reasons for using self-supply water?',
    "How often do you experience water shortages from your self-supply source?",
    "What are the major challenges you face with your self-supply water system?",
    "Have you ever experienced waterborne diseases due to self-supply?",
    "How do you address quality concerns?",
    "What improvements would you suggest for sustainable self-supply water systems in Ayeduase-Kotei?"  
]

# Function to create frequency table and chi-square p-value
def analyze_column(col):
    data = df[col].dropna()
    n = len(data)
    freq_table = data.value_counts().reset_index()
    freq_table.columns = ["Category", "Frequency"]
    freq_table["Percent"] = round(100 * freq_table["Frequency"] / n, 2)
    
    # Chi-square goodness of fit test (assuming uniform distribution)
    observed = freq_table["Frequency"].values
    if len(observed) > 1:  # Need at least 2 categories for chi-square
        chi2, p = stats.chisquare(observed)
    else:
        p = None  # Can't compute if only one category
    
    return freq_table, p, n

# Generate results for all demographic columns
results = {}
for col in demographic_cols:
    if col in df.columns:
        results[col] = analyze_column(col)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Demographic Dashboard"),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label': col + f' (N={results[col][2]})', 'value': col} for col in demographic_cols if col in results],
        value=demographic_cols[0],
        style={'width': '50%'}
    ),
    html.Div(id='table-output', style={'margin-top': '20px'}),
    dcc.Graph(id='chart-output', style={'margin-top': '20px'})
])

@app.callback(
    [Output('table-output', 'children'), Output('chart-output', 'figure')],
    Input('demo-dropdown', 'value')
)
def update_output(col):
    if col not in results:
        return html.Div("No data available"), {}
    
    freq_table, p, n = results[col]
    
    # Create DataTable for frequency table
    table = DataTable(
        data=freq_table.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in freq_table.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'minWidth': '100px'}
    )
    
    # p-value display
    p_text = f"p-value: {p:.3f}" if p is not None else "p-value: N/A"
    
    # Create interactive pie chart (or bar if preferred)
    fig = px.pie(
        freq_table, 
        values='Percent', 
        names='Category', 
        title=f'{col} Distribution (N={n}, {p_text})',
        hole=0.3  # Donut style for visual appeal
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(margin=dict(t=40, b=0, l=0, r=0))
    
    # Return table with p-value header
    return html.Div([
        html.H3(p_text),
        table
    ]), fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)