# Programming vacancies compare

This is python console app making statistics with vacancies and average salary by programming languages using API
of two popular russian job websites - HeadHunter and SuperJob

### How to install

You'll need to create an environment variable or create a .env file with your SuperJob token:
```
SUPERJOB_TOKEN='your superjob token'
```

Then run the script with 
```
python3 main.py
```
The result will be kind of
```
╔HeadHunter Moscow══════╦══════════════════╦═════════════════════╦══════════════════╗
║ Язык программирования ║ Вакансий найдено ║ Вакансий обработано ║ Средняя зарплата ║
╠═══════════════════════╬══════════════════╬═════════════════════╬══════════════════╣
║ Python                ║ 1517             ║ 341                 ║ 155925           ║
║ JavaScript            ║ 2000             ║ 776                 ║ 138599           ║
║ Java                  ║ 1999             ║ 451                 ║ 179467           ║
║ Swift                 ║ 298              ║ 95                  ║ 185489           ║
║ Go                    ║ 441              ║ 87                  ║ 190574           ║
║ C#                    ║ 954              ║ 260                 ║ 154944           ║
║ C++                   ║ 125              ║ 54                  ║ 133267           ║
║ Scala                 ║ 163              ║ 28                  ║ 219565           ║
║ Kotlin                ║ 430              ║ 127                 ║ 202038           ║
║ Ruby                  ║ 163              ║ 58                  ║ 167118           ║
╚═══════════════════════╩══════════════════╩═════════════════════╩══════════════════╝

╔SuperJob Moscow════════╦══════════════════╦═════════════════════╦══════════════════╗
║ Язык программирования ║ Вакансий найдено ║ Вакансий обработано ║ Средняя зарплата ║
╠═══════════════════════╬══════════════════╬═════════════════════╬══════════════════╣
║ Python                ║ 114              ║ 40                  ║ 142325           ║
║ JavaScript            ║ 212              ║ 130                 ║ 121623           ║
║ Java                  ║ 92               ║ 40                  ║ 145185           ║
║ Swift                 ║ 6                ║ 4                   ║ 152500           ║
║ Go                    ║ 24               ║ 12                  ║ 205000           ║
║ C#                    ║ 70               ║ 40                  ║ 117600           ║
║ C++                   ║ 60               ║ 40                  ║ 129525           ║
║ Scala                 ║ 16               ║ 2                   ║ 180000           ║
║ Kotlin                ║ 14               ║ 6                   ║ 152000           ║
║ Ruby                  ║ 6                ║ 2                   ║ 60000            ║
╚═══════════════════════╩══════════════════╩═════════════════════╩══════════════════╝
```
### Python3 should be already installed. 

Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).