
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

df.describe() # data framemizin count,mean,standart devision,minimum Q1,Q3,medyan ve maximun gibi değerleri sorguladık

df['Nationality'].value_counts().head() #En fazla oyuncu olan ülkelerin ilk 5 tanesi

df['Nationality'].value_counts().tail() #En fazla oyuncu olan ülkelerin son 5 tanesi

df['Club'].value_counts().head(10) #En çok oyunculu klüpler ilk 10 tanesi

en_genc = df.sort_values('Age', ascending = True)[[ 'Age', 'Club', 'Nationality']].head(10) #En genç 10 oyuncunun yaş,club ve nationality den oluşan framesini oluşturduk.
en_yasli = df.sort_values('Age', ascending = False)[['Age', 'Club', 'Nationality']].head(10) #En yaşlıların ilk 10 tanesini oluşturduk

sns.set(style="darkgrid") 
ax = sns.countplot(x = 'Position' ,data = df) 
ax.set_title(label='Pozisyondaki Oyuncu Sayısı', fontsize=30);
plt.show() #seaborn kütüphanesini kullanarak bir countplot oluşturduk ve ekrana bastık

