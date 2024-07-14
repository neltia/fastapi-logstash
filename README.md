# fastapi-logstash
Basic Auth &amp; WAS ->ELK Log Analysis

## Setting
### virtualenv
Vagrantfile setup & Virtualbox

vagrant: 2.4.0
virtualbox: 6.1
linux: ubuntu linux 22.04

### ES Cluster
- .env file
<pre>
ES_CRT_PATH=/usr/share/certs/ca/ca.crt

# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=

# Version of Elastic products
STACK_VERSION=8.11.1

# Set the cluster name
CLUSTER_NAME=docker-cluster

# Set to 'basic' or 'trial' to automatically start the 30-day trial
LICENSE=basic

# Port to expose Elasticsearch HTTP API to the host
ES_PORT=9200

# Port to expose Kibana to the host
KIBANA_PORT=5601

# Increase or decrease based on the available host memory (in bytes)
MEM_LIMIT=1073741824

# Project namespace (defaults to the current folder name if not set)
# COMPOSE_PROJECT_NAME=myproject
</pre>

- test settings
  - ELK: vb linux
  - WAS: Windows
<pre>
sudo docker-compose -f docker-compose-dev.yml down
sudo docker-compose -f docker-compose-dev.yml up
sudo docker logs fastapi-logstash_logstash_1
</pre>

### Mapping
- log index Mapping
<pre>
PUT /_index_template/fastapi-log-template
{
  "index_patterns": ["fastapi-logs-*"],
  "template": {
    "mappings": {
      "properties": {
        "timestamp": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
        },
        "message": {
          "type": "text"
        },
        "level": {
          "type": "keyword"
        }
      }
    }
  }
}
</pre>

- WAS RUN
<pre>
uvicorn app.main:app
</pre>
