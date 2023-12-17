# Discord-Stock-bot
A simple to use discord stock bot with graphs!

This was just a little project I did in my free time, I'm sure there are other bots that do this but this is lightweight and customizable.

It utilizes yahoo finance, and obviously the discord module, so make sure to run "pip install discord yfinance" to download necessary libraries

I think there's some error with how the graph is created, but it's mostly OK, although there are occasional missing points where it just creates a long line instead of a proper graph. 

To set this up you just need to go to the developer portal in discord, make an app, make a bot and retrieve it's bot token, then place it in this code. Once you give the bot permissions in the dev portal and invite it to the server, start up the bot on your PC (or wherever) and it should work with the command "/stock aapl 1d" or "/stock nio 4 mo"

If you dont specify a time period itll just default to 7 days
