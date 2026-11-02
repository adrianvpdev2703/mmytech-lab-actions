# Laboratorio: Automatización de Revisiones con GitHub Actions

Este repositorio contiene la estructura y configuración necesaria para validar automáticamente el código cada vez que se realice un `push` o se proponga un cambio mediante `Pull Request`.

---

## 📁 Estructura del Repositorio

```text
githubactions-lab/
├── .github/
│   └── workflows/
│       └── ci.yml             # Workflow de GitHub Actions con 2 jobs paralelos (Python y Ansible)
├── .ansible-lint              # Reglas de linting para Ansible
├── ansible/
│   ├── ansible.cfg            # Parametros de configuracion de Ansible
│   ├── inventory/
│   │   └── hosts.ini          # Inventario de servidores / hosts
│   ├── playbooks/
│   │   └── site.yml           # Playbook principal de automatizacion
│   └── roles/
│       └── common/
│           └── tasks/
│               └── main.yml   # Tareas modulares
├── src/
│   └── app.py                 # Script de Python con logica funcional
├── tests/
│   └── test_app.py            # Pruebas unitarias con pytest
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Descripcion y guia de uso
```

---

## ⚙️ ¿Cómo Funciona el Workflow de GitHub Actions?

El archivo [`.github/workflows/ci.yml`](.github/workflows/ci.yml) ejecuta dos tareas automáticas en paralelo:

1. **`python-checks`**:
   - Analiza el código con `flake8` para detectar errores de sintaxis, variables sin usar o fallos de formato.
   - Ejecuta las pruebas unitarias con `pytest` para verificar que el código funciona como se espera.

2. **`ansible-checks`**:
   - Ejecuta `ansible-playbook --syntax-check` contra el playbook y el inventario para garantizar que no existan errores estructurales de YAML o directivas inválidas de Ansible.
   - Ejecuta `ansible-lint` para verificar el cumplimiento de buenas prácticas de automatización.

---

## 🚀 Pruebas Locales

Si deseas probar localmente antes de subir tus cambios:

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar linter y tests de Python
flake8 src/ tests/
pytest -v tests/

# 3. Validar sintaxis de Ansible
cd ansible
ansible-playbook --syntax-check playbooks/site.yml -i inventory/hosts.ini
ansible-lint playbooks/site.yml
```
