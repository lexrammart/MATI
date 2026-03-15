import urllib.request
import json
import ssl


ACTUAL_VERSION = "1.1.7"

def check_update():
    """
    Consulta la API pública de GitHub para verificar si hay un nuevo Release.
    Retorna una tupla (True, dict_datos) si hay actualización, o None si estás al día.
    """
    url = "https://api.github.com/repos/lexrammart/MATI-Releases/releases/latest"

    try:
<<<<<<< HEAD
        # 1. EL PARCHE SSL: Creamos un contexto que ignora la verificación del certificado
=======
        # 1. PARCHE SSL
>>>>>>> fix/ssl-cert-updater
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

<<<<<<< HEAD
        # Hacemos la petición (simulando ser un navegador básico para que GitHub no nos bloquee)
        req = urllib.request.Request(url, headers={"User-Agent": "MATI-Updater"})

        # Le pasamos el contexto SSL modificado a la petición
        with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
            data = json.loads(response.read().decode())

        # GitHub guarda la versión en "tag_name" (ej. "v1.1.5")
        latest_version_tag = data.get("tag_name", "")

        # Le quitamos la 'v' y espacios fantasma
        latest_version = latest_version_tag.replace("v", "").strip()

        # 2. EL PARCHE MATEMÁTICO: Convertimos "1.1.5" a (1, 1, 5) para comparar exacto
        version_github = tuple(map(int, latest_version.split(".")))
        version_local = tuple(map(int, ACTUAL_VERSION.split(".")))
=======
        req = urllib.request.Request(url, headers={"User-Agent": "MATI-Updater"})

        with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
            data = json.loads(response.read().decode())

        latest_version_tag = data.get("tag_name", "")

        # CHISMOSAFE: Imprimimos qué diablos nos mandó GitHub
        print(f"[*] INFO: GitHub dice que la última versión es: '{latest_version_tag}'")

        latest_version = latest_version_tag.replace("v", "").strip(" .")
        if not latest_version:
            print("Advertencia: El tag llegó completamente vacío.")
            return None

        # 2. PARCHE MATEMÁTICO CON BLINDAJE EXTRA
        try:
            version_github = tuple(map(int, latest_version.split(".")))
            version_local = tuple(map(int, ACTUAL_VERSION.split(".")))
        except ValueError:
            print(
                f"Error matemático: El tag '{latest_version_tag}' tiene un formato que no se puede comparar."
            )
            return None
>>>>>>> fix/ssl-cert-updater

        changelog = data.get("body", "Mejoras de rendimiento y telemetría.")

<<<<<<< HEAD
        # Si la versión de GitHub es mayor a la tuya, disparamos la alerta
=======
>>>>>>> fix/ssl-cert-updater
        if version_github > version_local:
            datos_reales = {"version": latest_version, "changelog": changelog}
            return (True, datos_reales)

    except Exception as e:
        print(f"Error al conectar con GitHub para buscar actualizaciones: {e}")

    return None
