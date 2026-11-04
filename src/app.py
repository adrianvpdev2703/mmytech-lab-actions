"""
Modulo de utilidades para validacion de configuraciones y entornos.
"""

def check_host_status(host: str) -> dict:
    """
    Verifica de manera basica la validez de un hostname o IP.
    """
    if not host or not isinstance(host, str):
        raise ValueError("El host proporcionado no es valido")

    clean_host = host.strip()
    return {
        "host": clean_host,
        "is_valid": len(clean_host) > 0,
        "status": "active"
    }


def calculate_allocated_resources(cores: int, ram_gb: int) -> dict:
    """
    Calcula la asignacion de recursos para provisionamiento.
    """
    if cores <= 0 or ram_gb <= 0:
        raise ValueError("Los cores y la memoria RAM deben ser mayores a cero")

    return {
        "cores": cores,
        "ram_gb": ram_gb,
        "ready_to_deploy": True
    }
