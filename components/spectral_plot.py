import plotly.graph_objects as go

def plot_spectrum(wavelengths, spectrum):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=wavelengths, y=spectrum, mode='lines', name='Transmission'))
    fig.update_layout(title='Simulated Transmission Spectrum', xaxis_title='Wavelength (μm)', yaxis_title='Transit Depth')
    return fig
