# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:26:10 2024

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import  Button, Slider

#==============================================================================#

def Izhikevich_Model(_I = 10, a = 0.02, b = 0.2, c = -65, d = 8):
    ######### Constantes
    spike_value = 35#Valor maximo de picos(Spike)
    ######### Configuración experimental
    # Tiempo
    T = 1000 # longitud de la simulación [ms]
    dt = 0.5 # derivada del timepo [ms]
    time =   np.arange(0, T+dt, dt)  # tamaño del paso[ms]
    # Recuperación
    u=np.zeros(len(time)) # lista de elementos de u 
    u[0]=-14
    # VOLTAGE
    V=np.zeros(len(time))     # Lista con el historial de V
    V[0]=-70# potencial inicial de v
    
    # I
    I = np.zeros(len(time))
    I[200:1500] = _I

    for t in range(1, len(time)):
        # Condición que se permite hacer calculos mientras no se alcance el potencial 
        if V[t-1] < spike_value:
            # Instrucciones para calcular el potencial de membrana
            dV = (0.04 * V[t-1] + 5) * V[t-1] + 140 - u[t-1]
            V[t] = V[t-1] + (dV + I[t-1]) * dt
            # instrucciones para la recuperación de variables
            du = a * (b * V[t-1] - u[t-1])
            u[t] = u[t-1] + dt * du
        # En otro caso, se alcazó el pico esperado.
        else:
            V[t-1] = spike_value    # asignar el valor de pico de pulso
            V[t] = c                # reiniciar el valor de la membrana
            u[t] = u[t-1] + d       # reiniciar el valor de recuperación

    return V

def I_values(_I=10, time=None):
    I = np.zeros(len(time))
    I[200:1500] = _I
    return I

#==============================================================================#

def start_IZ_sim():
    #Parametros para las gráficas
    T= 1000 
    dt = 0.5 
    time = np.arange(0, T+dt, dt) 
    I_init = 10
    a_init = 0.02
    b_init = 0.2
    c_init = -65
    d_init = 8

    V = Izhikevich_Model()
    I = I_values(time=time)

    axis_color = 'lightgoldenrodyellow'

    fig = plt.figure("Modelo de neurona Izhikevich", figsize=(12, 6))
    ax = fig.add_subplot(111)
    plt.title("Modelo interactivo de Izhikevich")
    fig.subplots_adjust(left=0.1, bottom=0.5)

    # plot lines
    line = plt.plot(time, V, label="Potencial de Membrana")[0]
    line2 = plt.plot(time, I, label="Umbral")[0]

    # add legend
    plt.legend(loc="upper right")

    # add axis labels
    plt.ylabel(" [V]/ [A]")
    plt.xlabel("Tiempo [s]")

    # define sliders (position, color, inital value, parameter, etc...)
    I_slider_axis = plt.axes([0.1, 0.40, 0.65, 0.03], facecolor=axis_color)
    I_slider = Slider(I_slider_axis, '$I_{ext}$ ', 0.1, 40, valinit=I_init)

    a_slider_axis = plt.axes([0.1, 0.35, 0.65, 0.03], facecolor=axis_color)
    a_slider = Slider(a_slider_axis, '$a$', 0.001, 0.15, valinit=a_init)

    b_slider_axis = plt.axes([0.1, 0.30, 0.65, 0.03], facecolor=axis_color)
    b_slider = Slider(b_slider_axis, '$b$', 0.001, 0.3, valinit=b_init)

    c_slider_axis = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor=axis_color)
    c_slider = Slider(c_slider_axis, '$c$', -75, -40, valinit=c_init)

    d_slider_axis = plt.axes([0.1, 0.20, 0.65, 0.03], facecolor=axis_color)
    d_slider = Slider(d_slider_axis, '$d$', 0.001, 10, valinit=d_init)

    # update functions
    def update(val):
        line.set_ydata(
            Izhikevich_Model(I_slider.val, a_slider.val, b_slider.val,
                             c_slider.val, d_slider.val))
        line2.set_ydata(I_values(I_slider.val, time=time))

    # update, if any slider is moved
    I_slider.on_changed(update)
    a_slider.on_changed(update)
    b_slider.on_changed(update)
    c_slider.on_changed(update)
    d_slider.on_changed(update)

    ########################### REGULAR SPIKING BUTTON #############################
    # Add a button for resetting the parameters
    RS_button_ax = plt.axes([0.1, 0.1, 0.15, 0.04])
    RS_button = Button(
        RS_button_ax, 'Disparos Normales', color=axis_color, hovercolor='0.975')

    # event of resert button being clicked
    def RS_button_was_clicked(event):
        #I_slider.reset()
        a_slider.reset()
        b_slider.reset()
        c_slider.reset()
        d_slider.reset()

    RS_button.on_clicked(RS_button_was_clicked)

    ########################### INTRINSICALLY BURSTING BUTTON ######################
    # Add a button for resetting the parameters
    IB_button_ax = plt.axes([0.35, 0.1, 0.15, 0.04])
    IB_button = Button(
        IB_button_ax,
        'INTRINSICALLY BURSTING',
        color=axis_color,
        hovercolor='0.975')

    # event of resert button being clicked
    def IB_button_was_clicked(event):
        #I_slider.reset()
        a_slider.reset()
        b_slider.reset()
        c_slider.set_val(-55)
        d_slider.set_val(4)

    IB_button.on_clicked(IB_button_was_clicked)

    ################################ CHATTERING BUTTON #############################
    # Add a button for resetting the parameters
    CH_button_ax = plt.axes([0.6, 0.1, 0.15, 0.04])
    CH_button = Button(
        CH_button_ax, 'CHATTERING', color=axis_color, hovercolor='0.975')

    # event of resert button being clicked
    def CH_button_was_clicked(event):
        #I_slider.reset()
        a_slider.reset()
        b_slider.reset()
        c_slider.set_val(-50)
        d_slider.set_val(2)

    CH_button.on_clicked(CH_button_was_clicked)

    ############################### FAST SPIKING BUTTON ############################
    # Add a button for resetting the parameters
    FS_button_ax = plt.axes([0.1, 0.02, 0.15, 0.04])
    FS_button = Button(
        FS_button_ax, 'Disparos Rapidos', color=axis_color, hovercolor='0.975')

    # event of resert button being clicked
    def FS_button_was_clicked(event):
        #I_slider.reset()
        a_slider.set_val(0.1)
        b_slider.reset()
        c_slider.reset()
        d_slider.reset()

    FS_button.on_clicked(FS_button_was_clicked)

    ######################### LOW-THRESHOLD SPIKING BUTTON #########################
    # Add a button for resetting the parameters
    LTS_button_ax = plt.axes([0.35, 0.02, 0.15, 0.04])
    LTS_button = Button(
        LTS_button_ax,
        'LOW-THRESHOLD SPIKING',
        color=axis_color,
        hovercolor='0.975')

    # event of resert button being clicked
    def LTS_button_was_clicked(event):
        #I_slider.reset()
        a_slider.reset()
        b_slider.set_val(0.25)
        c_slider.reset()
        d_slider.reset()

    LTS_button.on_clicked(LTS_button_was_clicked)

    ################################# RESONATOR BUTTON #############################
    # Add a button for resetting the parameters
    RZ_button_ax = plt.axes([0.6, 0.02, 0.15, 0.04])
    RZ_button_ = Button(
        RZ_button_ax, 'RESONADOR', color=axis_color, hovercolor='0.975')

    # TODO Does it work?
    # event of resert button being clicked
    def RZ_button_was_clicked(event):
        #I_slider.reset()
        a_slider.set_val(0.1)
        b_slider.set_val(0.26)
        c_slider.reset()
        d_slider.reset()

    RZ_button_.on_clicked(RZ_button_was_clicked)

    plt.show()


#==============================================================================#

if (__name__ == '__main__'):
    start_IZ_sim()