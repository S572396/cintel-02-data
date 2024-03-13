import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from shiny import reactive, render, req
from palmerpenguins import load_penguins  # Import the palmerpenguins library

import seaborn as sns

# Load palmer penguins data set
penguins_df = load_penguins()  # Use the function directly without specifying the module

# Set title page
ui.page_opts(title="Sandra's Palmer Penguin Data", fillable=True)

# Create sidebar with open parameter and 2nd level header
with ui.sidebar(collapsed=False):
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 10)
    ui.h2("Sidebar")

    # Use ui.input_selectize() to create a dropdown input to choose a column
    ui.input_selectize(
        "selected_attribute",
        "Select Plotly Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    )

    # Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
    ui.input_numeric("plotly_bin_count", "Number of Plotly bins", 20)

    # Use ui.input_slider() to create a slider input for the number of Seaborn bins
    ui.input_slider("seaborn_bin_count", "Number of Seaborn bins", 0, 100, 20)

    # Use ui.hr() to add a horizontal rule to the sidebar
    ui.hr("Number of Seaborn bins")

    # Use ui.a() to add a hyperlink to the sidebar
    ui.a("GitHub", href="https://github.com/S572396/cintel-02-data", target="_blank") 

    # Use ui.input_checkbox_group() to create a checkbox group input to filter the species
    ui.input_checkbox_group(
        "selected_species_list",
        "Select Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie"],
        inline=True
    )





