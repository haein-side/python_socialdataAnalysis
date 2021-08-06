#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib


# In[2]:


CHART_NAME = 'onlineShopping'
cnt, PNG, UNDERBAR = 0, '.png', '_'
filename = 'C:/Users/kim/Desktop/analysis/onlineshopping_201901_202106.csv'


# In[5]:


#컬럼 색인 정보 출력

import pandas as pd
data = pd.read_csv(filename, index_col=['상품군별','범위별'], encoding='euc-kr')
#data = data[index_col['상품군별'] == "합계" and index_col['범위별'] == "계"]
print(data.columns)


# In[12]:


#drop_cols = ['합계, 종합몰','합계, 전문몰']
#PRODUCT = data.drop(drop_cols, axis=1)
PRODUCT = ['합계']
WHEN = ['2019. 01', '2019. 02', '2019. 03', '2019. 04',
       '2019. 05', '2019. 06', '2019. 07', '2019. 08', '2019. 09', '2019. 10',
       '2019. 11', '2019. 12', '2020. 01', '2020. 02', '2020. 03', '2020. 04',
       '2020. 05', '2020. 06', '2020. 07', '2020. 08', '2020. 09', '2020. 10',
       '2020. 11', '2020. 12', '2021. 01', '2021. 02', '2021. 03', '2021. 04',
       '2021. 05 p)', '2021. 06 p)']

chartdata3 = data.loc[PRODUCT, WHEN]
chartdata3 = chartdata3.T


# In[9]:


print(chartdata3)


# In[10]:


import matplotlib
import matplotlib.pyplot as plt

import matplotlib 
matplotlib.font_manager._rebuild()

font_path = "C:/Windows/Fonts/나눔손글씨 다행체.ttf"

#폰트 이름 얻어오기
#font_name = font_manager.FontProperties(fname=font_path).get_name()

#font 설정
matplotlib.rc('font',family='Nanum DahaengCe')

chartdata3.plot(title='firstGraph')

plt.grid(True)
plt.xlabel('일자')
plt.ylabel('상품군 거래량 합계')
plt.title('일자별 거래량 합계')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')


# In[ ]:




