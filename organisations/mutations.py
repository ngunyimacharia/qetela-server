from organisations.models import Organisation as OrganisationModel
from organisations.models import Level as LevelModel
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


class OrganisationMutations(graphene.ObjectType):
    create_organisation = CreateOrganisationMutation.Field()
    update_organisation = UpdateOrganisationMutation.Field()
    delete_organisation = DeleteOrganisationMutation.Field()
    add_level = AddLevelMutation.Field()
    update_level = UpdateLevelMutation.Field()
    delete_level = DeleteLevelMutation.Field()
