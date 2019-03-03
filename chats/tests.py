from django.test import TestCase

# from .models import Organisation,Level,Team,Position
from .seeder import gen_chats
from goals.seeder import gen_goals
from organisations.seeder import gen_organisations
from accounts.seeder import gen_users
from qetela.schema import schema

def initialize():
    gen_organisations()
    gen_users()
    gen_goals()
    gen_chats()

class GoalGraphTests(TestCase):
    def test_goals_with_no_record(self):
        query = '''
        query chats {
            chats{
                title
            }
        }
        '''
        expected = {
            "chats": []
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_goals_with_records(self):
        initialize()
        query = '''
        query{
          chats{
            title,
            messageSet{
              content
            }
          }
        }
        '''
        result = schema.execute(query)
        assert not result.errors
        #check goals
        chats = result.data['chats']
        assert len(chats) > 0
        #check kpis
        assert len(chats[3]['messageSet']) > 0
