# -*- coding: utf-8 -*-
import random
K = 2

def emission(x, z, mu):
	return mu[z][x]

def forward(X, A, pi, mu):
	l = len(X)
	# X = x1 ~ xn
	alpha = [[pi[k] * emission(X[0], k, mu) for k in range(K)]]
	# loop n times
	for x in X[1:]:
		alpha.append(
			# -1 は最後に追加した要素
			[emission(x, j, mu) *
			sum(A[i][j] * alpha[-1][i] 
			for i in range(K))
			for j in range(K)])
	return alpha

def backward(X, A, mu):
	l = len(X)
	beta = [[1] * K]
	for x in reversed(X[1:]):
		beta.insert(0,
			[sum(beta[0][i] * emission(x, i, mu) * A[j][i]
				for i in range(K))
				for j in range(K)])
	return beta

def likelyhood(X, A, pi, mu):
	alpha = forward(X, A, pi, mu)
	return sum(alpha[-1]) # 最後に追加したZ_nの要素を合計

def forward_backward(X, A, pi, mu):
	alpha = forward(X, A, pi, mu)
	beta = backward(X, A, mu)
	L = sum(alpha[-1])

	gamma = [[alpha[i][j] * beta[i][j] / L 
		for j in range(K)]
		for i in range(len(X))]

	xi = [[[alpha[i][j] * emission(X[i+1], h, mu) * A[j][h] * beta[i+1][h] / L
		for h in range(K)]
		for j in range(K)]
		for i in range(len(X)-1)]

	return gamma, xi, L

def init(d):
	p = [random.random() for i in range(d)]
	return normalize(p)

def normalize(p):
	d = len(p)
	s = sum(p)
	if s != 0.0:
		result = [p[i] / s for i in range(d)]
	else:
		result = [1.0 / d] * d
	return result

def display_param(A, pi, mu):
	print "A:", A
	print "pi:", pi
	print "mu:", mu

def em_algorithm(X):
	# init
	pi = init(K) #pi[i] = p(z_0=i)
	A = [init(K) for k in range(K)] # A[i][j] = p(z_n=j|z_{n-1}=i)
	D = 3 # number of observed data
	mu = [init(D) for k in range(K)]
	N = len(X)
	print "X:", X
	display_param(A, pi, mu)

	# loop
	for loop in range(10):
		# E-step
		(gamma, xi, L) = forward_backward(X, A, pi, mu)

		# M-step
		pi = normalize([gamma[0][k] for k in range(k)])
		A = [normalize([sum([xi[n][j][k] for n in range(N-1)])
			for j in range(K)])
			for k in range(K)]
		mu = [normalize([sum([gamma[n][k] for n in range(N) if X[n] == i])
			for i in range(D)])
			for k in range(K)]
		print "likelyhood:", L

	print "likelyhood:", likelyhood(X, A, pi, mu)
	display_param(A, pi, mu)

if __name__ == '__main__':
	X = [0, 2, 0, 1, 0, 2]
	em_algorithm(X)




