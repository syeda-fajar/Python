from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
countid=0

class NoteModel(BaseModel):
     title:str
     content:str
   
     
app= FastAPI()
Notes=[]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/notes")
async def getNote():
          return Notes
        

@app.post("/notes")
async def addNote(notes:NoteModel):
     global countid
     new_notes = notes.model_dump()
     new_notes["id"]=countid
     Notes.append(new_notes)
     countid=countid+1
     return {"message": "Added!"}

@app.delete("/notes/{notes_id}")
async def DeleteNotes(notes_id:int):
      for item in Notes:
            if item["id"]==notes_id:
                  Notes.remove(item)
                  return {"message": "Deleted"}
      raise HTTPException(status_code=404, detail="Item not found")
@app.put("/notes/{notes_id}")
async def UpdateNote(notes_id:int,notes:NoteModel):
      updated_data = notes.model_dump()
      for item in Notes:
            if item["id"]==notes_id:
                  item["id"]=notes_id
                  item.update(updated_data)
                  return {"message": "Updated", "note": item}
      raise HTTPException(status_code=404, detail="Item not found")

      

      
      

     
     