
# Validates that a recipe meets all requirements and has all expected values
def validate(source):
    # Check that minimum fields are meet
    # Validate Baker's Percent
    # Check for duplicates (Recipe, Author, Origin, Ingredient, Tool, etc.)
    return False

# Needs to be automated in form manager to work for any form object
# Translates a recipe into a valid recipe object
def objectify(source, mapping):
    recipe = {}

    recipe['title'] = source.get(mapping['title'], None)
    recipe['description'] = source.get(mapping['description'], None)
    recipe['modified'] = source.get(mapping['modified'], None)
    recipe['origin'] = {
        'id': source.get(mapping['origin']['id'], None),
        'authors': None, # Get list of authors matching regex
        'source': source.get(mapping['origin']['source'], None),
        'reference': source.get(mapping['origin']['reference'], None)
    }
    recipe['categories'] = [] #get list of categories matching regex

    recipe['ingredients'] = []
    recipe['equipment'] = []

    recipe['instructions'] = {}
    recipe['instructions']['preperation'] = []
    recipe['instructions']['cooking'] = []
    recipe['instructions']['serving'] = []
    recipe['instructions']['storage'] = []
    recipe['instructions']['tips'] = []

    #ingredients
    index = 1
    while True:
        name = source.get(mapping['ingredients']['name'].format(index), None)
        if name is None:
            break;

        temp = {}
        temp['name'] = source.get(mapping['ingredients']['name'].format(index), None)
        temp['preperation'] = source.get(mapping['ingredients']['preperation'].format(index), None)
        temp['amount'] = source.get(mapping['ingredients']['amount'].format(index), None) #run calculation instead
        base = source.get(mapping['ingredients']['bakers_percent']['base'].format(index), None)
        temp['bp_base'] = False if base is None else True
        temp['bp_percent'] = source.get(mapping['ingredients']['bakers_percent']['percent'].format(index))

        recipe['ingredients'].append(temp)

        index += 1

    index = 1
    while True: #make a for after getting all fields that match regex
        instruct = source.get(mapping['preperation']['value'].format(index))
        if instruct is None:
            break
        recipe['instructions']['preperation'].append(instruct)

        index += 1

#    ingredients = []# find list of items matching regex in ingredients
#    for item in ingredients:


#    if validate(recipe):
    return recipe;

#    raise ValidationError
