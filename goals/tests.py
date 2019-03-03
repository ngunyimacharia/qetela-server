from django.test import TestCase

# from .models import Organisation,Level,Team,Position
from .seeder import gen_goals
from organisations.seeder import gen_organisations
from accounts.seeder import gen_users
from qetela.schema import schema

def initialize():
    gen_organisations()
    gen_users()
    gen_goals()

class GoalGraphTests(TestCase):
    def test_goals_with_no_record(self):
        query = '''
        query goals {
            goals{
                title,
                start,
                end
            }
        }
        '''
        expected = {
            "goals": []
         }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_goals_with_records(self):
        initialize()
        query = '''
        query{
          goals{
            title,
            kpiSet{
              target,
              metric,
              kpiupdateSet{
                progress
              }
            },
            goalallocationSet{
              team{
                name
              }
            },
          }
        }
        '''
        result = schema.execute(query)
        assert not result.errors
        #check goals
        goals = result.data['goals']
        assert len(goals) > 0
        #check kpis
        assert len(goals[0]['kpiSet']) > 0
        #check kpi updates
        assert len(goals[0]['kpiSet'][0]['kpiupdateSet']) > 0
        #check goal allocations
        assert len(goals[3]['goalallocationSet']) > 0
