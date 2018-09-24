import numpy as np 



class LogisticRegression(object):
	def __init__(self, gama):
		super(LogisticRegression, self).__init__()
		self.gama = gama

	def fit(X, y):
		pass

	def predict():
		pass
		




if __name__ == '__main__':
	X = [[1,3,1],[2,3,4],[7,8,5],[2,1,3],[7,4,5]]
	y = [1,-1,1,-1,1]

	lr = LogisticRegression()
	lr.fit(X,y)
	result = lr.predict([4,2,1])
	print(result)