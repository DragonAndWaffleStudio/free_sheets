# free_sheets
Download your favorite sheets from Musescore! Use it while it works...

To install use:
```
$ git clone https://github.com/DragonAndWaffleStudio/free_sheets.git
$ pip install .
```

To run use:
```
$ free_sheets <url>
```
and then input the musescore link and press enter.

## Requirements:
* Python3
* requests <code>$ pip install requests</code>
* cairosvg <code>$ pip install cairosvg</code> (this package requieres cairo, so use `$ brew install cairo`)
* selenium <code>$ pip install selenium</code>
* PyPDF2 <code>$ pip install PyPDF2</code>
* Firefox Webdriver (altho you can use a chrome one I guess if you change the code a bit) at https://github.com/mozilla/geckodriver/releases
