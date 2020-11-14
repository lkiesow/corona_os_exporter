# corona\_os\_exporter

Prometheus Exporter for Osnabrück COVID-19 Cases

Run this by executing

```shell
python3 corona_os_exporter.py
```

The metrics are available at 127.0.0.1:8888/metrics:

```sh
# HELP corona_osnabrueck_cases Number of cases in Osna
# TYPE corona_osnabrueck_cases gauge
corona_osnabrueck_cases{type="confirmed", authority="district"} 1038
corona_osnabrueck_cases{type="recovered", authority="district"} 2888
corona_osnabrueck_cases{type="dead", authority="district"} 85
corona_osnabrueck_cases{type="confirmed", authority="city"} 283
corona_osnabrueck_cases{type="recovered", authority="city"} 1316
corona_osnabrueck_cases{type="dead", authority="city"} 16
```
