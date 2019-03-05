{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')\n",
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "5    2017-01-10  131.270004  132.220001  129.289993  129.889999  129.889999   \n",
      "6    2017-01-11  130.910004  131.500000  129.250000  130.500000  130.500000   \n",
      "7    2017-01-12  130.630005  130.850006  128.500000  129.179993  129.179993   \n",
      "8    2017-01-13  131.149994  133.929993  130.580002  133.699997  133.699997   \n",
      "9    2017-01-17  135.039993  135.399994  132.089996  132.889999  132.889999   \n",
      "10   2017-01-18  133.210007  133.649994  131.059998  133.259995  133.259995   \n",
      "11   2017-01-19  142.009995  143.460007  138.250000  138.410004  138.410004   \n",
      "12   2017-01-20  139.360001  140.789993  137.660004  138.600006  138.600006   \n",
      "13   2017-01-23  138.649994  139.490005  137.309998  137.389999  137.389999   \n",
      "14   2017-01-24  138.110001  140.929993  137.029999  140.110001  140.110001   \n",
      "15   2017-01-25  140.800003  141.389999  139.050003  139.520004  139.520004   \n",
      "16   2017-01-26  140.449997  141.210007  138.509995  138.960007  138.960007   \n",
      "17   2017-01-27  139.460007  142.490005  139.000000  142.449997  142.449997   \n",
      "18   2017-01-30  141.770004  141.970001  138.800003  141.220001  141.220001   \n",
      "19   2017-01-31  140.550003  141.830002  139.699997  140.710007  140.710007   \n",
      "20   2017-02-01  141.199997  142.410004  139.300003  140.779999  140.779999   \n",
      "21   2017-02-02  140.610001  141.039993  139.050003  139.199997  139.199997   \n",
      "22   2017-02-03  139.509995  140.639999  139.100006  140.250000  140.250000   \n",
      "23   2017-02-06  140.000000  141.000000  139.160004  140.970001  140.970001   \n",
      "24   2017-02-07  141.490005  144.279999  141.050003  144.000000  144.000000   \n",
      "25   2017-02-08  143.570007  145.070007  142.559998  144.740005  144.740005   \n",
      "26   2017-02-09  144.979996  145.089996  143.580002  144.139999  144.139999   \n",
      "27   2017-02-10  144.679993  145.300003  143.970001  144.820007  144.820007   \n",
      "28   2017-02-13  145.190002  145.949997  143.050003  143.199997  143.199997   \n",
      "29   2017-02-14  143.199997  144.110001  140.050003  140.820007  140.820007   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "221  2017-11-16  194.330002  197.699997  193.750000  195.509995  195.509995   \n",
      "222  2017-11-17  195.740005  195.949997  192.649994  193.199997  193.199997   \n",
      "223  2017-11-20  193.300003  194.320007  191.899994  194.100006  194.100006   \n",
      "224  2017-11-21  195.039993  197.520004  194.970001  196.229996  196.229996   \n",
      "225  2017-11-22  196.580002  196.750000  193.630005  196.320007  196.320007   \n",
      "226  2017-11-24  196.649994  196.899994  195.330002  195.750000  195.750000   \n",
      "227  2017-11-27  195.559998  195.850006  194.000000  195.050003  195.050003   \n",
      "228  2017-11-28  195.339996  199.679993  194.009995  199.179993  199.179993   \n",
      "229  2017-11-29  198.910004  199.029999  184.320007  188.149994  188.149994   \n",
      "230  2017-11-30  190.309998  190.860001  186.679993  187.580002  187.580002   \n",
      "231  2017-12-01  186.990005  189.800003  185.000000  186.820007  186.820007   \n",
      "232  2017-12-04  189.360001  189.720001  178.380005  184.039993  184.039993   \n",
      "233  2017-12-05  183.500000  188.139999  181.190002  184.210007  184.210007   \n",
      "234  2017-12-06  183.380005  186.479996  182.880005  185.300003  185.300003   \n",
      "235  2017-12-07  185.710007  187.339996  183.220001  185.199997  185.199997   \n",
      "236  2017-12-08  186.500000  189.419998  186.300003  188.539993  188.539993   \n",
      "237  2017-12-11  187.850006  189.419998  185.910004  186.220001  186.220001   \n",
      "238  2017-12-12  186.009995  187.850006  184.820007  185.729996  185.729996   \n",
      "239  2017-12-13  186.100006  188.690002  185.410004  187.860001  187.860001   \n",
      "240  2017-12-14  187.979996  192.639999  187.199997  189.559998  189.559998   \n",
      "241  2017-12-15  189.610001  191.429993  188.009995  190.119995  190.119995   \n",
      "242  2017-12-18  191.199997  191.649994  188.899994  190.419998  190.419998   \n",
      "243  2017-12-19  190.179993  190.300003  185.750000  187.020004  187.020004   \n",
      "244  2017-12-20  187.940002  189.110001  185.259995  188.820007  188.820007   \n",
      "245  2017-12-21  189.440002  190.949997  187.580002  188.619995  188.619995   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "5     5985800      Q1  \n",
      "6     5615100      Q1  \n",
      "7     5388900      Q1  \n",
      "8    10515000      Q1  \n",
      "9    12183200      Q1  \n",
      "10   16168600      Q1  \n",
      "11   23203400      Q1  \n",
      "12    9497400      Q1  \n",
      "13    7433900      Q1  \n",
      "14    7754700      Q1  \n",
      "15    7238100      Q1  \n",
      "16    6038300      Q1  \n",
      "17    8323900      Q1  \n",
      "18    8122500      Q1  \n",
      "19    4411600      Q1  \n",
      "20    6033400      Q1  \n",
      "21    3462400      Q1  \n",
      "22    3512600      Q1  \n",
      "23    3552100      Q1  \n",
      "24    8573500      Q1  \n",
      "25    6887100      Q1  \n",
      "26    4555100      Q1  \n",
      "27    6171900      Q1  \n",
      "28    4790400      Q1  \n",
      "29    8355000      Q1  \n",
      "..        ...     ...  \n",
      "221   5678400      Q4  \n",
      "222   3906300      Q4  \n",
      "223   3827500      Q4  \n",
      "224   4787300      Q4  \n",
      "225   5895400      Q4  \n",
      "226   2160500      Q4  \n",
      "227   3210100      Q4  \n",
      "228   6981100      Q4  \n",
      "229  14202700      Q4  \n",
      "230   6630100      Q4  \n",
      "231   6219500      Q4  \n",
      "232   9069800      Q4  \n",
      "233   5783700      Q4  \n",
      "234   5490100      Q4  \n",
      "235   4659500      Q4  \n",
      "236   4987300      Q4  \n",
      "237   5298600      Q4  \n",
      "238   4265900      Q4  \n",
      "239   4710000      Q4  \n",
      "240   7792800      Q4  \n",
      "241   7285600      Q4  \n",
      "242   5011000      Q4  \n",
      "243   7033000      Q4  \n",
      "244   6545400      Q4  \n",
      "245   4729800      Q4  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Days\n",
    "#The DJI and NFLX files have a different date format than the NFLX_daily_by_quarter file. The DJI file lists a total stock price for multiple stocks.\n",
    "#netflix_stocks_quarterly contains a \"Quarter\" column"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.columns=['Date','Open','High','Low','Close','Price','Volume']\n",
    "dowjones_stocks.columns=['Date','Open','High','Low','Close','Price','Volume']\n",
    "netflix_stocks_quarterly.columns=['Date','Open','High','Low','Close','Price','Volume','Quarter']\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\patmo\\Anaconda3\\lib\\site-packages\\scipy\\stats\\stats.py:1713: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.\n",
      "  return np.add.reduce(sorted[indexer] * weights, axis=axis) / sumval\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "ax = sns.violinplot(x='Quarter',y='Price',data=netflix_stocks_quarterly)\n",
    "ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')\n",
    "ax.set_ylabel('Closing Stock Price')\n",
    "ax.set_xlabel('Business Quarters in 2017')\n",
    "plt.show()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "\n",
    "plt.scatter(x=x_positions,y=earnings_actual,color='red', alpha=.5)\n",
    "plt.scatter(x=x_positions,y=earnings_estimate,color='blue',alpha=.5)\n",
    "plt.legend([\"Actual\",\"Estimate\"])\n",
    "plt.xticks(x_positions,chart_labels)\n",
    "plt.title(\"Earnings Per Share in Cents\")\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 276,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([<matplotlib.axis.XTick at 0x2461fd77ac8>,\n",
       "  <matplotlib.axis.XTick at 0x2461fd80048>,\n",
       "  <matplotlib.axis.XTick at 0x2461fd80358>,\n",
       "  <matplotlib.axis.XTick at 0x2461e6436d8>],\n",
       " <a list of 4 Text xticklabel objects>)"
      ]
     },
     "execution_count": 276,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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aqLty2atIxHBihUrWLx4MaNHj653OGa2AWjoZq61a9ey9dZbO5F0kyS23nprX9GZ2XrT0MkEcCKpkevNzNanhk8mZmbW+Br6nkmlpjP/p0fnt/CCD3Rapl+/fuy00060tLQwevRorrvuOrbccssejcPMrK/rU8mkHjbZZBPmzp0LwLHHHsvll1/Ol770pTpHZfbW0tMnit3VlRNL65ibubph77335pln3vgX4V/72tfYfffd2XnnnTn33HMBOOOMM/j2t994A/jUqVP5+te/3m75hQsXsuOOO3LSSScxduxYDjroINasWQPAxIkT171i5vnnn6f13WWvv/46p59++rp5ffe73+31dTcz64iTSRe9/vrr/PKXv2TSpEkA3HHHHcyfP5+HHnqIuXPnMmfOHO69916mTJnC9Olv/PfQG2+8kaOOOqrd8gDz58/n05/+NE888QRbbrklN910U4exXHXVVQwZMoRZs2Yxa9Ysvve97/GnP/2p91bezKwTbubqxJo1axg3bhwLFy5kt912433vex+Qkskdd9zB+PHjAWhubmb+/PmccMIJLFu2jCVLlrB8+XK22mortttuOy655JKq5bfbbjtGjx7NuHHjANhtt91YuHBhhzHdcccdPProo8yYMQOA1atXM3/+fP+mxMzqxsmkE633TFavXs1hhx3G5ZdfzmmnnUZEcNZZZ/GJT3ziTdNMnjyZGTNm8OyzzzJlyhSAdssvXLiQgQMHruvv16/fumau/v3789e//hWgzW9GIoJLL72Ugw8+uMfX18ysFm7m6qIhQ4ZwySWXcPHFF/Paa69x8MEHc/XVV9Pc3AzAM888w7JlywCYMmUKN9xwAzNmzGDy5MkAHZZvT1NTE3PmzAFYdxXSOq/vfOc7vPbaawA8+eSTvPzyyz27wmZm3dCnrkzq/cTF+PHj2WWXXbjhhhs45phjmDdvHnvvvTcAgwcP5gc/+AHbbLMNY8eO5aWXXmLkyJEMHz4cgIMOOqhq+X79+rW7vC9+8YscffTRXHfddey///7rhp944oksXLiQXXfdlYhg2LBh3Hzzzb245mZmHWuY/wE/YcKEqPznWPPmzWPHHXesU0R9n+vP+go/Glw7SXMiYkK94+h2M5ekQZIekvSIpCcknVelzHGSlkuamz8n9ky4ZmbWiGpp5voLsH9ENEsaANwv6ecR8UBF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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = .8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars1_x,revenue_by_quarter)\n",
    "\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = .8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "\n",
    "plt.bar(bars2_x,earnings_by_quarter, color='Green')\n",
    "\n",
    "\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.legend(labels)\n",
    "plt.title(\"How does Revenue Compare to Earnings in the Last 4 Quarters?\")\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Revenue increases gradually and steadily over time.\n",
    "#Earnings also increases gradually and steadily over time. Earnings increase as revenue increases.\n",
    "#Roughly 10%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "# ax1 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "ax1 = plt.subplot(1,2,1)\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'], color='Green')\n",
    "ax1.set_title('Netflix')\n",
    "ax1.set_xlabel('Date')\n",
    "ax1.set_ylabel('Stock Price')\n",
    "\n",
    "ax2 = plt.subplot(1,2,2)\n",
    "plt.plot(dowjones_stocks['Date'],dowjones_stocks['Price'])\n",
    "ax2.set_xlabel('Date')\n",
    "ax2.set_ylabel(\"Stock Price\")\n",
    "ax2.set_title('Dow Jones')\n",
    "\n",
    "plt.subplots_adjust(wspace=.5)\n",
    "plt.suptitle(\"How did Netflix Compare to Dow Jones Industrial Average in 2017?\")\n",
    "plt.show()\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 293,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.savefig(\"How did Netflix Compare to Dow Jones Industrial Average in 2017.png\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
