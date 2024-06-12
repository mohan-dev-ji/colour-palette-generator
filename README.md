# Color Analysis App

The Color Analysis App is a Flask web application that allows users to upload an image, and then analyzes the image to display the 10 most common colors along with their respective hex codes.

## Features

- Upload an image file (PNG, JPG, etc.)
- Display the uploaded image on the web page
- Analyze the colors in the uploaded image
- Show the top 10 most common colors with their hex codes
- Display color swatches for a visual representation

## Prerequisites

- Python (version 3.6 or later)
- Flask (Python web framework)
- Pillow (Python Imaging Library)
- NumPy (numerical computing library)

## Installation

1. Clone the repository:


git clone https://github.com/mohan-dev-ji/colour-palette-generator.git

2. Navigate to the project directory:


cd colour-palette-generator

3. Create a virtual environment (optional but recommended):


python -m venv env
source env/bin/activate # On Windows, use env\Scripts\activate

4. Install the required dependencies:


pip install -r requirements.txt

## Usage

1. Run the Flask application:


python app.py

2. Open your web browser and navigate to `http://localhost:5000`.

3. Upload an image file using the file input field.

4. After uploading the image, the application will display the uploaded image and the top 10 most common colors with their hex codes.


## Configuration

You can configure the following settings in the `app.py` file:

- `UPLOAD_FOLDER`: The directory where uploaded images will be stored temporarily.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).