# corona_os_exporter

Prometheus Exporter for Osnabrück COVID-19 Cases

Run this by executing

```shell
python3 corona_os_exporter.py
```

The metrics are available at 127.0.0.1:8888/metrics:

```sh
# curl http://127.0.0.1:8888/metrics
# HELP corona_osnabrueck_cases Number of cases in Osnabrueck
# TYPE corona_osnabrueck_cases gauge
corona_osnabrueck_cases{type="confirmed"} 1280
corona_osnabrueck_cases{type="recovered"} 4071
corona_osnabrueck_cases{type="dead"} 101
```
