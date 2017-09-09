import string
import numpy as np
import random
class Caesar(object):
	def __init__(self,key):
		self.l=list(string.ascii_lowercase)
		self.key=key
		self.d={j:i for i,j in enumerate(self.l)}
	def encrypt(self,plaintext):
		n=np.array(list(plaintext))
		n1=np.array([self.d[i] for i in n])
		n1=(n1+self.key)%26
		n2=np.array([self.l[i] for i in n1])
		return ''.join(n2)
	def decrypt(self,ciphertext):
		n=np.array(list(ciphertext))
		n1=np.array([self.d[i] for i in n])
		n1=(n1-self.key)%26
		n2=np.array([self.l[i] for i in n1])
		return ''.join(n2)
	def load_data(self):
		li=(self.l)*50
		random.shuffle(li)
		X=np.array(list(map(self.encrypt,li)))
		X=np.array([self.d[i] for i in X])
		X=X.reshape(len(X),1)
		Y=np.array([self.d[i] for i in li])
		return X,Y

if __name__ == '__main__':
	c=Caesar(random.randint(0,2))
	print(c.load_data())

