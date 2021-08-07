#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 데이터분석을 위한 pandas, 시각화를 위한 matplotlib, seaborn을 불러옴
import matplotlib
import pandas as pd

# 코로나 발생 이전인 2019년 01월부터 2021년 06월까지
# 온라인쇼핑몰 거래량 합계 도출
CHART_NAME = 'onlineShopping02'
cnt, PNG, UNDERBAR = 0, '.png', '_'
filename = 'C:/Users/kim/Desktop/analysis/onlineshopping_201901_202106.csv'

# pd.read_csv(경로): 해당 csv를 읽어와 DataFrame Type으로 변환
#컬럼 색인 정보 출력
data = pd.read_csv(filename, index_col=['상품군별','범위별'], encoding='euc-kr')
print(data.columns)


# In[2]:


# DataFrame명.head() : data의 상단을 보여준다(default는 5)
data.head(9)


# In[3]:


# 코로나 시기 수요가 많았을 것으로 예측되는 '가전·전자·통신기기'와 
# 수요가 적었을 것으로 예측되는 '의복'의 쇼핑몰 취급상품범위별 거래량을 y축으로 두고
# 2019년 01월부터 2021년 06월까지의 월을 x축으로 두는 꺾은선 그래프 생성
PRODUCT = ['가전·전자·통신기기', '의복']
WHEN = ['2019. 01', '2019. 02', '2019. 03', '2019. 04',
       '2019. 05', '2019. 06', '2019. 07', '2019. 08', '2019. 09', '2019. 10',
       '2019. 11', '2019. 12', '2020. 01', '2020. 02', '2020. 03', '2020. 04',
       '2020. 05', '2020. 06', '2020. 07', '2020. 08', '2020. 09', '2020. 10',
       '2020. 11', '2020. 12', '2021. 01', '2021. 02', '2021. 03', '2021. 04',
       '2021. 05 p)', '2021. 06 p)']
chartdata2 = data.loc[PRODUCT, WHEN]
chartdata2 = chartdata2.T


# In[6]:


print(chartdata2)


# In[7]:


import matplotlib.pyplot as plt
matplotlib.font_manager._rebuild()

#font 경로
font_path = "C:/Windows/Fonts/나눔스퀘어 보통.ttf"

#font 설정
matplotlib.rc('font',family='NanumSquare')

# 온라인쇼핑몰 상품군별 취급상품범위별 거래량 꺽은선그래프 그리기
chartdata2.plot(title='secondGraph')

plt.grid(True)
plt.xlabel('시점', labelpad=15)
plt.ylabel('상품군별 취급상품범위별 거래량 합계', labelpad=20)
plt.title('온라인쇼핑몰 상품군별 취급상품범위별 월별 거래량 합계')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')


# In[ ]:




