FROM condaforge/miniforge3:24.11.3-2
RUN pip install nilearn==0.11.1
ENTRYPOINT ["python", "main.py"]
