FROM python:3.12-slim

# Prevents Python from buffering outputs
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /miosis_app

# Copy only requirements first for better caching
COPY requirements.txt /miosis_app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project files
COPY . /miosis_app/

# Expose port 5000
EXPOSE 5000

# Ensure the correct command is used
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:5000"]
