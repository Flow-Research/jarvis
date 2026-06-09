#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

mkdir -p images

render_dot() {
  local source="$1"
  local target="$2"
  dot -Tpng "$source" -Gdpi=180 -o "$target"
}

render_dot diagrams/ecosystem_context.dot images/ecosystem_context.png
render_dot diagrams/protocol_layers.dot images/protocol_layers.png
render_dot diagrams/worksession_control_flow.dot images/worksession_control_flow.png
render_dot diagrams/zero_trust_gate.dot images/zero_trust_gate.png
render_dot diagrams/evidence_learning_flow.dot images/evidence_learning_flow.png
render_dot diagrams/future_adapter_ecosystem.dot images/future_adapter_ecosystem.png

pandoc jarvis_protocol_architecture_brief.md \
  --standalone \
  --from markdown+raw_html \
  --pdf-engine=weasyprint \
  --css brief.css \
  --metadata title="Jarvis Protocol Architecture Brief" \
  --resource-path=".:images" \
  --output jarvis_protocol_architecture_brief.pdf

echo "Rendered docs/architecture_brief/jarvis_protocol_architecture_brief.pdf"
