from fastapi import APIRouter, HTTPException
import logging

# Create a logger for the KI Model module
logger = logging.getLogger(__name__)

router = APIRouter()

# Simulated KI Model status
ki_model_status = {
    "model_loaded": False,
    "model_name": "ExampleKIModel"
}

@router.get("/ki-example")
def ki_example():
    """Example endpoint for the KI Model module."""
    return {"message": "This is an example of KI Model endpoint"}

@router.get("/ki-status")
def ki_status():
    """Checks if the KI Model is loaded."""
    if ki_model_status["model_loaded"]:
        return {"status": "Model loaded", "model_name": ki_model_status["model_name"]}
    else:
        raise HTTPException(status_code=400, detail="Model is not loaded")

@router.post("/load-model")
def load_model(model_name: str):
    """Loads a KI model."""
    ki_model_status["model_name"] = model_name
    ki_model_status["model_loaded"] = True
    logger.debug(f"Model {model_name} loaded.")
    return {"message": f"Model {model_name} loaded successfully"}

@router.post("/predict")
def predict(data: dict):
    """Makes a prediction using the KI model."""
    if not ki_model_status["model_loaded"]:
        raise HTTPException(status_code=400, detail="Model is not loaded")
    
    prediction_result = {"prediction": "Example prediction result"}
    logger.debug(f"Prediction made: {prediction_result}")
    return {"message": "Prediction made", "result": prediction_result}
