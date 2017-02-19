<h1>API</h1>

Base URL: /api/v1/

## NoiseData

Endpoint: /api/v1/noisedata/

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": {
        "type": "FeatureCollection",
        "features": [
            {
                "id": 1,
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        8.525390625,
                        13.798828125
                    ]
                },
                "properties": {
                    "noise_mean_day": 10.0
                }
            }
        ]
    }
}
```

Endpoint: /api/v1/noisedata/<id>
```json
{
    "id": 1,
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [
            8.525390625,
            13.798828125
        ]
    },
    "properties": {
        "noise_mean_day": 10.0
    }
}
```