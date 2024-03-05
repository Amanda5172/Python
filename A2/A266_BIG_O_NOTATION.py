from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import math

#constant
x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]
plot(x, y, 'r')
xlabel('Inputs')
ylabel('Steps')
title('Constant Complexity')
show()

#linear
x = [2, 4, 6, 8, 10, 12]
y = [2, 4, 6, 8, 10, 12]
plot(x, y, 'b')
xlabel('Inputs')
ylabel('Steps')
title('Linear Complexity')
show()

#logarithmic
x = [2, 4, 6, 8, 10, 12]
y = [math.log(2), math.log(4), math.log(6), math.log(8), math.log(10), math.log(12)]
plot(x, y, 'b')
xlabel('Inputs')
ylabel('Steps')
title('Logarithmic Complexity')
show()

#quadratic
x = [2, 4, 6, 8, 10, 12]
y = [4, 16, 36, 64, 100, 144]
plot(x, y, 'b')
xlabel('Inputs')
ylabel('Steps')
title('Quadratic Complexity')
show()

#exponential
x = [2, 4, 6, 8, 10, 12]
y = [math.exp(2), math.exp(4), math.exp(6), math.exp(8), math.exp(10), math.exp(12)]
plot(x, y, 'b')
xlabel('Inputs')
ylabel('Steps')
title('Exponential Complexity')
show()
#?
#factorial
