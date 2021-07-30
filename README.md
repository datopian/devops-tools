Python tests checking basic CKAN endpoints are working as expected

## Run tests

```
python -m unittest discover -s uptime-check -p "*_test.py" -v
```

## Environment Variables

- `CKAN_BASE_URL` - Base URL for a CKAN portal. Same as `ckan.site_url`
- `CKAN_API_KEY` - Sysadmin API key
