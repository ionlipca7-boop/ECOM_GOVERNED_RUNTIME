def score_donor(candidate):
    score = 0

    if candidate.get('has_readme'):
        score += 20
    if candidate.get('has_tests'):
        score += 20
    if candidate.get('has_runtime_guard'):
        score += 20
    if candidate.get('has_state_contract'):
        score += 20
    if candidate.get('has_cleanup_policy'):
        score += 20

    return {
        'status': 'DONOR_SCORE_READY',
        'score': score,
        'max_score': 100
    }
