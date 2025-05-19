import pandas as pd
import vizro.plotly.express as px
from vizro import Vizro
from vizro import charts as vz
import vizro.models as vm

# Load Walmart Sales Data
file_path = 'Walmart_Sales.csv'
df = pd.read_csv(file_path)

# Preprocess Data
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.sort_values('Date', inplace=True)

# --- KPI Analyses ---
# Weekly Sales by Store
sales_by_store = df.groupby('Store')['Weekly_Sales'].sum().reset_index().sort_values(by='Weekly_Sales', ascending=False)

# Weekly Sales Over Time
sales_over_time = df.groupby('Date')['Weekly_Sales'].sum().reset_index()

# Sales on Holiday vs Non-Holiday
holiday_sales = df.groupby('Holiday_Flag')['Weekly_Sales'].mean().reset_index()
holiday_sales['Holiday_Flag'] = holiday_sales['Holiday_Flag'].map({0: 'Non-Holiday', 1: 'Holiday'})

# Temperature vs Weekly Sales
temp_sales = df.groupby('Temperature')['Weekly_Sales'].mean().reset_index()

# CPI vs Weekly Sales
cpi_sales = df.groupby('CPI')['Weekly_Sales'].mean().reset_index()

# Unemployment vs Weekly Sales
unemp_sales = df.groupby('Unemployment')['Weekly_Sales'].mean().reset_index()

# --- Vizro Dashboard Components ---
page1 = vm.Page (
        id="page1",
        title="Dashboard-1",
        components=[
            vm.Graph(figure=px.bar(sales_by_store, x='Store', y='Weekly_Sales', title='Total Weekly Sales by Store', color='Weekly_Sales')),
            vm.Graph(figure=px.line(sales_over_time, x='Date', y='Weekly_Sales', title='Weekly Sales Over Time')),
        ]
    )

page2 = vm.Page (
        id="page2",
        title="Dashboard-2",
        components=[
            vm.Graph(figure=px.bar(holiday_sales, x='Holiday_Flag', y='Weekly_Sales', title='Avg Weekly Sales: Holiday vs Non-Holiday', color='Holiday_Flag')),
            vm.Graph(figure=px.scatter(temp_sales, x='Weekly_Sales', y='Temperature', title='Temperature vs Weekly Sales')),
        ]
    )

page3 = vm.Page (
        id="page3",
        title="Dashboard-3",
        components=[
            vm.Graph(figure=px.scatter(cpi_sales, x='CPI', y='Weekly_Sales', title='CPI vs Weekly Sales')),
            vm.Graph(figure=px.line(unemp_sales, x='Unemployment', y='Weekly_Sales', title='Unemployment vs Weekly Sales')),
        ]
    )

page4 = vm.Page (
        id="page4",
        title="Combined Dashboard",
        layout=vm.Grid(grid=[[0, 0, 3, 4],
                            [1, 2, 5, 5]]),
        components=[
            vm.Graph(figure=px.bar(sales_by_store, x='Store', y='Weekly_Sales', title='Total Weekly Sales by Store', color='Weekly_Sales')),
            vm.Graph(figure=px.line(sales_over_time, x='Date', y='Weekly_Sales', title='Weekly Sales Over Time')),
            vm.Graph(figure=px.bar(holiday_sales, x='Holiday_Flag', y='Weekly_Sales', title='Avg Weekly Sales: Holiday vs Non-Holiday')),
            vm.Graph(figure=px.scatter(temp_sales, x='Weekly_Sales', y='Temperature', title='Temperature vs Weekly Sales')),
            vm.Graph(figure=px.scatter(cpi_sales, x='CPI', y='Weekly_Sales', title='CPI vs Weekly Sales')),
            vm.Graph(figure=px.line(unemp_sales, x='Unemployment', y='Weekly_Sales', title='Unemployment vs Weekly Sales'))
        ]
    )


# Create Dashboard
dashboard = vm.Dashboard(pages=[page1, page2, page3, page4],
                         navigation=vm.Navigation(
                             pages={"Story": ["page1", "page2", "page3"], "Combined-Dash": ["page4"]},
                             nav_selector=vm.NavBar()
                         ), title="Walmart Sales Dashboard")

# Run Vizro App
Vizro().build(dashboard).run()