clear
output_precision(8)

function y = f(x)
  y = e.^(sqrt(abs(x))) - (cos(x)).^2 + x.^3 - sqrt(1 + cos(x))
endfunction

value1 = fzero(@f, -1.2)
value2 = fzero(@f, -0.7)
value3 = fzero(@f, 0.5)

disp(value1)
disp(value2)
disp(value3)