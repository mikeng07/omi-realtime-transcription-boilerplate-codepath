from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.post("/webhook")
def webhook(uid: str, transcript: dict):
    

    # Hint: The transcript contains segments with text data
    # Hint: Access the latest segment with transcript["segments"][-1]["text"]
    # Hint: Return a dictionary with a "message" key and the value being the notification message

    # Task: Implement keyword detection and response logic of your choice
    # example: if the word "tired" is mentioned, return a message notifying the user to take a break

    # TODO: Write your code below this line
    # if any ("cookie" in segment["text"] for segment in transcript["segments"]):
    #     return {"message": "cookie found"}
    # return {"message": "no cookie found"}

    # print(transcript)
    # return {"message" : "testing for webhook"}


    for segment in transcript["segments"]:
        print (segment["text"])
        if "tired" in segment["text"].lower():
            print("tired found")
            return {"message" : "take a break"}
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
