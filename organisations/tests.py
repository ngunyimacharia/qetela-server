from django.test import TestCase

from .models import Organisation,Level,Team,Position
from .seeder import gen_organisations
from qetela.schema import schema

def initialize():
    organisation = Organisation(
        id=1,
        name='Test'
    )
    organisation.save()
    level = Level(
        id=1,
        label='Test',
        number=1,
        organisation=organisation
    )
    level.save()
    team = Team(
        id=1,
        name='Test',
        active=True,
        level=level
    )
    team.save()
    position = Position(
        id=1,
        title='Test',
        description='Test description',
        team = team
    )
    position.save()

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

class LevelGraphTests(TestCase):
    def test_get_organisation_with_level(self):
        initialize()
        query = '''
        query organisation{
          organisation(id:1){
            name,
            website
            levelSet{
              label
              number,
            }
          }
        }
        '''
        expected = {
            "organisation": {
              "name": "Test",
              "website": None,
              "levelSet": [
                {
                  "label": "Test",
                  "number": 1
                }
                ]
            }
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_adding_level(self):
        initialize()
        mutation = '''
        mutation addLevel {
            addLevel(organisationId:1,label:"Test"){
                label,
                number
            }
        }
        '''
        expected = {
            "addLevel": {
              "label": "Test",
              "number":2
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_updating_level(self):
        initialize()
        mutation = '''
        mutation updateLevel {
            updateLevel(id:1,label:"Updated"){
                label
            }
        }
        '''
        expected = {
            "updateLevel": {
              "label": "Updated"
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_delete_level(self):
        initialize()
        mutation = '''
        mutation deleteLevel {
            deleteLevel(id:1){
                ok
            }
        }
        '''
        expected = {
            "deleteLevel": {
              "ok": True
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

class TeamGraphTest(TestCase):
    def test_get_organisation_with_team(self):
        initialize()
        query = '''
        query organisation{
          organisation(id:1){
            name
            levelSet{
              label
              teamSet{
                id,
                name
              }
            }
          }
        }
        '''
        expected = {
           "organisation": {
              "name": "Test",
              "levelSet": [
                {
                  "label": "Test",
                  "teamSet": [
                    {
                      "id": "1",
                      "name": "Test"
                    }
                  ]
                }
                ]
            }
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_adding_team(self):
        initialize()
        mutation = '''
        mutation addTeam{
          addTeam(levelId:1,name:"Test"){
            name
          }
        }
        '''
        expected = {
           "addTeam": {
             "name": "Test"
           }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_updating_team(self):
        initialize()
        mutation = '''
        mutation updateTeam{
          updateTeam(id:1,name:"Updated"){
            id
            name
          }
        }
        '''
        expected = {
           "updateTeam": {
             "id":1,
             "name": "Updated"
           }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_deleting_team(self):
        initialize()
        mutation = '''
        mutation deleteTeam{
          deleteTeam(id:1){
            ok
          }
        }
        '''
        expected = {
           "deleteTeam": {
             "ok": True
           }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

class PositionGraphTest(TestCase):
    def test_get_organisation_with_position(self):
        initialize()
        query = '''
        query organisation{
          organisation(id:1){
            name
            levelSet{
              label
              teamSet{
                name
                positionSet{
                  id,
                  title
                }
              }
            }
          }
        }
        '''
        expected = {
           "organisation": {
              "name": "Test",
              "levelSet": [
                {
                  "label": "Test",
                  "teamSet": [
                    {
                      "name": "Test",
                      "positionSet": [
                        {
                          "id":"1",
                          "title": "Test"
                        }
                       ]
                    }
                  ]
                }
                ]
            }
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_adding_position(self):
        initialize()
        mutation = '''
        mutation addPosition{
          addPosition(teamId:1,title:"Test",description:"Test description"){
            title
          }
        }
        '''
        expected = {
           "addPosition": {
             "title": "Test"
           }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_updating_position(self):
        initialize()
        mutation = '''
        mutation updatePosition{
          updatePosition(id:1,title:"Updated",description:"Updated description"){
            title,
            description
          }
        }
        '''
        expected = {
           "updatePosition": {
             "title": "Updated",
             "description":"Updated description"
           }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

    def test_deleting_position(self):
        initialize()
        mutation = '''
        mutation deletePosition{
          deletePosition(id:1){
            ok
          }
        }
        '''
        expected = {
           "deletePosition": {
             "ok": True
           }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected

class OrganisationSeederTest(TestCase):
    def test_seeder(self):
        gen_organisations(1)
        assert Organisation.objects.all().count() == 1
