from fastapi import APIRouter ,APIRouter,UploadFile,File 
from fastapi.responses import FileResponse , JSONResponse, RedirectResponse
from os import getcwd , remove


router = APIRouter()

@router.get("/")
async def main():
    return FileResponse("templates/inicio.html")

@router.get("/mapa")
async def mapa_root():
    return FileResponse("templates/mapa.html")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
      with open (getcwd()+ "/"+ file.filename,"wb") as myfile:
           content =await file.read()
           myfile.write(content)
           print(myfile.name)
           myfile.close()
      return RedirectResponse(url="/mapa", status_code=status.HTTP_302_FOUND)
@router.get("/file/{name_file}")
def get_file(name_file :str):
     return FileResponse(getcwd() + "/"+ name_file)


@router.get("/download/{name_file}")
def download_file(name_file :str):
     return FileResponse(getcwd() + "/"+ name_file, media_type= "application/octet-stream",filename=name_file)
     
@router.delete("/delete/{name_file}")
def delete_file(name_file : str):
    try:
         remove(getcwd() + "/" + name_file)
         return JSONResponse( content={
               "removed":True
               },status_code=200)       
    except FileNotFoundError:
          return JSONResponse( content={
               "removed":False,
               "message":"file not found"
               },status_code=404)
    
    

    