def score_donors(inventory):
    scored = []

    for item in inventory:
        score = 0
        reasons = []

        if item['classification'] in ['WORKING_DONOR', 'ACTIVE_ROUTE']:
            score += 40
            reasons.append('working_or_active_classification')

        if any(tag != 'unknown' for tag in item['capability_tags']):
            score += 20
            reasons.append('has_capability_tags')

        if item['suffix'] in ['.py', '.json', '.md', '.txt']:
            score += 10
            reasons.append('usable_text_or_code_file')

        if item['risk_flags']:
            score -= 20
            reasons.append('risk_flags_present')

        if item['classification'] in [
            'ARCHIVE_NOISE',
            'FAILED_ATTEMPT_NO_ACTIVE_WRITE',
            'FORBIDDEN_PATH'
        ]:
            score -= 50
            reasons.append('not_promotable_classification')

        scored.append({
            'path': item['path'],
            'relative_path': item['relative_path'],
            'capability_tags': item['capability_tags'],
            'classification': item['classification'],
            'risk_flags': item['risk_flags'],
            'score': score,
            'reasons': reasons,
            'promotion_decision': 'CANDIDATE_REVIEW_REQUIRED' if score >= 50 else 'DO_NOT_PROMOTE_NOW'
        })

    scored.sort(key=lambda x: x['score'], reverse=True)

    return {
        'scoreboard': scored,
        'selected_donors': [x for x in scored if x['promotion_decision'] == 'CANDIDATE_REVIEW_REQUIRED'][:50],
        'quarantine': [x for x in scored if x['classification'] == 'QUARANTINE_CANDIDATE'][:500],
        'forbidden': [x for x in scored if x['classification'] == 'FORBIDDEN_PATH'][:500],
        'failed': [x for x in scored if x['classification'] == 'FAILED_ATTEMPT_NO_ACTIVE_WRITE'][:500]
    }
