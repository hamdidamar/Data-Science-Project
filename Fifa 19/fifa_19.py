
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_19.csv') #kullanacağımız kütüphaneler datamızı import ettik

fifa.head(5) # ilk 5 satırdaki verileri ekrana bastırdık
fifa.tail(5) # son 5 satırdaki verileri ekrana bastırdık

df = pd.DataFrame(fifa) #data frame oluşturduk

df.info() # data framemizin bilgilerini istedik

# data framemizi istediğimiz gibi temizlemeye başlıyoruz

df.columns # df'nin columnlarını sorduk

df.shape  #kaç satır ve sutun olduğunu sorguladık

df.isnull().any() #boş değer olup olmadığını sorguladık

chosen_columns = ['Name',
    'Age',
    'Nationality',
    'Overall',
    'Potential',
    'Special',
    'Acceleration',
    'Aggression',
    'Agility',
    'Balance',
    'BallControl',
    'Body Type',
    'Composure',
    'Crossing',
    'Curve',
    'Club',
    'Dribbling',
    'FKAccuracy',
    'Finishing',
    'GKDiving',
    'GKHandling',
    'GKKicking',
    'GKPositioning',
    'GKReflexes',
    'HeadingAccuracy',
    'Interceptions',
    'International Reputation',
    'Jersey Number',
    'Jumping',
    'Joined',
    'LongPassing',
    'LongShots',
    'Marking',
    'Penalties',
    'Position',
    'Positioning',
    'Preferred Foot',
    'Reactions',
    'ShortPassing',
    'ShotPower',
    'Skill Moves',
    'SlidingTackle',
    'SprintSpeed',
    'Stamina',
    'StandingTackle',
    'Strength',
    'Value',
    'Vision',
    'Volleys',
    'Wage',
    'Weak Foot',
    'Work Rate'
] #seçeceğimiz columnleri bir değişkene atıyoruz

df = pd.DataFrame(df, columns = chosen_columns) # ve yeniden şekillendiriyoruz

df.sample(5) #seçilenlerden rastgele 5 tanesini istiyoruz

df.set_index('Name', inplace=True) #indexi name göre yapıyoruz ve boş olanları atıyoruz
