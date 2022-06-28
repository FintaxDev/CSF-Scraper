import CreateFile
import ReadFile
import ReadQR

CSF_path = "Constancia de Situacion Fiscal.pdf"

url = ReadQR.URL(CSF_path)
Json_path = "data.json"

CreateFile.Json(url, Json_path)

dictJSON = ReadFile.Json(Json_path)
for table in dictJSON.keys():
    print(f"\n============{table}====================")
    for key, value in dictJSON[table].items():
        print(key, value)
