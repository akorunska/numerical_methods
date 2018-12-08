clear

function y = f(x)
  y = (x.^2) .* cos(x) .* sin(x) + pi - x
endfunction

x = -10:0.1:10;
plot(x, f(x));
axis([-10, 10, -10, 10]);