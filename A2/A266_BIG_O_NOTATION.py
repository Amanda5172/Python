from matplotlib.pyplot import ylabel, plot, show, xlabel, title
x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]
plot(x, y, 'r')
xlabel('Inputs')
ylabel('Steps')
title('Constant Complexity')
show()
