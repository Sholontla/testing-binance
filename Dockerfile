FROM python:3.9

# 
WORKDIR /.

# 
COPY ./requirements.txt ./requirements.txt
COPY ./static /static
COPY ./templates /templates
# 
RUN pip install  --upgrade -r ./requirements.txt

# 
COPY . .

# 
CMD ["main.py"]
ENTRYPOINT ["python"]