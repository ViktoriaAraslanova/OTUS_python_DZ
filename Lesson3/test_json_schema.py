from jsonschema import validate
import json


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)


def test_get_a_resource(session, base_url):
    res = session.get(f'{base_url}/1')
    assert_valid_schema(
        res.json(), 'schemas/getting_a_resource_schema.json'
    )


def test_listing_all_resources(session, base_url):
    res = session.get(f'{base_url}')
    assert_valid_schema(
        res.json(), 'schemas/listing_all_resources_schema.json'
    )
