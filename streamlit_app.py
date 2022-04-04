# my_dashboard.py
import numpy as np
from scipy.stats import norm
import streamlit as st
from bokeh.plotting import figure
from bokeh.models import HoverTool

st.title('Normal distribution')

mu_in = st.slider('Mean', value=5, min_value=-10, max_value=10)
std_in = st.slider('Standard deviation',
                   value=5.0,
                   min_value=0.0,
                   max_value=10.0)
size = st.slider('Number of samples', value=100, max_value=500)


def norm_dist(mu, std, size=100):
    """Generate normal distribution."""
    return norm.rvs(mu, std, size=size)


data = norm_dist(mu_in, std_in, size=size)

# Fit the normal distribution
mu, std = norm.fit(data)

# Make some plots
x = np.linspace(-40, 40, 100)
y = norm.pdf(x, mu, std)

title = f"Fit results: {mu=:.2f},  {std=:.2f}"

hist, edges = np.histogram(data, bins=50, density=True)

fig = figure(
    title=title,
    x_axis_label='x',
    y_axis_label='y',
)

quad = fig.quad(top=hist,
                bottom=0,
                left=edges[:-1],
                right=edges[1:],
                line_color="white",
                alpha=0.5)

line = fig.line(x, y, legend_label='Fit', line_width=2, line_color='red')

fig.add_tools(
    HoverTool(renderers=[quad],
              tooltips=[
                  ('value', '@top{0.00}'),
              ],
              point_policy='follow_mouse'))

st.bokeh_chart(fig, use_container_width=True)
