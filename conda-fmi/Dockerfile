FROM condaforge/mambaforge:4.9.2-5

ARG CONDA_ENV helloworld
ENV CONDA_ENV ${CONDA_ENV}

COPY . .

RUN mamba env create && conda clean -afy

# install PythonFMU custom version
RUN conda run -n $CONDA_ENV python -m pip install gym
RUN conda run -n $CONDA_ENV git clone https://github.com/bfut/PythonFMU pythonfmu; \
        cat ./pythonfmu/pythonfmu/pythonfmu-export/CMakeLists.txt; \
        cd pythonfmu; \
        conda run -n $CONDA_ENV python -m pip install --verbose .

# run PythonFMU factory example
# ENTRYPOINT [ "conda run -n $CONDA_ENV python -c" ]
CMD conda run -n $CONDA_ENV python --version; \
        cd pythonfmu/examples; \
        conda run -n $CONDA_ENV pythonfmu build -f ./demoslave.py --no-external-tool; \
        ls -lg
