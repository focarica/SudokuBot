# Sudoku Bot

A small project created to solve Sudoku puzzles on the website [sudokutable.com](https://sudokutable.com). This project was developed purely for learning purposes during my studies on web scraping. (I did this in 2021/2022, but recently i wanted make it more understandable and easier for others to use)

## Prerequisites
* Python 3.x
* Chrome
* Git

## Installation 
1. Clone the repository:
    ```        
    git clone https://github.com/focarica/SudokuBot.git
    cd SudokuBot
    ```

2. Create and Active a venv:

    If Windows
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

    If MacOs or Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies
    ```
    pip install -r requirements.txt
    ```

4. Download chromedriver

    If you using a version of Chrome < 115, please follow this link and install your version:

    [Chrome until version 115](https://developer.chrome.com/docs/chromedriver/downloads)

    If your version > 115, plese folow this link and install your version:

    [Chrome version bigger 115](https://googlechromelabs.github.io/chrome-for-testing/)

    Paste the chromedriver file into [driver dir](https://github.com/focarica/SudokuBot/tree/main/driver) in your work environment.

## Use

1. Run the application.

```
python3 main.py
```


## Important Note

Make sure to update the `chromedriver` according to the current version of Chrome installed on your machine. If you want to understand the program but don't want to read all the code, feel free to read [summary file](https://github.com/focarica/SudokuBot/blob/main/summary.md).
