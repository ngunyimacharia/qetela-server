from django.test import TestCase

from .models import Organisation
from .seeder import gen_organisastion
from qetela.schema import schema

def initialize():
    organisation = Organisation(
        id=1,
        name='Test'
    )
    return organisation.save()

class OrganisationGraphTests(TestCase):
    def test_organisations_with_no_records(self):
        query = '''
        query organisations {
            organisations{
                name,
                website,
                branches,
                cfFrequency,
                created,
                updated
            }
        }
        '''
        expected = {
            "organisations": []
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_organisations_with_one_record(self):
        initialize()
        query = '''
        query organisations {
            organisations{
                id,
                name,
                website,
                branches,
                cfFrequency
            }
        }
        '''
        expected = {
            "organisations": [
                {
                    "id": "1",
                    "name": "Test",
                    "website": None,
                    "branches": False,
                    "cfFrequency": 7
                }
            ]
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_get_organisation(self):
        initialize()
        query = '''
        query organisation{
            organisation(id:1){
                id,
                name,
                website,
                branches,
                cfFrequency
            }
        }
        '''
        expected = {
                "organisation": {
                  "id": "1",
                  "name": "Test",
                  "website": None,
                  "branches": False,
                  "cfFrequency": 7
                }
        }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected


    def test_adding_organisation(self):
        mutation = '''
        mutation createOrganisation {
            createOrganisation(name:"Test"){
                name,
                website,
                branches,
                cfFrequency,
            }
        }
        '''
        expected = {
            "createOrganisation": {
              "name": "Test",
              "website": None,
              "branches": False,
              "cfFrequency": 7,
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected


    def test_updating_organisation(self):
        initialize()
        mutation = '''
        mutation updateOrganisation {
            updateOrganisation(id:1,name:"Updated",website:"updated.com",branches:true,cfFrequency:2){
                name,
                website,
                branches,
                cfFrequency,
            }
        }
        '''
        expected = {
            "updateOrganisation": {
              "name": "Updated",
              "website": "updated.com",
              "branches": True,
              "cfFrequency": 2,
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_delete_organisation(self):
        initialize()
        mutation = '''
        mutation deleteOrganisation {
            deleteOrganisation(id:1){
                ok
            }
        }
        '''
        expected = {
            "deleteOrganisation": {
              "ok": True
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

class OrganisationSeederTest(TestCase):
    def test_seeder(self):
        gen_organisastion(10)
        assert Organisation.objects.all().count() == 10
