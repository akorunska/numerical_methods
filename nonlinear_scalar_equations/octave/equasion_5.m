function y = f(x)
  y = e.^(sqrt(abs(x))) - (cos(x)).^2 + x.^3 - sqrt(1 + cos(x))
endfunction

value1 = fzero(@f, -1.6)
value2 = fzero(@f, -0.6)
value3 = fzero(@f, 0.5)

disp(value1)
disp(value2) 
disp(value3)

x = -2:0.1:2;
plot(x, f(x));
axis([-2, 2, -2, 2]);
