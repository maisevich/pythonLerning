import summ
import view
import mult
import segmet
import subtract

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()

    summ.init(value_a, value_b)
    mult.init(value_a, value_b)
    segmet.init(value_a, value_b)
    subtract.init(value_a, value_b)

    result_sum = summ.sum()
    result_mult = mult.mult()
    result_segmet = segmet.segmet()
    result_subtract = subtract.subtract()

    view.view_data(result_mult)
    view.view_data(result_sum)
    view.view_data(result_segmet)
    view.view_data(result_subtract)
