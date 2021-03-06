import mplfinance as mpf
import matplotlib.animation as animation

import create_candles

from main import Broker
from candles import ReversalPatterns


class Animation:
    tik = input("Choose your destiny: ")
    Broker.dataframe = Broker.form_data(tik)
    dframe = Broker.dataframe

    # dframe = create_candles.create_c()

    last_time_index = dframe.index[-1]

    resample_map = {'Open': 'first',
                    'High': 'max',
                    'Low': 'min',
                    'Close': 'last'}
    resample_period = 'H'

    rs = dframe.resample(resample_period).agg(resample_map).dropna()

    new_candle = rs.iloc[-1]

    def get_new_candle(ticker):
        dframe = Broker.form_data(ticker)

        rs = dframe.resample(Animation.resample_period).agg(Animation.resample_map).dropna()


        if Animation.new_candle[0] != rs.iloc[-1][0] or Animation.new_candle[1] != rs.iloc[-1][1] or Animation.new_candle[2] != rs.iloc[-1][2] or Animation.new_candle[3] != rs.iloc[-1][3]:
            Animation.new_candle = rs.iloc[-1]
            return Animation.new_candle

        else:
            return Animation.get_new_candle(Animation.tik) #!



fig, axes = mpf.plot(Animation.dframe,
                     returnfig=True,
                     type="candle",
                     style=Broker.design_candle['style'],
                     mav=Broker.design_candle['mav'])
ax = axes[0]

ReversalPatterns.in_neck(Animation.rs)

mpf.show()

def animate(ival):

    nxt = Animation.get_new_candle(Animation.tik)

    Animation.dframe = Animation.dframe.append(nxt)


    ax.clear()

    if Animation.dframe.index[-1] != Animation.last_time_index:
        Animation.dframe = Animation.dframe.drop([Animation.dframe.index[0]])

    Animation.rs = Animation.dframe.resample(Animation.resample_period).agg(Animation.resample_map).dropna()

    Animation.last_time_index = Animation.dframe.index[-1]

    ReversalPatterns.hammer(Animation.rs)
    ReversalPatterns.hanging_man(Animation.rs)
    ReversalPatterns.engulfing_pattern(Animation.rs)
    ReversalPatterns.dark_cloud_cover(Animation.rs)
    ReversalPatterns.piercing_pattern(Animation.rs)
    ReversalPatterns.on_neck(Animation.rs)
    ReversalPatterns.in_neck(Animation.rs)

    mpf.plot(Animation.rs, ax=ax,
            type="candle",
            style=Broker.design_candle['style'],
            mav=Broker.design_candle['mav']
            )


ani = animation.FuncAnimation(fig, animate, interval=10000)

mpf.show()
