#!/usr/bin/env bash

rm -rf pem openssl_config csr_out cert_out
# create private key
openssl genrsa -out pem 2048

# create csr config
# - what is sans list?: SAN - subject alternative names
# - in a SAN certificate, you can have multiple complete CN
# - modern clients need SAN attribute: https://support.apple.com/en-us/HT210176
cat <<'EOF' >openssl_config
[req]
default_bits              = 2048
req_extensions            = extension_requirements
distinguished_name        = dn_requirements

[extension_requirements]
basicConstraints          = CA:FALSE
keyUsage                  = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName            = @sans_list

[dn_requirements]
countryName               = KO
stateOrProvinceName       = Seoul
localityName              = Seoul
0.organizationName        = Desilo
organizationalUnitName    = Engineering
commonName                = Common Name (e.g. server FQDN or YOUR name)
emailAddress              = seungwoo.jung@desilo.ai

[sans_list]
DNS.1                     = desilo.co

EOF

# create csr
openssl req -new -key pem -out csr_out -config openssl_config

# create self-signed cert
openssl x509 -req -signkey pem -in csr_out -out cert_out -days 5
