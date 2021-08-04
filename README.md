Tools and scripts useful for Devops purposes for Ckan projects.


## Tests

Python tests checking basic CKAN endpoints are working as expected

### Running tests

```
python -m unittest discover -s tests/uptime-check -p "*_test.py" -v
```

### Environment Variables

- `CKAN_BASE_URL` - Base URL for a CKAN portal. Same as `ckan.site_url`
- `CKAN_API_KEY` - Sysadmin API key


## Scirpts

### `templater.sh`

Updates files with variables defined as `{{VARIABLE_NAME}}` in the given file
with Environment Variables with the same name

#### Usage

Pass the path to the file to `tempalter.sh` and save output to new file

```
bash scripts/templater.sh values.yaml.template > values.yaml
```
