def Json(request:dict, filename:str)->None:
    import json
    with open(filename, "w") as outfile:
        json.dump(request, outfile, indent=4, ensure_ascii=False)

def Excel(request:dict, filename:str, orientation="horizontal")->None:
    import xlsxwriter
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    if orientation == "horizontal":
        j=0
        for table in request.keys():
            for key, value in request[table].items():
                worksheet.write(0, j, key.replace(":", ""))
                worksheet.write(1, j, value)
                j+=1

    if orientation == "vertical":
        i=0
        for table in request.keys():
            for key, value in request[table].items():
                worksheet.write(i, 0, key.replace(":", ""))
                worksheet.write(i, 1, value)
                i+=1

    workbook.close()
