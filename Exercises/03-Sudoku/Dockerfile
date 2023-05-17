# Start base image/container
FROM python:alpine      



RUN pip install requests regex
WORKDIR /app
ADD sudoku.py /app/sudoku.py


ENTRYPOINT [ "python", "sudoku.py" ]