FROM ubuntu:noble

ENV PATH="/root/.local/bin:$PATH"
ENV VIRTUAL_ENV="/opt/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# cargo required for pydantic-core?
# libxml2 libxslt for lxml
RUN apt-get update && apt-get install -y git curl cargo
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv python install 3.12
RUN uv venv $VIRTUAL_ENV

RUN curl -fsSL https://raw.githubusercontent.com/tj/n/master/bin/n | bash -s lts && \
    npm install -g n && \
    npm i -g wrangler

WORKDIR /app

COPY requirements.txt .
COPY README.md .
COPY metrics.json /root/.config/wrangler/metrics.json

RUN uv pip install --upgrade pip setuptools wheel
RUN uv pip install -r requirements.txt
RUN python -m compileall

ENV CLOUDFLARE_API_TOKEN=
# ENV TZ=America/Chicago

COPY entrypoint.sh .
# ENTRYPOINT ['entrypoint.sh']
CMD '/app/entrypoint.sh'
