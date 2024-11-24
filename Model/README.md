﻿# Project README
Project: Weather Forecasting Model using Neural Networks (Project 1)
Author: Austyn Griego
Course: CS3210 - Machine Learning
Date: November 23rd, 2024
Description: The following code serves to create and train a Machine learning Neural Network model to predict weather data (more specifically
TMAX: High Temp, TMIN: Low Temp, PRCP: percipitation(in), SNOW: snowfall, AWND: Average windspeed. The model is trained on historical weather 
data fetched from the NOAA API. The model is trained to predict weather based on variables: TMAX, TMIN, PRCP, SNOW, and AWND. The model is 
evaluated using the mean absolute error (MAE) metric. The code also includes feature engineering steps such as feature interactions, handling 
missing values, log transformation, and outlier removal. The code also includes cross-validation to evaluate the model's performance on unseen 
data. The code was written in Python using the TensorFlow and Keras libraries. Next steps for my project include pickling the model and creating
a web application to make weather predictions (ultimatelty in the form of a forecast) based on users inputed area code.
Expected Output: (Does not include whole terminal)


           TMAX       TMIN      PRCP      SNOW      AWND
0   30.649105  21.798904  0.056685  0.374776  1.989867
1   30.886742  13.839097 -0.002862 -0.023608  1.636345
2   33.025394  17.816542  0.003772 -0.006042  1.986617
3   58.480766  33.398182  0.022621  0.007936  2.137068
4   33.944649  10.508843  0.035643  0.111181  2.472005
5   43.997738  31.708420  0.062956  0.014387  1.434307
6   39.569668  17.923689  0.001376  0.040324  2.879066
7   46.394253  18.552187  0.004391  0.108923  2.859167
8   50.161633  32.412430 -0.007998  0.014864  1.993458
9   37.838444  18.793606  0.048525  0.021543  1.640200
10  54.828003  31.089054 -0.011720 -0.022754  2.230787
11  30.883478  11.623567  0.013028  0.009561  2.138787
TMAX - Cross-validated MAE scores: [5.217477321624756, 4.962740898132324, 7.67523193359375, 4.241466045379639, 6.864092826843262]
TMAX - Mean MAE: 5.792201805114746, Std MAE: 1.2741936942143461
TMIN - Cross-validated MAE scores: [2.5119829177856445, 3.4668445587158203, 5.723386287689209, 2.7941524982452393, 3.3494675159454346]
TMIN - Mean MAE: 3.5691667556762696, Std MAE: 1.1329328441133384
PRCP - Cross-validated MAE scores: [0.0175316259264946, 0.0360301248729229, 0.025606459006667137, 0.03322714567184448, 0.012624627910554409]
PRCP - Mean MAE: 0.025003996677696705, Std MAE: 0.008929095574935493
SNOW - Cross-validated MAE scores: [0.05248164013028145, 0.06008616089820862, 0.32279443740844727, 0.06556811928749084, 0.09559101611375809]
SNOW - Mean MAE: 0.11930427476763725, Std MAE: 0.10279123390978992
AWND - Cross-validated MAE scores: [0.2580391764640808, 0.33852994441986084, 0.513201892375946, 0.32479649782180786, 0.2868109345436096]
AWND - Mean MAE: 0.344275689125061, Std MAE: 0.08909259088817569
TMAX - Loss: 55.7394905090332, MAE: 5.908624649047852
TMIN - Loss: 17.14907455444336, MAE: 2.7959482669830322
PRCP - Loss: 0.0005450723692774773, MAE: 0.016687707975506783
SNOW - Loss: 0.010554363019764423, MAE: 0.05877925083041191
AWND - Loss: 0.1375368982553482, MAE: 0.28712281584739685
Evaluation results: {'TMAX': {'loss': 55.7394905090332, 'mae': 5.908624649047852}, 'TMIN': {'loss': 17.14907455444336, 'mae': 2.7959482669830322}, 'PRCP': {'loss': 0.0005450723692774773, 'mae': 0.016687707975506783}, 'SNOW': {'loss': 0.010554363019764423, 'mae': 0.05877925083041191}, 'AWND': {'loss': 0.1375368982553482, 'mae': 0.28712281584739685}}
