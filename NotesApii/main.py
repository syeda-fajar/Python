from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from database import engine,get_db
from models import NoteTable,Base
from fastapi import Depends
from sqlalchemy.orm import Session



class NoteModel(BaseModel):
     title:str
     content:str
   
     
app= FastAPI()
Notes=[]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/notes")
async def getNote(db: Session = Depends(get_db)):
          all_note=db.query(NoteTable).all()
          return all_note
        

@app.post("/notes")
async def addNote(notes:NoteModel,db: Session = Depends(get_db)):
     new_note = NoteTable(title=notes.title, content=notes.content)
     db.add(new_note)
     db.commit()
     db.refresh(new_note)
     return {"message": "Added!"}

@app.delete("/notes/{notes_id}")
async def DeleteNotes(notes_id:int,db: Session = Depends(get_db)):
      item=db.query(NoteTable).filter(NoteTable.id == notes_id).first()
      if not item:
            raise HTTPException(status_code=404, detail="Item not found")
      db.delete(item)
      db.commit()
      return {"message": "Deleted"}

@app.put("/notes/{notes_id}")
async def UpdateNote(notes_id:int,notes:NoteModel,db:Session=Depends(get_db)):
       item=db.query(NoteTable).filter(NoteTable.id == notes_id).first()
       if not item:
            raise HTTPException(status_code=404, detail="Item not found")
       item.title =notes.title
       item.content=notes.content
       db.commit()
       db.refresh(item)
       return {"message": "Updated", "note": item}   

      

      
      

     
     