def build_finish_signal(report_name='project_assembler_report_short_current.md'):
    return {
        'status': 'FINISH_ASSEMBLER_READY_FOR_HUMAN_AUDIT',
        'safe_state': 'STOP_SAFE_NO_RUNTIME_ACTION_PERFORMED',
        'report': report_name,
        'next': 'human audit before any physical clean build or runtime action'
    }
