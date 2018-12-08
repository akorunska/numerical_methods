clear

function y = f(x)
  y = e.^(sqrt(abs(x))) - (cos(x)).^2 + x.^3 - sqrt(1 + cos(x))
endfunction

x = -2:0.1:2;
plot(x, f(x));
axis([-2, 2, -2, 2]);