from sklearn.neighbors import KNeighborsClassifier
x1=[7,7,3,1]  #input_column
y1=[7,4,4,4]  #input_column
target=['bad','bad','good','good']  #output_column
print(x1)
print(y1)
#zip
features=list(zip(x1,y1))
print(features)
#model creation
knn=KNeighborsClassifier(n_neighbors=3) #k=3
knn.fit(features,target)  #training model
print(knn.predict([[3,7]]))