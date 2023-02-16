import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

model = pickle.load(open('./pickles/model.pkl', 'rb'))
cv = pickle.load(open('./pickles/cv.pkl', 'rb'))

# cors
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# routes
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict")
async def get_data(news: str):
    print(news)
    data = cv.transform([news]).toarray()
    return model.predict(data)[-1]

# true: National Federation of Independent Business
# fake: CA Exams 2021: Supreme Court asks ICAI to extend opt-out option for July exams, final order tomorrow
#python -m uvicorn server:app --reload