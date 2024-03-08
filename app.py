import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

penguins_df = palmerpenguins.load_penguins()

# Get the Data
# go back and ediit/update

ui.page_opts(title="Sandra's Palmer Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
