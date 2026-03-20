import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auth import validar_contrasena

# Test 1
def test_contrasena_valida():
# Arrange
    contrasena = "Segura1!"
# Act
    resultado = validar_contrasena(contrasena)
# Assert
    assert resultado == True
# Test 2
def test_sin_mayuscula():
    assert validar_contrasena("segura1!") == False 

# Test 3
def test_sin_numero():
    assert validar_contrasena("Seguridad!") == False
# Test 4
def test_exactamente_8_caracteres():
    assert validar_contrasena("Segur1!a") == True
# Test 5
def test_con_espacio():
    assert validar_contrasena("Segura 1!") == False