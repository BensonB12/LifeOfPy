from fastapi import FastAPI

app = FastAPI()

my_decorator = app.get("/")

def gcd(x,y):
    if(y == 0):
        return abs(x)
    else:
        return gcd(y, x % y)

@app.get("/{a}/{b}/")
def root(a: int, b: int):
    return {"answer": gcd(a,b)}