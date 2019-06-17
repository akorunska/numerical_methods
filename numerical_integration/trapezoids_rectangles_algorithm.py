from Integral import Integral
from prettytable import PrettyTable


def trapezoids_rectangles_algorithm(integral, epsilon=(10**-9)):
    it_H_list = []
    ir_H_list = []
    it_h_list = []
    rt_h_list = []

    n = 1
    H = integral.b - integral.a
    it_H_list.append(H / 2 * (integral.sum_of_border_values()))

    while True:
        h = H / 2
        x = list()
        x.append(integral.a + h)
        for i in range(1, n):
            x.append(x[-1] + H)
        y = [integral.f(x[i]) for i in range(0, n)]
        ir_H_list.append(H * sum(y))
        it_h_list.append(0.5 * (ir_H_list[-1] + it_H_list[-1]))
        rt_h_list.append(1 / 3 * (it_h_list[-1] - it_H_list[-1]))
        if abs(rt_h_list[-1]) > epsilon:
            n *= 2
            H = h
            it_H_list.append(it_h_list[-1])
        else:
            break

    result = it_h_list[-1] + rt_h_list[-1]

    return (
        it_H_list,
        ir_H_list,
        it_h_list,
        rt_h_list,
        result,
    )


if __name__=="__main__":
    it_H_list, ir_H_list, it_h_list, rt_h_list, result, = trapezoids_rectangles_algorithm(Integral())
    t = PrettyTable(['n', 'I_T(H)', 'I_П(H)', 'I_T(h)', 'R_T(h)'])
    for i in range(len(it_H_list)):
        t.add_row([i + 1, it_H_list[i], ir_H_list[i], it_h_list[i], rt_h_list[i]])
    print(t)
    print("I = ", result)

