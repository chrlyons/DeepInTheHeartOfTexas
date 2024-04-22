FROM python:3.12-slim AS base

FROM base AS base_plus_src
COPY . ./

FROM base_plus_src AS song
CMD ["python3", "main.py"]