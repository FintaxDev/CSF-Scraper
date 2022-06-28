import cv2
import fitz
import os

def URL(pdf_path:str)->str:
    pdf_file = fitz.open(pdf_path)
    page = pdf_file[0]
    for image_index, img in enumerate(page.get_images(), start=1):
        xref = img[0]
        pix = fitz.Pixmap(pdf_file, xref)
        pix.save("page-%i.png" % image_index)
        try:
            imagen = cv2.imread("page-%i.png" % image_index)
            det=cv2.QRCodeDetector()
            val, pts, st_code = det.detectAndDecode(imagen)
            if val:
                url = val
        except:
            pass
        os.remove("page-%i.png" % image_index)
    return url
