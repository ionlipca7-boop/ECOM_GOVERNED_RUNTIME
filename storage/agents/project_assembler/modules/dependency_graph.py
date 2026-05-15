def build_dependency_graph():
    return {
        'status': 'PROFILE_LEVEL_DEPENDENCY_GRAPH_READY',
        'edges': [
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
        ],
        'note': 'Current graph is profile-level. File-level import/dependency tracing may be added later.'
    }
