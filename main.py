import os #buat folder
import sys #panggil pdf
import warnings
from pdfreader import SimplePDFViewer

# mengecek adanya direktori
if len(sys.argv)<2:
    print('Usage: python main.py <pdf_file>')
    sys.exit(1)

# get pdf filename from command 
pdf_file_name = sys.argv[1]

# Membuat direktori jika belum ada
if not os.path.exists('hasil'):
    os.makedirs('hasil')

# Membaca file pdf dgn mode baca biner
with open(pdf_file_name, "rb") as pdf_file:
    # create SimplePDFViewer obj
    pdf_viewer = SimplePDFViewer(pdf_file)
    # Filtering warning data binary
    warnings.filterwarnings("ignore", category=Warning)

    # melakukan iterasi (looping) tiap halaman pada dokumen pdf
    for idx, canvas in enumerate(pdf_viewer):
        # mendapatkan teks dari halaman saat ini
        page_text = "".join(canvas.strings)

        #menentukan nama file hasil
        output_name = f"hasil/{os.path.splitext(os.path.basename(pdf_file_name))[0]}-page{idx}.txt"

        #Menentukan teks hasil ekstraksi ke dalam file teks
        with open(output_name,'w') as txt_file:
            txt_file.write(page_text)
            