#  Stock Analysis Visualizer


## Introduction
My project is a tool for exploring and analyzing stock trends in a flexible, user-friendly way.

## Overview
This project is an interactive web application that allows users to visualize stock market data through customizable line charts. Users can choose from 7 technical indicators, select any specific stock, adjust the time intervals for the data, set their desired time period, and choose from 4 series types . The program generates a line chart based on these customized choices, displaying the selected data and technical analysis in an easy-to-understand visual format. I provided clear basic definitions for each input to guide users through the process of making informed choices. I placed the accordion of information in the middle so if the user already understands everything then they can simple selects their choices and scroll to the chart, but if they need that step-by-step information then it's right there next to the choices so they don't have to scroll back and forth between them.

## File Details
   ### Main File
    The file "app.py" contains routing, flask to display page and form for user, fetching between form and API.

   ### Supporting Files
    The file "trying.env" contains the alpha vantage key but protects it from someone else looking at the source code to steal it and use it for themselves.

    The file "help.py" contains the lookup and usd functions necessary to interact with the API as well as the error handling function.

    The file "create_db.py" creates the finance database used to keep count of how many successful API calls happen each day.

    The file "finance.db" contains the table called api_calls that has user id, the count of successful API calls for the day, and the date. Alpha vantage told me that I could have a free API key, but could only make 10 calls a day so I implemented this to keep track and make sure I don't go over the allotted amount as I want to maintain access.

   ### Templates
    The file "error.html" contains the bootstrap connection to make coding simpler and the html to display when an error has occured in the program.

    The file "index.html" contains the bootstrap connection, the form where the user can input or select the necessary information that the API call needs, an accordion with information about each choice the user will make when making the API call, the javascript connection that directs the program to "script.js", and the chart container where a chart will be displayed.

   ### Static Files
    The file "script.js" contains the chart creation, chart update, chart design choices, communication between the API and the chart, and the API calls count.

    The file "style.css" contains basic formatting and style changes for the user interface.


## Design Decisions
I readjusted the form inputs multiple times to get them to be straight across the page without being ontop of each other and different sizes, originally they displayed as multiple lines of options all at varying sizes. I wanted them to be consistent and simple so the user can focus on what they choose instead of being distracted by the design.

The default settings for the display of my page and chart were very jarring with a lot of white space which made it hard to look at for too long. I take it someone who is using this visualizer would be staring into the data points trying to make sense of the analysis so I wanted a dark background with bright accents that were still calming enough when combined.

I chose green since it's a calming and creative color. I thought about doing a dark grey background with green, yellow, and blue accenting colors, but opted for the lighter green background as it is still easy on eyes without being dull. I went through multiple iterations of yellow to make it as golden as possible. The topic of the website being how well stocks are doing made green and gold seem fitting because of how money is typically represented by those colors.

I went through different colors like grey and blue on the accordion and as accent colors, but opted for a lighter green so the accordion stuck out without being jarring, and then a blush pink that matched well with the green and gold. Since it ended up being lighter overall, I did use black text and black for the graph's lines to maintain readability.

## Challenges & Solutions
In the beginning, I had to figure out what API I could use for the project I was thinking about as I wanted to do something with finance or politics and I found Alpha Vantage. I read through the documentation and realized I could make something that helped me look up technical information about any stock and could build on more of its features later on as needed, but I knew I didn't want to parse through all of that raw data so I chose to make a chart.

I ultimately found chart.js, but working with chart.js proved difficult at times because I couldn't understand why the x-axis wouldn't simply display the time interval I was giving it; that made me dive deeper into multiple iterations of changing up how the API and chart.js communicate. Ultimately, I realized with some googling about overlay charts that the information being displayed wasn't what I had thought it was. The time interval was about the data points themselves and the calculations not the x-axis. This helped me also understand that I needed to take away the options for bar and pie graphs as the only graphing method that made sense for the data was a line graph. While looking into this, I realized the API and chart.js had different representations for the same values like 1min for API was 1 minute for chart.js so I added a section in the javascript to translate this between them.

It took me a while to get the database count to work because there was more to it than I initially thought, but CS50's duck helped me make everything work. I didn't realize I needed to create the database originally because I hadn't had to for my previous project, but it walked me through getting that done which is very easy. It recommended using the .env too which is why I named it "trying.env" because I hadn't known that existed and was taking a chance with the duck's advice.

When it came to my error handling, I had "error.html" because I knew I needed the display, but I had the help.py because I knew I needed the usd function as I had a lot of trouble with my previous project not working because that part got changed. I'm glad I had added the help.py to my project though because the duck helped me understand that I needed that error handling function in order to use my error.html without having to run as much code.

## Conclusion
I learned a lot while researching, building, fixing, and redesigning this project. Although we worked with the majority of the tools and concepts I used for this project in previous projects, this was my first time building and handling every step of the process on my own. Planning this out and deciding what API would work best, finding chart.js, reading the documentation for both to be able to make definitive decisions and see how every piece could fit together took longer than I anticipated. I gained an appreciation for how understanding all of these different languages can come in handy when wokring with what other people have built so you can make use of their creations to build something that's your own in a much smaller timeframe.

Learning about .env through the CS50 duck taught me about collaboration in a way because I'm not sure if I wouldv'e found that solution on my own. I was discussing how I wanted to keep the api key from being used by others and it gave me that option. I'm excited to collaborate with others and discover new tools and techniques. I know that I can do the research and find the solutions to any problem I encounter in my future projects because I just did it. Working with others and other AIs will likely dramatically increase my productivity and speed with which I can learn or find the information I need.

