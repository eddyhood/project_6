import json

def update_json():
    with open('minerals.json', 'r') as f:
        new_data = []
        pk = 0
        data = json.load(f)
        for mydict in data:
            try:
                mydict['image_filename'] = mydict.pop('image filename')
            except:
                continue
            try:
                mydict['image_caption'] = mydict.pop('image caption')
            except:
                continue
            try:
                mydict['strunz_classification'] = mydict.pop('strunz classification')
            except:
                continue
            try:
                mydict['crystal_system'] = mydict.pop('crystal system')
            except:
                continue
            try:
                mydict['unit_cell'] = mydict.pop('unit cell')
            except:
                continue
            try:
                mydict['crystal_symmetry'] = mydict.pop('crystal symmetry')
            except:
                continue
            try:
                mydict['mohs_scale_hardness'] = mydict.pop('mohs scale hardness')
            except:
                continue
            try:
                mydict['optical_properties'] = mydict.pop('optical properties')
            except:
                continue
            try:
                mydict['refractive_index'] = mydict.pop('refractive index')
            except:
                continue
            try:
                mydict['crystal_habit'] = mydict.pop('crystal habit')
            except:
                continue
            try:
                mydict['specific_gravity'] = mydict.pop('specific gravity')
            except:
                continue
            try:
                path = mydict['image_filename']
                name = mydict['name']
                mydict['image_filename'] = str(name)+'.jpg'
            except:
                continue

            pk += 1
            entry = {
                'model': 'rocks.Rock',
                'pk': pk,
                'fields': mydict
            }
            new_data.append(entry)

    with open('modified_minerals.json', 'w') as m:
        json.dump(new_data, m, indent=2)


update_json()
