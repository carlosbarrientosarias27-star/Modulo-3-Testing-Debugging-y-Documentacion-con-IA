def validar_contrasena(contrasena):
    """
    Valida que una contraseña cumpla los requisitos de seguridad.
    Reglas:
    - Longitud entre 8 y 20 caracteres
    - Al menos una letra mayúscula
    - Al menos un número
    - Al menos un carácter especial: !@#$%^&*()
    - Sin espacios en blanco
    Devuelve True si es válida, False si no lo es.
    """
    import re
    if not (8 <= len(contrasena) <= 20):
        return False
    if not re.search(r'[A-Z]', contrasena):
        return False
    if not re.search(r'[0-9]', contrasena):
        return False
    if not re.search(r'[!@#$%^&*()]', contrasena):
        return False
    if ' ' in contrasena:
        return False
    return True