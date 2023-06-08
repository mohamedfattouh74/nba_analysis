from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
sns.set_palette("RdBu")
sns.set_style("darkgrid")
plt.tight_layout()

team_name = []
games_played = []
wins = []
losses = []
win_percent = []
minutes = []
points = []
field_goals_made = []
field_goals_attempted = []
field_goals_percent = []
threes_made = []
threes_attempted = []
threes_percent = []
ft_made = []
ft_attempted = []
ft_percent = []
o_rebound = []
d_rebound = []
rebounds = []
assists = []
turnovers = []
steals = []
blocks = []
blocks_against = []
personal_fouls = []
year = []
images = []

website = "https://www.nba.com/stats/teams/traditional?SeasonType=Regular+Season&Season=2022-23&PerMode=Totals"
path = "C:/Users/LENOVO/Downloads/chromedriver"

driver = webdriver.Chrome(path)
driver.get(website)

options = driver.find_elements(By.XPATH, '//div[@class="nba-stats-primary-split-block"]/div[1]/label/div/select/option')

season_start = 2022

try:
    for option in options[0:9]:
        option = option.text
        website = f"https://www.nba.com/stats/teams/traditional?SeasonType=Regular+Season&Season={option}&PerMode=Totals"
        path = "C:/Users/LENOVO/Downloads/chromedriver"

        driver = webdriver.Chrome(path)
        driver.get(website)
        table = driver.find_element(By.CLASS_NAME, 'Crom_body__UYOcU')
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:

            try:

                team_name.append(row.find_element(By.TAG_NAME, "span").text)
                games_played.append(row.find_element(By.XPATH, './/td[3]').text)
                wins.append(row.find_element(By.XPATH, './/td[4]').text)
                losses.append(row.find_element(By.XPATH, './/td[5]').text)
                win_percent.append(row.find_element(By.XPATH, './/td[6]').text)
                minutes.append(row.find_element(By.XPATH, './/td[7]').text)
                points.append(row.find_element(By.XPATH, './/td[8]').text)
                field_goals_made.append(row.find_element(By.XPATH, './/td[9]/a').text)
                field_goals_attempted.append(row.find_element(By.XPATH, './/td[10]/a').text)
                field_goals_percent.append(row.find_element(By.XPATH, './/td[11]').text)
                threes_made.append(row.find_element(By.XPATH, './/td[12]/a').text)
                threes_attempted.append(row.find_element(By.XPATH, './/td[13]/a').text)
                threes_percent.append(row.find_element(By.XPATH, './/td[14]').text)
                ft_made.append(row.find_element(By.XPATH, './/td[15]').text)  # Free throws
                ft_attempted.append(row.find_element(By.XPATH, './/td[16]').text)
                ft_percent.append(row.find_element(By.XPATH, './/td[17]').text)
                o_rebound.append(row.find_element(By.XPATH, './/td[18]/a').text)
                d_rebound.append(row.find_element(By.XPATH, './/td[19]/a').text)
                rebounds.append(row.find_element(By.XPATH, './/td[20]/a').text)
                assists.append(row.find_element(By.XPATH, './/td[21]/a').text)
                turnovers.append(row.find_element(By.XPATH, './/td[22]/a').text)
                steals.append(row.find_element(By.XPATH, './/td[23]/a').text)
                blocks.append(row.find_element(By.XPATH, './/td[24]/a').text)
                blocks_against.append(row.find_element(By.XPATH, './/td[25]/a').text)
                personal_fouls.append(row.find_element(By.XPATH, './/td[26]/a').text)
                year.append(season_start)
                element = row.find_element(By.XPATH, '//div[contains(@class,'
                                                     '"StatsTeamsTraditionalTable_teamLogo")]/div/img')
                images.append(element.get_attribute('src'))


            except:

                team_name.append(None)
                games_played.append(None)
                wins.append(None)
                losses.append(None)
                win_percent.append(None)
                minutes.append(None)
                points.append(None)
                field_goals_made.append(None)
                field_goals_attempted.append(None)
                field_goals_percent.append(None)
                threes_made.append(None)
                threes_attempted.append(None)
                threes_percent.append(None)
                ft_made.append(None)  # Free throws
                ft_attempted.append(None)
                ft_percent.append(None)
                o_rebound.append(None)
                d_rebound.append(None)
                rebounds.append(None)
                assists.append(None)
                turnovers.append(None)
                steals.append(None)
                blocks.append(None)
                blocks_against.append(None)
                personal_fouls.append(None)
                year.append(None)
                images.append(None)

        season_start = season_start - 1
except:
    pass

nba_dict = {
    'team': team_name, 'games_played': games_played, 'wins': wins, 'losses': losses, 'win_percent': win_percent,
    'minutes': minutes, 'points': points, 'field_goals_made': field_goals_made,
    'field_goals_attempted': field_goals_attempted,
    'field_goals_percent': field_goals_percent, 'threes_made': threes_made, 'threes_attempted': threes_attempted,
    'threes_percent': threes_percent, 'ft_made': ft_made, 'ft_attempted': ft_attempted, 'ft_percent': ft_percent,
    'o_rebound': o_rebound, 'd_rebound': d_rebound, 'rebounds': rebounds, 'assists': assists, 'turnovers': turnovers,
    'steals': steals, 'blocks': blocks, 'blocks_against': blocks_against, 'personal_fouls': personal_fouls,
    "year": year,
    "image": images
}

nba_df = pd.DataFrame(nba_dict)

nba_df.to_csv('nba_data_RS_2022-2014.csv', index=False)

nba_df = nba_df.set_index("team")


