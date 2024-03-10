# cintel-02-data
Working with Data Sources-Palmer Penguins
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

penguins_df = palmerpenguins.load_penguins()

# Get the Data-Always familarize yourself with the dataset you are working with first.
#column names for penguins inclue:
# species: penguin species (Chinstrap, Adelie, or Gentoo)
#island: island name (Dream, Torgersen, or Biscoe) in Palmer Archipelago
#bill_length_mm: length of bill in millimeters
#bill_depth_mm: depth of bill in millimeters
#flipper_length_mm: lenrth of the flipper in millimeters
#body_mass_g: body mass in grams
#sex: MALE or FEMALE

#Load the dataset into a pandas DataFrame.
penguins_df =palmerpenguins.load_penguins()

# Define User Interface (ui)
ui.page_opts(title = "Sandra's Practice of Palmer Penguin Data"


ui.page_opts(title="Sandra's Palmer Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
