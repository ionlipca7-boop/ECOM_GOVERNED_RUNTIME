import argparse
from pathlib import Path

from project_assembler_agent import ProjectAssemblerAgent
from modules.self_audit import run_self_audit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', required=True)
    parser.add_argument(
        '--mode',
        default='full_readonly',
        choices=['inventory_only', 'full_readonly', 'self_audit'],
    )
    args = parser.parse_args()

    if args.mode == 'self_audit':
        root = Path(__file__).resolve().parent
        result = run_self_audit(root)
        print(result['status'])
        print(result['present_count'])
        print(result['missing_count'])
        return

    agent = ProjectAssemblerAgent(args.profile)

    if args.mode == 'inventory_only':
        inventory_result = agent.inventory_scan()
        report_path = agent.build_initial_report(inventory_result)
        print('ASSEMBLER_INVENTORY_PASS')
        print(report_path)
        return

    result = agent.run_full_readonly_workflow()

    print('ASSEMBLER_FULL_READONLY_PASS')
    print(result['status'])
    print(result['outputs_dir'])


if __name__ == '__main__':
    main()
