from collections import defaultdict


def default_edges():
    return [
        ['telegram', 'url_intake'],
        ['url_intake', 'field_sources'],
        ['field_sources', 'photo_pipeline'],
        ['field_sources', 'description_html'],
        ['field_sources', 'category_aspects'],
        ['category_aspects', 'listing_registry'],
        ['description_html', 'listing_registry'],
        ['photo_pipeline', 'listing_registry'],
        ['listing_registry', 'final_critic'],
        ['final_critic', 'ebay_readonly']
    ]


def build_capability_graph(inventory, expected_capabilities=None):
    capability = defaultdict(lambda: {
        'files': [],
        'classifications': defaultdict(int),
        'risk_flags': defaultdict(int)
    })

    for item in inventory:
        for tag in item['capability_tags']:
            node = capability[tag]
            node['files'].append(item['relative_path'])
            node['classifications'][item['classification']] += 1
            for flag in item['risk_flags']:
                node['risk_flags'][flag] += 1

    capability_map = {
        key: {
            'file_count': len(value['files']),
            'sample_files': value['files'][:80],
            'classification_counts': dict(value['classifications']),
            'risk_flag_counts': dict(value['risk_flags'])
        }
        for key, value in sorted(capability.items())
    }

    gaps = []
    if expected_capabilities:
        gaps = [x for x in expected_capabilities if x not in capability_map]

    return {
        'capability_map': capability_map,
        'capability_graph': {
            'nodes': list(capability_map.keys()),
            'edges': default_edges()
        },
        'gaps': gaps
    }
