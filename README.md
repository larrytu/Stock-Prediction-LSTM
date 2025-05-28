### Stock Market Prediction

**Author: Larry Tu**

## Table of Contents
1. [Executive Summary](#Executive-Summary)
2. [Rationale](#Rationale)
3. [Research Question](#research-question)
4. [Data Sources](#data-sources)
5. [Methodology](#methodology)
6. [Results](#results)
7. [Next Steps](#next-steps)
---

## Executive Summary
The purpose of this project is to utilize ML models to be able to create stock price predictions for Nvidia. As many people know, stocks are highly volatile which makes accurate predictions incredibly difficult. A person's tweet can send a stock soaring or tumbling down within hours with no warning. An ideal model would be one that studies people's sentiments from all social media platforms to see what people are talking about on the current stock, with higher importance to those with more influence. In this project, it will be a more simple model, which only analyzes historical data to make predictions. In this project, I will be engineering new features, filling in missing data and utilizing different machine learning models to make accurate predictions. This project is for potential traders to become more educated in the stock market.

## Rationale
People should care about this question due to the importance of stocks in a person's wealth.

## Research Question
Which set of indicators (ex: daily highs, lows, macd, rsi, etc) most accurately predicts short-term stock price movements, and how does each indicator contribute to the predictive power of a machine learning model?

## Data Sources
https://www.kaggle.com/datasets/footballjoe789/us-stock-dataset

## Methodology
LSTM - Long Short Term Memory

XGboost

ARIMA (Autoregressive integrated moving average)

Random Forest

These are the techniques I plan to use for this project. Each one of these models are efficient in making predictions in time-series data. Each has their own strengths and downsides which will be explored at a later date.
I also created new features such as the interactions between each feature like RSI and Stochastic, Bollinger Bonds, creating a volume to price ratio, etc.

## Results

Random Forest

| Metric      | Train   | Test     |
|-------------|---------|----------|
| MSE         | 5.3829  | 13.4837  |
| RMSE        | 0.5837  | 8.3847   |
| R-squared   | 0.9482  | 0.9073   |
| MAE         | 0.7817  | 7.3829   |

LSTM

| Metric      | Train   | Test     |
|-------------|---------|----------|
| MSE         | 0.0048  | 69.9454  |
| RMSE        | 0.0690  | 8.7434   |
| R-squared   | 0.8961  | 0.9495   |
| MAE         | 0.0664  | 7.6175   |

ARIMA

| Metric    | Value        |
|-----------|--------------|
| MSE       | 42.846901354936165 |
| MAE       | 4.165435312236351  |
| RMSE      | 6.545754452691925  |
| MAPE      | 0.09387029171674306|
| R²        | 0.9690770130157705 |


From the tables shown above, each model shows good results compared to the baseline model which was the Random Forest model. The LSTM model had an R-Squared of 0.896 on the train and 0.949 on the test, followed by an R-Squared of 0.96 with the ARIMA model. With the ARIMA model, I had used the XGBoost model to choose the ideal features to get a more accurate prediction. I then used the autoARIMA to get the ideal order when fitting the ARIMA model. The ideal order was 0,1,5 which produced the above results. In the charts for the LSTM model, we see that the predicted prices are similar with the original stock price. Also looking at the distribution, we see its a little skewed to the right which can be the result of some outliers. Looking at the QQ plot, its mostly normal except at the ends are a little skewed.

For the ARIMA model, I tested for stationarity, which means that the mean and standard deviation continues to increase over time and doesn't stay at the same spot. I also created a residuals vs fitted values to see how the model is, which showed  that it was dense in the beginning but it becomes a little more spread out as the fitted values get larger. This means that some values are small outliers. 




## Next steps
My next steps will be to continue working on the different models to maybe analyze sentiments from social media to see how it affects stock prices.




