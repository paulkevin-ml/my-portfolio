import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "hours": [1,2,3,4,5,6,7,8,9,10],
    "score": [50,55,60,63,68,74,78,84,90,95]
}
df = pd.DataFrame(data)
print(df)

x = df[["hours"]]
y = df[["score"]]

model = LinearRegression()
model.fit(x,y)

prediction = model.predict([[7]])
print("Predicted score for 7 hours:", prediction)
print("Slope(score per hour):", model.coef_)
print("Intercept(baseline score):", model.intercept_) 
