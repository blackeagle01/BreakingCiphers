from caesar import Caesar
from sklearn.cross_validation import train_test_split
from keras.models import Sequential,load_model
from keras.layers import Dense
from keras.utils import to_categorical
import os
#Preprocess the data

x,y=Caesar().load_data()
X_train,X_test,Y_train,Y_test=train_test_split(x,y)
X_train=to_categorical(X_train,26)
X_test=to_categorical(X_test,26)
Y_train=to_categorical(Y_train,26)
Y_test=to_categorical(Y_test,26)

#Create a NN

model=Sequential()
model.add(Dense(50,activation='relu',input_dim=26))
model.add(Dense(50,activation='relu'))
model.add(Dense(26,activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#Training
if os.path.exists('mymodel.h5'):
	model=load_model('mymodel.h5')
	print(model.evaluate(X_test,Y_test)[1]*100)

else:
	model.fit(X_train,Y_train,epochs=300)
	model.save('mymodel.h5')
	print(model.evaluate(X_test,Y_test))


