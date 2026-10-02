"""Review normalized encryption posture and explicit KMS key metadata."""

def analyze(data):
    out = []
    for r in data.get("resources", []):
        if r.get("encrypted") is not True:
            unknown = r.get("encrypted") is None
            out.append(finding(r["id"], "UNKNOWN" if unknown else "HIGH", "ENCRYPTION_STATE", "Encryption status is unknown." if unknown else "Resource explicitly reports encryption disabled.", "Collect authoritative encryption settings and enable encryption when supported.", r))
    for k in data.get("keys", []):
        if k.get("state") in {"Disabled", "PendingDeletion"}:
            out.append(finding(k["id"], "HIGH", "KEY_UNAVAILABLE", "Key is disabled or pending deletion; dependent workloads may fail.", "Review key dependencies and approved lifecycle change.", k))
        if k.get("rotation_supported") is True and k.get("rotation_enabled") is False:
            out.append(finding(k["id"], "MEDIUM", "ROTATION_DISABLED", "Supported key rotation is disabled.", "Review rotation requirements and enable supported rotation.", k))
    return out

import argparse
import json
import sys
from pathlib import Path

def finding(resource, severity, check, detail, remediation, evidence):
    return dict(resource=resource, severity=severity, check=check, detail=detail, remediation=remediation, evidence=evidence)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--output", type=Path)
    p.add_argument("--fail-on-high", action="store_true")
    args = p.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict):
            raise ValueError("Expected JSON object")
        results = analyze(data)
        text = json.dumps({"results": results, "count": len(results), "scope": __doc__}, indent=2)
        if args.output:
            args.output.write_text(text + "\n", encoding="utf-8")
        else:
            print(text)
        return int(args.fail_on_high and any(r["severity"] == "HIGH" for r in results))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as e:
        print(f"Input/report error: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())

