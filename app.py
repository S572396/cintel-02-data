import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from shiny import reactive, render, req
from palmerpenguins import load_penguins
import seaborn as sns


# Load palmer penguins data set
penguins_df = palmerpenguins.load_penguins()

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

#Use ui.hr() to add a horizontal rule to the sidebar
ui.hr("Number of Seaborn bins")

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
ui.input_checkbox_group(
    "selected_species_list",
    "Select Species",
    ["Adelie", "Gentoo", "Chinstrap"],
    selected=["Adelie"],
    inline=True
)

with ui.layout_columns():

    @render_plotly
    def plot1_plotly():
        return px.histogram(penguins_df, x="flipper_length_mm", color="species", marginal="box")


with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")


# Plotly Histogram
with ui.layout_columns():

    @render_plotly
    def plot1():
        fig = px.histogram(penguins_df, x="flipper_length_mm", color="species", marginal="box")
        return fig

    @render_plotly
    def plot2():
        fig = px.histogram(penguins_df, x="flipper_length_mm", color="species", marginal="box")
        return fig

# Seaborn Histogram
with ui.layout_columns():

    @render_plotly
    def plot3():
        # Seaborn Histogram
        sns.set(style="whitegrid")
        g = sns.histplot(data=penguins_df, x="flipper_length_mm", hue="species", element="step", common_norm=False)
        return g.figure

    @render_plotly
    def plot4():
        # Seaborn Histogram
        sns.set(style="whitegrid")
        g = sns.histplot(data=penguins_df, x="flipper_length_mm", hue="species", element="step", common_norm=False)
        return g.figure

# Scatter plot
@render_plotly
def Penguin_Species_Plot():
    plotly_scatter = px.scatter(
        penguins_df,
        x="bill_depth_mm",
        y="bill_length_mm",
        color="species",
        labels={"bill_depth_mm": "X Label", "bill_length_mm": "Y Label"},
        title="Penguin Species Plot",
    )
    return plotly_scatter




