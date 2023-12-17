import discord
from discord.ext import commands
import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime, timedelta

TOKEN = 'your_bot_token'
PREFIX = '/'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='stock')
async def stock(ctx, symbol, period='7d'):
    try:
        stock_data = yf.Ticker(symbol)

        period = str(period)
        # you can add more time periods, it's easily customizable
        valid_periods = ['1d','2d','3d','4d','5d','6d','7d','8d','9d','10d','11d','12d','13d','14d','15d','16d','17d','18d','1mo','2mo','3mo','4mo','5mo','6mo','7mo','8mo','9mo','10mo','11mo','12mo','1y','2y','5y','10y','max']
        if period not in valid_periods:
            await ctx.send(f"Invalid time period. Please use one of the following: {', '.join(valid_periods)}")
            return

        work = '1h' if period in ['1d','2d','3d','4d','5d','6d','7d','8d','9d','10d'] else '1d'
        
        # Fetch historical data for the specified period
        historical_data = stock_data.history(period=period, interval=work)['Close']

        # Generate and send a time series plot with custom styling
        plt.figure(figsize=(10, 5), facecolor='black')  # background color of the plot
        plt.plot(historical_data.index, historical_data.values, color='lime', linewidth=3)  # line color and thickness
        plt.title(f"{symbol} Stock Price ({period.capitalize()})", color='lime')  # title color
        plt.xlabel('Time', color='lime')  # Set x-axis label color to green
        plt.ylabel('Closing Price (USD)', color='lime')  # y-axis label color

        # Customize ticks and grid
        plt.xticks(rotation=45, ha='right', color='lime')  # x-axis tick label color
        plt.yticks(color='lime')  # y-axis tick label color
        plt.grid(color='darkgreen', linestyle='--', linewidth=0.5)  # grid color

        # Saves plot to BytesIO object
        image_stream = BytesIO()
        plt.tight_layout()
        plt.savefig(image_stream, format='png', facecolor='black')  # background color
        plt.close()

        # ngl I dont even know what \/ this does but it works
        image_stream.seek(0)

        # sends image
        await ctx.send(f"**{stock_data.info['longName']} ({symbol})**\n"
                       f"Current Price: {stock_data.info['ask']} USD\n"
                       f"Previous Close: {stock_data.info['regularMarketPreviousClose']} USD\n"
                       f"Open: {stock_data.info['regularMarketOpen']} USD\n"
                       f"Day Range: {stock_data.info['regularMarketDayLow']} - {stock_data.info['regularMarketDayHigh']} USD",
                       file=discord.File(image_stream, 'stock_chart.png'))

    except Exception as e:
        await ctx.send(f"Error fetching stock data for {symbol}: {e}")

bot.run(TOKEN)
