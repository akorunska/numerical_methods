clear
output_precision(9)

function y = f(x)
  y = x.^2 * cos(x) * sin(x) + pi - x
endfunction

value1 = fzero(@f, -9.2)
value2 = fzero(@f, -7.6)
value3 = fzero(@f, -6.6)
value4 = fzero(@f, -4.3)
value5 = fzero(@f, -3.8)
value6 = fzero(@f, 2)
value7 = fzero(@f, 3)
value8 = fzero(@f, 4.6)
value9 = fzero(@f, 6.2)
value10 = fzero(@f, 7.7)
value11 = fzero(@f, 9.4)

disp(value1)
disp(value2) 
disp(value3)
disp(value4)
disp(value5)
disp(value6)
disp(value7) 
disp(value8)
disp(value9)
disp(value10)
disp(value11)