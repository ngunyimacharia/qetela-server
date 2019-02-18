from organisations.models import Organisation as OrganisationModel
from organisations.models import Level as LevelModel
from organisations.models import Team as TeamModel
from organisations.models import Position as PositionModel
import graphene

class CreateOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    website = graphene.String()
    branches = graphene.Boolean()
    cf_frequency = graphene.Int()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        id = graphene.Int()
        name = graphene.String(required=True)
        website = graphene.String()
        branches = graphene.Boolean()
        cf_frequency = graphene.Int()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, name, **org_data):
        website = org_data.get('website', None)
        branches = org_data.get('branches', False)
        cf_frequency = org_data.get('cf_frequency', 7)
        organisation = OrganisationModel(name=name,website=website,branches=branches,cf_frequency=cf_frequency)
        organisation.save()
        return CreateOrganisationMutation(id=organisation.id,name=organisation.name,website=organisation.website,branches=organisation.branches,cf_frequency=organisation.cf_frequency,created=organisation.created,updated=organisation.updated)


class UpdateOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    website = graphene.String()
    branches = graphene.Boolean()
    cf_frequency = graphene.Int()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        website = graphene.String()
        branches = graphene.Boolean()
        cf_frequency = graphene.Int()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, id, **org_data):

        organisation = OrganisationModel.objects.get(pk=id)

        for k,v in org_data.items():
            setattr(organisation,k,v)

        organisation.save()

        return UpdateOrganisationMutation(id=id,name=organisation.name,website=organisation.website,branches=organisation.branches,cf_frequency=organisation.cf_frequency,created=organisation.created,updated=organisation.updated)


class DeleteOrganisationMutation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):

        organisation = OrganisationModel.objects.get(pk=id)
        result = organisation.delete()
        return DeleteOrganisationMutation(ok=result)

class AddLevelMutation(graphene.Mutation):
    organisation_id = graphene.Int()
    id = graphene.Int()
    label = graphene.String()
    number = graphene.Int()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        organisation_id = graphene.Int()
        id = graphene.Int()
        label = graphene.String()
        number = graphene.Int()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, organisation_id, label):
        organisation = OrganisationModel.objects.get(pk=organisation_id)
        levels = organisation.level_set.all()
        level = LevelModel(label=label,number=(len(levels)+1),organisation=organisation)
        level.save()
        return AddLevelMutation(id=level.id,label=level.label,number=level.number,created=level.created,updated=level.updated)


class UpdateLevelMutation(graphene.Mutation):
    id = graphene.Int()
    label = graphene.String()
    number = graphene.Int()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        id = graphene.Int()
        label = graphene.String()
        number = graphene.Int()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, id, label):

        level = LevelModel.objects.get(pk=id)
        level.label = label
        level.save()

        return UpdateLevelMutation(id=level.id,label=level.label,number=level.number,created=level.created,updated=level.updated)


class DeleteLevelMutation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        level = LevelModel.objects.get(pk=id)
        organisation = level.organisation
        if(len(organisation.level_set.filter(number__gt=level.number))):
            raise ValueError("You can only delete the lowest level.")
        result = level.delete()
        return DeleteLevelMutation(ok=result)

class AddTeamMutation(graphene.Mutation):
    level_id = graphene.Int()
    id = graphene.Int()
    name = graphene.String()
    active = graphene.Boolean()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        level_id = graphene.Int()
        id = graphene.Int()
        name = graphene.String()
        active = graphene.Boolean()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, level_id, name):
        level = LevelModel.objects.get(pk=level_id)
        team = TeamModel(name=name,level=level,active=True)
        team.save()
        return AddTeamMutation(id=team.id,name=team.name,active=team.active)


class UpdateTeamMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    active = graphene.Boolean()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        active = graphene.Boolean()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, id, name):
        team = TeamModel.objects.get(pk=id)
        team.name = name
        team.save()
        return UpdateTeamMutation(id=team.id,name=team.name,active=team.active)

class DeleteTeamMutation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        ok = graphene.Boolean()

    def mutate(self, info, id):
        team = TeamModel.objects.get(pk=id)
        if team.children.count():
            raise ValueError("You cannot delete a team with children.")
        result = team.delete()
        return DeleteLevelMutation(ok=result)

class AddPositionMutation(graphene.Mutation):
    team_id = graphene.Int()
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        team_id = graphene.Int()
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, team_id, title, description):
        team = TeamModel.objects.get(pk=team_id)
        position = PositionModel(title=title,description=description,team=team)
        position.save()
        return position

class UpdatePositionMutation(graphene.Mutation):
    team_id = graphene.Int()
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    created = graphene.types.datetime.DateTime()
    updated = graphene.types.datetime.DateTime()

    class Arguments:
        team_id = graphene.Int()
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        created = graphene.types.datetime.DateTime()
        updated = graphene.types.datetime.DateTime()

    def mutate(self, info, id, **kwargs):
        position = PositionModel.objects.get(pk=id)
        for k,v in kwargs.items():
            setattr(position,k,v)
        position.save()
        return position

class DeletePositionMutation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        ok = graphene.Boolean()

    def mutate(self, info, id):
        position = PositionModel.objects.get(pk=id)
        result = position.delete()
        return DeletePositionMutation(ok=result)


class OrganisationMutations(graphene.ObjectType):
    create_organisation = CreateOrganisationMutation.Field()
    update_organisation = UpdateOrganisationMutation.Field()
    delete_organisation = DeleteOrganisationMutation.Field()
    add_level = AddLevelMutation.Field()
    update_level = UpdateLevelMutation.Field()
    delete_level = DeleteLevelMutation.Field()
    add_team = AddTeamMutation.Field()
    update_team = UpdateTeamMutation.Field()
    delete_team = DeleteTeamMutation.Field()
    add_position = AddPositionMutation.Field()
    update_position = UpdatePositionMutation.Field()
    delete_position = DeletePositionMutation.Field()
