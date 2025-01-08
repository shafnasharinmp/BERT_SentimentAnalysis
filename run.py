from train import train
from evaluate import evaluate
from predict import predict_sentiment

def main():
    train()
    evaluate()

    text = "This movie was amazing!" # Give user input
    sentiment = predict_sentiment(text)
    print(f"The sentiment is: {sentiment}")

if __name__ == "__main__":
    main()
