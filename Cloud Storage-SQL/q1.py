from google.cloud import storage
import os


fldr1 = 'folder1'
fldr2= 'blopplocal'

os.mkdir(fldr2)



sclient = storage.Client()
sbucket = sclient.get_bucket("blopp")
blobs = sbucket.list_blobs()
for b in blobs:
    fldr = fldr2 + '/'
    if b.name.startswith(fld1) and b.name[-1] != '/':
        flder_strct = b.name.split('/')
        for folder in flder_strct[:-1]:
            fldr += folder + '/'
            try:
                os.mkdir(fldr)
            except Exception as e:
                pass
            
        b.download_to_filename(fldr + flder_strct[-1])

print('Bucket "blopp" has been replicated!')