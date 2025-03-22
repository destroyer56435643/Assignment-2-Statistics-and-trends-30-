import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn; seaborn.set()




def Sep_df(Df):
    
    DfN = Df[2:]
    
    print (DfN)
    
    DfN.columns = DfN.iloc[0]
    DfN = DfN[1:]
    
    return DfN 


def filter_rows_by_value(df, column_name, Names, SecColm_name, value):
    
    FT = df[df[column_name].isin(Names)]
    
    FP = FT[FT[SecColm_name] == value]
    
    FP = FP.drop(columns = ['Country Code','Indicator Name','Indicator Code'])
    
    FP = FP = FP.set_index('Country Name')
    
    FP = FP.dropna(axis = 1)
    
    FT = FP.T
    
    FP = FP.astype(int)
    
    FT = FT.astype(int)
    
    
    
    return FP,FT

pop  = pd.read_excel('API_19_DS2_en_excel_v2_3027.xls')
Co2 = pd.read_excel('API_EN.GHG.CO2.MT.CE.AR5_DS2_en_excel_v2_2338.xls')
Count = ['United Kingdom','Argentina','Afghanistan']

UK = ['United Kingdom']


pop_Countries = Sep_df(pop)
Urban_pop, YearsDf = filter_rows_by_value(pop_Countries,'Country Name', Count,'Indicator Name','Urban population')
Pop_co2 = Sep_df(Co2)
Co2Count,Co2Year = filter_rows_by_value(Pop_co2, 'Country Name' , Count , 'Indicator Name' , 'Carbon dioxide (CO2) emissions (total) excluding LULUCF (Mt CO2e)')
UK_Acess_E,UK_Acess_e_years = filter_rows_by_value(pop_Countries,'Country Name', UK, 'Indicator Name', 'Electric power consumption (kWh per capita)')

Total_pop,Total_pop_Years = filter_rows_by_value(pop_Countries, 'Country Name', Count, 'Indicator Name', 'Population, total')

Temp_co2 = Co2Year.iloc[0:45]
Temp_Years = UK_Acess_e_years.iloc[10:]
filt_Years  = YearsDf.iloc[10:]
filt_Pop = Total_pop_Years[10:]

desc_of_pop = Co2Year.describe()

Temp_pop_Co2_Years = Total_pop_Years.iloc[-20:]

Temp_Co22 = Co2Year.iloc[-20:]


x1, x2 = Temp_Years['United Kingdom'].iloc[0], Temp_Years['United Kingdom'].iloc[-1]
y1, y2 = Temp_co2['United Kingdom'].iloc[0], Temp_co2['United Kingdom'].iloc[-1]

AROC = (y2 - y1) / (x2 - x1)

plt.figure(figsize = (10,6))

plt.plot(filt_Years['Argentina'],Co2Year['Argentina'])



plt.ticklabel_format(style='plain', axis='x')
plt.ylabel('Total Co2 Emissions (Mt)', fontweight = 'bold')
plt.xlabel('Urban Pop of Argentina', fontweight = 'bold')
plt.title('Correlation between Urban Pop and Co2 Emissions of Argentina',fontweight = 'bold',fontsize = 15)


plt.show()

plt.figure()

plt.scatter(Temp_Years['United Kingdom'],Temp_co2['United Kingdom'])

plt.xlabel('Electric Power Consumption (kWh per capita', fontweight = 'bold',fontsize = 10)
plt.ylabel('Total Co2 Emissions (Mt)',fontweight = 'bold', fontsize = 10)
plt.title('Electric Power Consumptions vs Total Co2 Emissions' , fontweight = 'bold')
plt.show()


plt.figure (figsize = (8,5))

plt.scatter(filt_Pop['Afghanistan'],Co2Year['Afghanistan'])

plt.ticklabel_format(style='plain', axis='x')
plt.ylabel('Total Co2 Emissions (Mt)',fontweight = 'bold')
plt.xlabel('Total population',fontweight = 'bold')
plt.title('Total Co2 emissions compaired with the total population', fontweight = 'bold')

plt.show()




    




    

    