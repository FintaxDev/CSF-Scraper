import CreateFile
import ReadFile
import ReadQR
import RequestURL

# Ubicacion de la Constancia de Situacion Fiscal
CSF_path = "Constancia de Situacion Fiscal.pdf"

# Ubicacion en donde se guardaran los archivos
Json_path = "data.json"
Excel_path = "data.xlsx"

# Leer el codigo QR
strUrl = ReadQR.URL(CSF_path)

# Consultar el validador QR en la pagina web del SAT
dicRequest = RequestURL.SIAT(strUrl)

# Crear archivo JSON
CreateFile.Json(dicRequest, Json_path)

# Leer archivo JSON
dictJSON = ReadFile.Json(Json_path)
for table in dictJSON.keys():
    print(f"\n===================={table}====================")
    for key, value in dictJSON[table].items():
        print(key, value)

# Crear archivo de Excel con los datos presentados en forma horizontal
CreateFile.Excel(dicRequest, "H" + Excel_path, "horizontal")

# Crear archivo de Excel con los datos presentados en forma vertical
CreateFile.Excel(dicRequest, "V" + Excel_path, "vertical")
