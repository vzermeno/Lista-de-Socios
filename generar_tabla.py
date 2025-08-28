import webbrowser
import os

# Datos de los socios
socios = [
    {
        "Estado": "No Check-In",
        "ID Contrato": "11156744",
        "ID Socio": "24979863",
        "Nombre": "Diaz Berlanga Roberto",
        "Tipo": "Owner",
        "Fecha": "9/6/2025",
        "País": "United States",
        "Membresía": "Palace Elite",
        "Beneficios": "SOCIOS ELITE SPGOLF,Free3NightsMPPC",
        "Habitación": "GVK Grand Deluxe Garden View",
        "Otros Datos": "18652776, MPG, 2398615, SOCIOSG, 4095004, Exit C Exit, US, 26853, 2, 2.0, M, False, 2, Palace Elite, 5, False, False"
    },
    # Agrega más socios aquí, en el mismo formato de diccionario
    # {
    #     "Estado": "...",
    #     "ID Contrato": "...",
    #     "ID Socio": "...",
    #     "Nombre": "...",
    #     "Tipo": "...",
    #     "Fecha": "...",
    #     "País": "...",
    #     "Membresía": "...",
    #     "Beneficios": "...",
    #     "Habitación": "...",
    #     "Otros Datos": "..."
    # },
]

def generar_html(socios):
    html_content = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Socios</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding: 20px;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Lista de Socios</h1>
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
'''
    if socios:
        headers = socios[0].keys()
        for header in headers:
            html_content += f'                        <th>{header}</th>\n'
    
    html_content += '''
                    </tr>
                </thead>
                <tbody>
'''

    for socio in socios:
        html_content += "                    <tr>\n"
        for key, value in socio.items():
            html_content += f"                        <td>{value}</td>\n"
        html_content += "                    </tr>\n"

    html_content += '''
                </tbody>
            </table>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''
    return html_content

def main():
    html = generar_html(socios)
    with open("socios.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Se ha generado el archivo 'socios.html' con éxito.")
    
    # Abrir el archivo en el navegador
    # webbrowser.open('file://' + os.path.realpath('socios.html'))

if __name__ == "__main__":
    main()