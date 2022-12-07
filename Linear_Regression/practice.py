import matplotlib.pyplot as plt
x = [0,2,4,6,8,10,12,14,16,18]
s_exp = [20*2**n for n in range(len(x))]
s_square = [20*n**2 for n in range(len(x))]
s_linear = [20*n for n in range(len(x))]
plt.scatter(x,[1]*len(x),s=s_exp, label='$s=2^n$', lw=1)
plt.scatter(x,[0]*len(x),s=s_square, label='$s=n^2$')
plt.scatter(x,[-1]*len(x),s=s_linear, label='$s=n$')
plt.ylim(-1.5,1.5)
plt.legend(loc='center left', bbox_to_anchor=(1.1, 0.5), labelspacing=3)
plt.show()