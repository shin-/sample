FROM python:3.7-alpine AS build
WORKDIR /app

RUN pip install -U pip
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY setup.py /app
COPY sample /app/sample/
RUN pip install .

FROM build AS lint
COPY requirements-lint.txt /app
RUN pip install -r requirements-lint.txt
ENTRYPOINT ["flake8"]
CMD ["./sample"]

FROM build AS test
COPY requirements-test.txt /app
RUN pip install -r requirements-test.txt
COPY tests /app/tests/
ENTRYPOINT ["py.test"]
CMD ["-v", "./tests"]

FROM python:3.7-alpine AS publish
COPY --from=build /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
RUN pip install ipython
ENTRYPOINT ["ipython"]
