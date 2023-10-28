import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
# import plotly.io as pio


def plotting():
    print('I am here')

    df = pd.read_csv('CalculatedData.csv') # LOADING THE DATAFRAME


    # ---------------- CREATING BARCHART FOR WATTS TABLE -----------------------------
    colors = ['#AEFF00','#00FF3C','#00FFFB','#0073FF','#B300FF','#FF00AA','#FF00FF','#FF6200','#FF0000','#151794']

    fig = go.Figure(data=[
        go.Bar(x = df.Name_of_appliance, y = df['Total Watts'],
            marker_color = colors, text =df['Total Watts'])
    ])

    fig.update_layout(
    title = 'Total watts used by each appliances'
    )

    fig.show()
    # ------------------------------------------------------------------------------



    # ----------------- CREATING PIECHART FOR TOTAL ENERGY COLUMN ----------------------
    fig1 = go.Figure(data = [
        go.Pie(labels = df['Name_of_appliance'], values = df['Energy'],
            hoverinfo = 'label+value', textinfo = 'label+percent',
            textfont = dict(size = 18),
            marker = dict(colors = colors, line = dict(color = '#000000', width = 3)))
    ])

    fig1.update_layout(
        height = 800,
        width = 800,
        title = 'Total Energy used by Each appliances'
    )
    fig1.show()

    # ---------------------------------------------------------------------------------



    # ----------------------------- CONVERTING PLOTS TO PDF FORMAT FILE ---------------------
    # plotly.io.write_image(fig, 'output_file.pdf', format='pdf')
    # plotly.io.write_image(fig1, 'PieChart.pdf', format='pdf')
    # # fig.write_image('Header.pdf')
    # fig1.write_image('footer.pdf')
    # --------------------------------------------------------------------------------------
    print('endof bloc')


if __name__ == "__main__":
    plotting()
