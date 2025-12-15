# Comparación: Programación Tradicional vs. POO en Python

Este repositorio contiene dos soluciones para el mismo problema: calcular el promedio semanal del clima.

## 1. Programación Tradicional (Estructurada)
**Archivo:** `Clima_tradicional.py`
* **Enfoque:** Se basa en **funciones** separadas.
* **Lógica:** Los datos (lista de temperaturas) viajan de una función a otra. La estructura es lineal: Entrada -> Proceso -> Salida.

## 2. Programación Orientada a Objetos (POO)
**Archivo:** `clima_poo.py`
* **Enfoque:** Se basa en **Clases y Objetos**.
* **Lógica:** Creamos la clase `ClimaSemanal` que contiene tanto los datos (atributos) como las funciones (métodos) en un solo lugar.
* **Encapsulamiento:** Usamos `__temperaturas` (privado) para proteger los datos.

## Conclusión
La POO permite organizar mejor el código y proteger la información, haciéndolo más escalable que la programación tradicional.
