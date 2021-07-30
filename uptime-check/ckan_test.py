import os
import requests
import unittest
import random

from urllib.parse import urljoin

API_KEY = os.environ.get('CKAN_API_KEY', '')
BASE_URL = os.environ.get('CKAN_BASE_URL', '')
SKIP_USER_LIST = os.environ.get('SKIP_USER_LIST', False)


def _make_request(endpoint='', full_url=False):
    headers = {'Authorization': API_KEY}
    resp = requests.get(
            urljoin(BASE_URL if not full_url else '', endpoint),
            headers = {'Authorization': API_KEY}
        )
    return resp


def _get_json(endpoint=''):
    resp = _make_request(endpoint)
    if resp.status_code == 200:
        return resp.json()
    return {}


def _get_random_package():
    random_package = {}
    package_search = _get_json('api/action/package_search').get('result')
    results = package_search.get('results',[])
    if len(results):
        rand_pkg_index = random.randrange(len(results))
        random_package = results[rand_pkg_index]
    return random_package


def _get_random_resource_id():
    random_resource_id = None
    random_resource_url = None
    random_package = _get_random_package()
    random_pkg_id = random_package.get('name')
    resources = random_package.get('resources',[])
    if len(resources):
        rand_res_index = random.randrange(len(resources))
        random_resource_id = random_package.get('resources',[])[rand_res_index].get('id')
        random_resource_url = random_package.get('resources',[])[rand_res_index].get('url')
    return random_pkg_id, random_resource_id, random_resource_url



RANDOM_PACKAGE_ID = _get_random_package().get('name')
RANDOM_RES_PKG_ID, RANDOM_RESOURCE_ID, RANDOM_RESOURCE_URL = _get_random_resource_id()

class CkanAPITestCase(unittest.TestCase):

    def test__status_show(self):
        resp = _make_request('api/action/status_show')
        self.assertEqual(resp.status_code, 200)

    def test__site_read(self):
        resp = _make_request('api/action/site_read')
        self.assertEqual(resp.status_code, 200)

    def test__package_list(self):
        resp = _make_request('api/action/package_list')
        self.assertEqual(resp.status_code, 200)

    def test__current_package_list_with_resources(self):
        resp = _make_request('api/action/current_package_list_with_resources')
        self.assertEqual(resp.status_code, 200)

    def test__group_list(self):
        resp = _make_request('api/action/group_list')
        self.assertEqual(resp.status_code, 200)

    def test__organization_list(self):
        resp = _make_request('api/action/organization_list')
        self.assertEqual(resp.status_code, 200)

    def test__license_list(self):
        resp = _make_request('api/action/license_list')
        self.assertEqual(resp.status_code, 200)

    def test__tag_list(self):
        resp = _make_request('api/action/tag_list')
        self.assertEqual(resp.status_code, 200)

    @unittest.skipIf(SKIP_USER_LIST, "Forbidden, returns 403")
    def test__user_list(self):
        resp = _make_request('api/action/user_list')
        self.assertEqual(resp.status_code, 200)

    def test__package_show(self):
        resp = _make_request(f'api/action/package_show?id={RANDOM_PACKAGE_ID}')
        self.assertEqual(resp.status_code, 200)

    def test__resource_show(self):
        resp = _make_request(f'api/action/resource_show?id={RANDOM_RESOURCE_ID}')
        self.assertEqual(resp.status_code, 200)

    def test__resource_view_list(self):
        resp = _make_request(f'api/action/resource_view_list?id={RANDOM_RESOURCE_ID}')
        self.assertEqual(resp.status_code, 200)

    def test__package_search(self):
        resp = _make_request('api/action/package_search')
        self.assertEqual(resp.status_code, 200)

    def test__resource_search(self):
        resp = _make_request('api/action/resource_search?query=name:District%20Names')
        self.assertEqual(resp.status_code, 200)

    def test__tag_search(self):
        resp = _make_request('api/action/tag_search?query="name:test"')
        self.assertEqual(resp.status_code, 200)

    def test__vocabulary_list(self):
        resp = _make_request('api/action/vocabulary_list')
        self.assertEqual(resp.status_code, 200)


class CkanPagesTestCase(unittest.TestCase):

    def test__main_page(self):
        resp = _make_request()
        self.assertEqual(resp.status_code, 200)

    def test__dataset_page(self):
        resp = _make_request('dataset')
        self.assertEqual(resp.status_code, 200)

    def test__org_page(self):
        resp = _make_request('organization')
        self.assertEqual(resp.status_code, 200)

    def test__group_page(self):
        resp = _make_request('group')
        self.assertEqual(resp.status_code, 200)

    def test__about_page(self):
        resp = _make_request('about')
        self.assertEqual(resp.status_code, 200)

    @unittest.skipIf(RANDOM_PACKAGE_ID is None, 'WARNING: No dataset found')
    def test__random_dataset_page(self):
        resp = _make_request(f'dataset/{RANDOM_PACKAGE_ID}')
        self.assertEqual(resp.status_code, 200)

    @unittest.skipIf(RANDOM_PACKAGE_ID is None, 'WARNING: No dataset found')
    def test__random_dataset_activity_page(self):
        resp = _make_request(f'dataset/activity/{RANDOM_PACKAGE_ID}')
        self.assertEqual(resp.status_code, 200)

    @unittest.skipIf(RANDOM_RESOURCE_ID is None, 'WARNING: No dataset found')
    def test__random_resource_page(self):
        resp = _make_request(f'dataset/{RANDOM_RES_PKG_ID}/resource/{RANDOM_RESOURCE_ID}')
        self.assertEqual(resp.status_code, 200)

    @unittest.skipIf(RANDOM_RESOURCE_ID is None, 'WARNING: No dataset found')
    def test__random_resource_download(self):
        resp = _make_request(RANDOM_RESOURCE_URL, full_url=RANDOM_RESOURCE_URL.startswith('http'))
        self.assertEqual(resp.status_code, 200)


def _make_request(endpoint='', full_url=False):
    headers = {'Authorization': API_KEY}
    resp = requests.get(
            urljoin(BASE_URL if not full_url else '', endpoint),
            headers = {'Authorization': API_KEY}
        )
    return resp


def _get_json(endpoint=''):
    resp = _make_request(endpoint)
    if resp.status_code == 200:
        return resp.json()
    return {}


def _get_random_package():
    random_package = {}
    package_search = _get_json('api/action/package_search').get('result')
    results = package_search.get('results',[])
    if len(results):
        rand_pkg_index = random.randrange(len(results))
        random_package = results[rand_pkg_index]
    return random_package


def _get_random_resource_id():
    random_resource_id = None
    random_resource_url = None
    random_package = _get_random_package()
    random_pkg_id = random_package.get('name')
    resources = random_package.get('resources',[])
    if len(resources):
        rand_res_index = random.randrange(len(resources))
        random_resource_id = random_package.get('resources',[])[rand_res_index].get('id')
        random_resource_url = random_package.get('resources',[])[rand_res_index].get('url')
    return random_pkg_id, random_resource_id, random_resource_url


def _skip_and_warn_if_resource_not_xists(cls, endpoint, full_url=False):
    if RANDOM_RESOURCE_ID:
        resp = _make_request(endpoint, full_url=full_url)
        cls.assertEqual(resp.status_code, 200)
    else:
        print(f'WARNING: No Resource found for dataset "{RANDOM_RES_PKG_ID}", skipping!')
