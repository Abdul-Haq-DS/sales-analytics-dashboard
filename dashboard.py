# ================================================
# Sales Analytics Dashboard
# Built with Plotly Dash
# Dataset: Superstore 2014-2017
# Author: Abdul
# ================================================

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import os

# ── Load data ────────────────────────────────────
BASE_DIR   = '/home/abdul/sales-analytics-dashboard'
CLEAN_DATA = os.path.join(BASE_DIR, 'data', 'processed', 'clean_superstore.csv')

df = pd.read_csv(CLEAN_DATA)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ── App init ─────────────────────────────────────
app = Dash(__name__)
app.title = "Sales Analytics Dashboard"

# ── Color palette ────────────────────────────────
COLORS = {
    'primary'    : '#2563EB',
    'success'    : '#16A34A',
    'danger'     : '#DC2626',
    'warning'    : '#D97706',
    'bg'         : '#F8FAFC',
    'card'       : '#FFFFFF',
    'text'       : '#1E293B',
    'muted'      : '#64748B',
    'border'     : '#E2E8F0',
}

# ── Reusable card style ───────────────────────────
def card(children, flex=1):
    return html.Div(children, style={
        'background'   : COLORS['card'],
        'borderRadius' : '12px',
        'padding'      : '20px',
        'boxShadow'    : '0 1px 4px rgba(0,0,0,0.08)',
        'border'       : f"1px solid {COLORS['border']}",
        'flex'         : flex,
    })

# ── KPI card ─────────────────────────────────────
def kpi_card(title, value, subtitle, color):
    return card(html.Div([
        html.P(title, style={
            'margin'     : '0 0 8px 0',
            'fontSize'   : '13px',
            'fontWeight' : '500',
            'color'      : COLORS['muted'],
            'textTransform': 'uppercase',
            'letterSpacing': '0.05em',
        }),
        html.H2(value, style={
            'margin'    : '0 0 4px 0',
            'fontSize'  : '28px',
            'fontWeight': '700',
            'color'     : color,
        }),
        html.P(subtitle, style={
            'margin'   : '0',
            'fontSize' : '12px',
            'color'    : COLORS['muted'],
        }),
    ]))

# ── Dropdown style ───────────────────────────────
dropdown_style = {
    'borderRadius' : '8px',
    'fontSize'     : '13px',
    'border'       : f"1px solid {COLORS['border']}",
}

# ── Layout ───────────────────────────────────────
app.layout = html.Div(style={
    'fontFamily'    : '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    'background'    : COLORS['bg'],
    'minHeight'     : '100vh',
    'padding'       : '0',
    'color'         : COLORS['text'],
}, children=[

    # ── Header ───────────────────────────────────
    html.Div(style={
        'background'   : COLORS['primary'],
        'padding'      : '20px 32px',
        'marginBottom' : '24px',
    }, children=[
        html.H1("Sales Analytics Dashboard", style={
            'margin'    : '0 0 4px 0',
            'fontSize'  : '22px',
            'fontWeight': '700',
            'color'     : '#FFFFFF',
        }),
        html.P("Superstore Dataset  |  2014 – 2017  |  9,994 orders", style={
            'margin'  : '0',
            'fontSize': '13px',
            'color'   : 'rgba(255,255,255,0.75)',
        }),
    ]),

    # ── Main content ─────────────────────────────
    html.Div(style={'padding': '0 32px 32px 32px'}, children=[

        # ── Filters row ──────────────────────────
        html.Div(style={
            'display'      : 'flex',
            'gap'          : '16px',
            'marginBottom' : '24px',
            'flexWrap'     : 'wrap',
        }, children=[
            card(html.Div([
                html.Label("Year", style={
                    'fontSize': '12px',
                    'fontWeight': '500',
                    'color': COLORS['muted'],
                    'marginBottom': '6px',
                    'display': 'block',
                }),
                dcc.Dropdown(
                    id='year-filter',
                    options=[{'label': 'All Years', 'value': 'All'}] +
                            [{'label': str(y), 'value': y}
                             for y in sorted(df['Year'].unique())],
                    value='All',
                    clearable=False,
                    style=dropdown_style,
                ),
            ]), flex=1),

            card(html.Div([
                html.Label("Region", style={
                    'fontSize': '12px',
                    'fontWeight': '500',
                    'color': COLORS['muted'],
                    'marginBottom': '6px',
                    'display': 'block',
                }),
                dcc.Dropdown(
                    id='region-filter',
                    options=[{'label': 'All Regions', 'value': 'All'}] +
                            [{'label': r, 'value': r}
                             for r in sorted(df['Region'].unique())],
                    value='All',
                    clearable=False,
                    style=dropdown_style,
                ),
            ]), flex=1),

            card(html.Div([
                html.Label("Category", style={
                    'fontSize': '12px',
                    'fontWeight': '500',
                    'color': COLORS['muted'],
                    'marginBottom': '6px',
                    'display': 'block',
                }),
                dcc.Dropdown(
                    id='category-filter',
                    options=[{'label': 'All Categories', 'value': 'All'}] +
                            [{'label': c, 'value': c}
                             for c in sorted(df['Category'].unique())],
                    value='All',
                    clearable=False,
                    style=dropdown_style,
                ),
            ]), flex=1),

            card(html.Div([
                html.Label("Segment", style={
                    'fontSize': '12px',
                    'fontWeight': '500',
                    'color': COLORS['muted'],
                    'marginBottom': '6px',
                    'display': 'block',
                }),
                dcc.Dropdown(
                    id='segment-filter',
                    options=[{'label': 'All Segments', 'value': 'All'}] +
                            [{'label': s, 'value': s}
                             for s in sorted(df['Segment'].unique())],
                    value='All',
                    clearable=False,
                    style=dropdown_style,
                ),
            ]), flex=1),
        ]),

        # ── KPI row ──────────────────────────────
        html.Div(style={
            'display'      : 'flex',
            'gap'          : '16px',
            'marginBottom' : '24px',
            'flexWrap'     : 'wrap',
        }, children=[
            html.Div(id='kpi-revenue',  style={'flex': 1}),
            html.Div(id='kpi-profit',   style={'flex': 1}),
            html.Div(id='kpi-orders',   style={'flex': 1}),
            html.Div(id='kpi-margin',   style={'flex': 1}),
        ]),

        # ── Charts row 1 ─────────────────────────
        html.Div(style={
            'display'      : 'flex',
            'gap'          : '16px',
            'marginBottom' : '16px',
            'flexWrap'     : 'wrap',
        }, children=[
            card(dcc.Graph(id='chart-monthly-trend',
                           config={'displayModeBar': False}), flex=2),
            card(dcc.Graph(id='chart-category',
                           config={'displayModeBar': False}), flex=1),
        ]),

        # ── Charts row 2 ─────────────────────────
        html.Div(style={
            'display'      : 'flex',
            'gap'          : '16px',
            'marginBottom' : '16px',
            'flexWrap'     : 'wrap',
        }, children=[
            card(dcc.Graph(id='chart-subcategory',
                           config={'displayModeBar': False}), flex=1),
            card(dcc.Graph(id='chart-discount',
                           config={'displayModeBar': False}), flex=1),
        ]),

        # ── Charts row 3 ─────────────────────────
        html.Div(style={
            'display'      : 'flex',
            'gap'          : '16px',
            'flexWrap'     : 'wrap',
        }, children=[
            card(dcc.Graph(id='chart-region',
                           config={'displayModeBar': False}), flex=1),
            card(dcc.Graph(id='chart-segment',
                           config={'displayModeBar': False}), flex=1),
        ]),

    ]),
])


# ── Callback: filter data + update all charts ────
@app.callback(
    Output('kpi-revenue',        'children'),
    Output('kpi-profit',         'children'),
    Output('kpi-orders',         'children'),
    Output('kpi-margin',         'children'),
    Output('chart-monthly-trend','figure'),
    Output('chart-category',     'figure'),
    Output('chart-subcategory',  'figure'),
    Output('chart-discount',     'figure'),
    Output('chart-region',       'figure'),
    Output('chart-segment',      'figure'),
    Input('year-filter',         'value'),
    Input('region-filter',       'value'),
    Input('category-filter',     'value'),
    Input('segment-filter',      'value'),
)
def update_dashboard(year, region, category, segment):

    # ── Apply filters ─────────────────────────────
    dff = df.copy()
    if year     != 'All': dff = dff[dff['Year']     == year]
    if region   != 'All': dff = dff[dff['Region']   == region]
    if category != 'All': dff = dff[dff['Category'] == category]
    if segment  != 'All': dff = dff[dff['Segment']  == segment]

    # ── KPI values ───────────────────────────────
    total_revenue  = dff['Sales'].sum()
    total_profit   = dff['Profit'].sum()
    total_orders   = dff['Order ID'].nunique()
    overall_margin = (total_profit / total_revenue * 100) if total_revenue else 0

    kpi_rev = kpi_card(
        "Total Revenue",
        f"${total_revenue:,.0f}",
        "Sum of all sales",
        COLORS['primary'],
    )
    kpi_pro = kpi_card(
        "Total Profit",
        f"${total_profit:,.0f}",
        "Net profit after costs",
        COLORS['success'] if total_profit > 0 else COLORS['danger'],
    )
    kpi_ord = kpi_card(
        "Total Orders",
        f"{total_orders:,}",
        "Unique order count",
        COLORS['warning'],
    )
    kpi_mar = kpi_card(
        "Profit Margin",
        f"{overall_margin:.1f}%",
        "Profit as % of revenue",
        COLORS['success'] if overall_margin > 10 else COLORS['danger'],
    )

    # ── Chart layout base ────────────────────────
    def base_layout(title):
        return dict(
            title=dict(text=title, font=dict(size=14, color=COLORS['text']),
                       x=0, xanchor='left'),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor ='rgba(0,0,0,0)',
            font=dict(family='-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
                      color=COLORS['text'], size=12),
            margin=dict(l=10, r=10, t=40, b=10),
            showlegend=True,
            xaxis=dict(showgrid=False, zeroline=False,
                       linecolor=COLORS['border']),
            yaxis=dict(showgrid=True,
                       gridcolor=COLORS['border'],
                       zeroline=False),
        )

    # ── Chart 1: Monthly trend ───────────────────
    monthly = dff.groupby('YearMonth').agg(
        Revenue=('Sales', 'sum'),
        Profit =('Profit','sum')
    ).reset_index()

    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=monthly['YearMonth'], y=monthly['Revenue'],
        name='Revenue', mode='lines+markers',
        line=dict(color=COLORS['primary'], width=2),
        marker=dict(size=4),
        fill='tozeroy',
        fillcolor='rgba(37,99,235,0.08)',
    ))
    fig_trend.add_trace(go.Scatter(
        x=monthly['YearMonth'], y=monthly['Profit'],
        name='Profit', mode='lines+markers',
        line=dict(color=COLORS['success'], width=2),
        marker=dict(size=4),
    ))
    fig_trend.update_layout(**base_layout("Monthly Revenue & Profit Trend"))
    fig_trend.update_xaxes(tickangle=45, tickfont=dict(size=10))

    # ── Chart 2: Category bar ────────────────────
    cat = dff.groupby('Category').agg(
        Revenue=('Sales', 'sum'),
        Profit =('Profit','sum')
    ).reset_index().sort_values('Revenue', ascending=False)

    fig_cat = go.Figure()
    fig_cat.add_trace(go.Bar(
        name='Revenue', x=cat['Category'], y=cat['Revenue'],
        marker_color=COLORS['primary'], opacity=0.85,
    ))
    fig_cat.add_trace(go.Bar(
        name='Profit', x=cat['Category'], y=cat['Profit'],
        marker_color=COLORS['success'], opacity=0.85,
    ))
    fig_cat.update_layout(**base_layout("Revenue vs Profit by Category"),
                          barmode='group')

    # ── Chart 3: Sub-category profit ─────────────
    subcat = dff.groupby('Sub-Category')['Profit'].sum()\
               .reset_index().sort_values('Profit', ascending=True)

    colors_subcat = [
        COLORS['danger'] if x < 0 else COLORS['primary']
        for x in subcat['Profit']
    ]

    fig_sub = go.Figure(go.Bar(
        x=subcat['Profit'],
        y=subcat['Sub-Category'],
        orientation='h',
        marker_color=colors_subcat,
        opacity=0.85,
    ))
    fig_sub.update_layout(**base_layout("Profit by Sub-Category"))
    fig_sub.update_layout(showlegend=False)
    fig_sub.add_vline(x=0, line_color=COLORS['muted'],
                      line_dash='dash', line_width=1)

    # ── Chart 4: Discount impact ─────────────────
    disc_map = {
        '0% No discount' : dff[dff['Discount'] == 0],
        '1–10%'          : dff[(dff['Discount'] > 0)   & (dff['Discount'] <= 0.10)],
        '11–20%'         : dff[(dff['Discount'] > 0.10)& (dff['Discount'] <= 0.20)],
        '21–30%'         : dff[(dff['Discount'] > 0.20)& (dff['Discount'] <= 0.30)],
        'Above 30%'      : dff[dff['Discount'] > 0.30],
    }
    disc_df = pd.DataFrame([{
        'Band'       : k,
        'Avg Profit' : v['Profit'].mean(),
        'Orders'     : len(v),
    } for k, v in disc_map.items()])

    disc_colors = [
        COLORS['danger'] if x < 0 else COLORS['success']
        for x in disc_df['Avg Profit']
    ]

    fig_disc = go.Figure(go.Bar(
        x=disc_df['Band'],
        y=disc_df['Avg Profit'],
        marker_color=disc_colors,
        opacity=0.85,
        text=[f"${v:,.0f}" for v in disc_df['Avg Profit']],
        textposition='outside',
    ))
    fig_disc.update_layout(**base_layout("Avg Profit by Discount Band"))
    fig_disc.update_layout(showlegend=False)
    fig_disc.add_hline(y=0, line_color=COLORS['muted'],
                       line_dash='dash', line_width=1)

    # ── Chart 5: Region performance ──────────────
    region_df = dff.groupby('Region').agg(
        Revenue=('Sales', 'sum'),
        Profit =('Profit','sum')
    ).reset_index().sort_values('Revenue', ascending=True)

    fig_region = go.Figure()
    fig_region.add_trace(go.Bar(
        name='Revenue', y=region_df['Region'],
        x=region_df['Revenue'],
        orientation='h', marker_color=COLORS['primary'], opacity=0.85,
    ))
    fig_region.add_trace(go.Bar(
        name='Profit', y=region_df['Region'],
        x=region_df['Profit'],
        orientation='h', marker_color=COLORS['success'], opacity=0.85,
    ))
    fig_region.update_layout(**base_layout("Revenue & Profit by Region"),
                             barmode='group')

    # ── Chart 6: Segment donut ───────────────────
    seg = dff.groupby('Segment')['Sales'].sum().reset_index()

    fig_seg = go.Figure(go.Pie(
        labels=seg['Segment'],
        values=seg['Sales'],
        hole=0.55,
        marker_colors=[COLORS['primary'], COLORS['warning'], COLORS['success']],
        textinfo='label+percent',
        textfont_size=12,
    ))
    fig_seg.update_layout(**base_layout("Revenue by Customer Segment"))
    fig_seg.update_layout(showlegend=False)

    return (kpi_rev, kpi_pro, kpi_ord, kpi_mar,
            fig_trend, fig_cat, fig_sub,
            fig_disc, fig_region, fig_seg)


# ── Run ──────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, port=8051)
