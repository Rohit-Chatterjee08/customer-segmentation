# in app.py

import gradio as gr
import requests
import json

# The URL where our FastAPI is running
API_URL = "https://segmentation-service-86215100553.us-central1.run.app/segment"

def segment_customer(annual_income, spending_score):
    """
    Sends customer data to the FastAPI and returns the predicted segment.
    """
    # Create the payload to send to the API
    payload = {
        "annual_income": annual_income,
        "spending_score": spending_score
    }
    
    try:
        # Make the POST request to our API
        response = requests.post(API_URL, json=payload)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        # Parse the JSON response
        result = response.json()
        segment_name = result.get("segment_name", "N/A")
        
        # Return a dictionary for the Label component
        return {segment_name: 1.0}

    except requests.exceptions.RequestException as e:
        # Handle connection errors or other request issues
        error_message = f"Error connecting to the API: {e}"
        print(error_message)
        return {"Error": 1.0}

# --- Build the Gradio App ---
with gr.Blocks(theme=gr.themes.Soft(), title="Customer Segmentation") as app:
    gr.Markdown("# 🛍️ Customer Segmentation Tool")
    gr.Markdown("Enter a customer's details to find their market segment.")

    with gr.Row():
        income_slider = gr.Slider(
            minimum=15, maximum=140, value=50, 
            label="Annual Income (in thousands of $)"
        )
        score_slider = gr.Slider(
            minimum=1, maximum=99, value=50, 
            label="Spending Score (1-100)"
        )
    
    segment_button = gr.Button("Find Segment", variant="primary")
    
    output_label = gr.Label(label="Predicted Segment")

    segment_button.click(
        fn=segment_customer,
        inputs=[income_slider, score_slider],
        outputs=output_label
    )

app.launch()