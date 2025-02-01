# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 08:03:59 2024

@author: DELL
"""

import tensorflow as tf
import numpy as np

# Datos de entrenamiento
x_train = np.array([1, 2, 3, 4])
y_train = np.array([0, -1, -2, -3])

# Definir el modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilar el modelo
model.compile(optimizer='sgd', loss='mean_squared_error')

# Entrenar el modelo
model.fit(x_train, y_train, epochs=100)

# Hacer predicciones
print(model.predict([5]))