import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

penguins_df = palmerpenguins.load_penguins()

# Get the Data
# go back and edit/update

#REQUIREMENTS:

#- the overall page to have a title
#-a sidebar with input components
#-the main content will include a data table, data grid, and some charts

ui.page_opts(title="Sandra's Palmer Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
