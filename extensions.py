name = input("file name?")
name = name.strip().lower()
part = name.rsplit(".", 1)
media_types ={
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "txt": "text/plain",
    "pdf": "application/pdf",
    "zip": "application/zip"
}
if len(part) == 2:
    extension = part[-1]
    print(media_types.get(extension, "application/octet-stream"))
else:
    print("application/octet-stream")


