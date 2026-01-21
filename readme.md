# FlaskIntroduction

> This repository has been archived and is no longer being updated.

## How To Run

1. Install `virtualenv`:

    ```sh
    pip install virtualenv
    ```

2. Open a terminal in the project root directory and run:

    ```sh
    virtualenv env
    ```

3. Then run the command:

    ```sh
    .\env\Scripts\activate
    ```

4. Then install the dependencies:

    ```sh
    (env) pip3 install -r requirements.txt
    ```

5. Finally start the web server:

    ```sh
    (env) python app.py
    ```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line:

```python

if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
