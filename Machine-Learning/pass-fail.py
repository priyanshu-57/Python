#pass/ fail predictor

#data
import pandas as pd

data= {
    "Hours": [1,2,3,4,5,6],
    "Marks": [30,40,50,60,70,80]
}

df= pd.DataFrame(data)

# print(df)

X=df[["Hours"]]   #features
y= df["Marks"]  #target

#train model
from sklearn.linear_model import LinearRegression

model= LinearRegression()
model.fit(X,y)

prediction= model.predict(pd.DataFrame({"Hours":[7]}))
print("Predicted mark", prediction)