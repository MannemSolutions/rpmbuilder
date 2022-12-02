FROM rockylinux:8

RUN dnf update -y && \
    dnf install -y python39 sudo make pinentry rpmdevtools rpm-build rpm-sign cmake bind-utils git iproute && \
    dnf groupinstall -y "Development Tools"

WORKDIR /usr/rpmbuilder

COPY rpmbuilder README.md /usr/rpmbuilder/
COPY scripts /

RUN pip3 install --upgrade pip && pip install --no-cache-dir .
RUN useradd -G wheel rpmbuilder
RUN /install_go.sh

USER rpmbuilder

CMD github2spec
