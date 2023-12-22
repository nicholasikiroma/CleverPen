# Title: CleverPen

## Description

CleverPen is a Flask-based blogging platform integrated with OpenAI's GPT 3.5 model. Created during my early software development journey, this project provided a valuable learning experience. I gained proficiency in Flask, the Jinja templating engine, and integrating third-party APIs into applications.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3
- Pip (Python Package Installer)

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/nicholasikiroma/CleverPen.git
    cd CleverPen
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:

        ```powershell
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables:**

    Create a `.env` file in the root directory and add your environment variables.

    ```env
    SECRET_KEY=your_secret_key
    API_KEY=api_key_provided_by_openAI
    ```

6. **Run the App:**

    ```bash
    flask run
    ```

    Your app will be accessible at [http://localhost:5000](http://localhost:5000).

Happy coding! 🚀
