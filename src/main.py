import json
from pathlib import Path

from eth_utils import to_canonical_address

from utils.constants import GENESIS_FORK_VERSION, GENESIS_VALIDATORS_ROOT
from utils.ssz import BLSToExecutionChange, compute_bls_to_execution_change_domain, compute_signing_root

EXECUTION_WITHDRAWAL_ADDRESS = to_canonical_address('0x2296e122c1a20Fca3CAc3371357BdAd3be0dF079')
BLS_WITHDRAWAL_PUBLIC_KEY = bytes.fromhex(
    '8b126e1a0e186a10d9fbaed2f8dc8f4d4c48459941d71ca9e9bfe3cbc54a638e9f726a0fa7e276eddadd7caa8afe27fb'
)
VALIDATORS_FILE = Path(Path(__file__).parent.resolve(), '../validators.txt')
PAYLOADS_FILE = Path(Path(__file__).parent.resolve(), '../payloads.json')


def get_bls_to_execution_change_signing_root(validator_index: int) -> bytes:
    message = BLSToExecutionChange(
        validator_index=validator_index,
        from_bls_pubkey=BLS_WITHDRAWAL_PUBLIC_KEY,
        to_execution_address=EXECUTION_WITHDRAWAL_ADDRESS,
    )
    domain = compute_bls_to_execution_change_domain(
        fork_version=GENESIS_FORK_VERSION,
        genesis_validators_root=GENESIS_VALIDATORS_ROOT,
    )
    return compute_signing_root(message, domain)


def main() -> None:
    # read validator indexes from file
    with open(VALIDATORS_FILE, "r") as f:
        validator_indexes = f.read().splitlines()

    # generate bls execution change payloads
    payloads = {}
    for index in validator_indexes:
        payloads[index] = get_bls_to_execution_change_signing_root(int(index)).hex()

    # write payloads to output file
    with open(PAYLOADS_FILE, "w") as f:
        json.dump(payloads, f)


if __name__ == '__main__':
    main()
