import numpy as np
import dearpygui.dearpygui as dpg
import eval_change as eval_change

    
def create_window():
    w_width = 300
    w_height = 0 
    std_xy = 'x**2'

    __unit_to_multiplier = {
        22: 0.1,  # step
        23: 0,  # start
        24: 1,  # end
        25: 'x**2', # function
        26: 'x' # name variable
    }

    def _counter():
        global counter
        try:
            counter += 1
        except Exception as e:
            print(e)
            counter = 0          
        return counter

    def _var(sender, app_data, user_data):
        print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")  #DEBUG
        try:
            __unit_to_multiplier[sender] = app_data
        except Exception as e:
            print(e)
                 
    def start_button():
        c, a, b, func_str, var = __unit_to_multiplier.values()
        x_var = np.arange(a, b, c)
        y_var = []       
        for var in x_var:
            func = eval_change.eval_found(func_str, var)
            y_var.append(func)
               
        with dpg.window(label=f"Graphic {_counter()}", width=600, height=600, pos=[w_width,0]):
            with dpg.plot(label=f"Step: {c} First x: {round(a, 2)} Last x: {round(b, 2)}\n Function: {func_str}", height=-1, width=-1):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                with dpg.plot_axis(dpg.mvYAxis, label="y"):
                    dpg.add_line_series(x_var, y_var, label=f"{__unit_to_multiplier[25]}")

    
    dpg.create_context()
    dpg.create_viewport(title='Creating Graphic', width=900, height=700)

    
    with dpg.window(label="Setting Window", width=w_width, height=w_height):         
        dpg.add_input_float(label="step", callback=_var, format="%.06f", default_value=0.01)
        dpg.add_input_float(label="start", callback=_var, format="%.06f", default_value=0)
        dpg.add_input_float(label="end", callback=_var, format="%.06f", default_value=1)
        dpg.add_input_text(label="y=f(x)", default_value=std_xy, callback=_var)        
        
        dpg.add_button(label="START", callback=start_button)
          
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()





create_window()