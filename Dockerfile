FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app             
COPY requirements.txt ./  
RUN pip3 install -r requirements.txt
COPY ./ ./
WORKDIR /app/DataEntryProject     
EXPOSE 8000               
CMD python3 ./manage.py runserver 0.0.0.0:8000  
