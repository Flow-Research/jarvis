# Jarvis Protocol Architecture Brief

This folder contains the shareable Jarvis protocol architecture brief.

- Source: [jarvis_protocol_architecture_brief.md](jarvis_protocol_architecture_brief.md)
- PDF: [jarvis_protocol_architecture_brief.pdf](jarvis_protocol_architecture_brief.pdf)
- Render script: [render_pdf.sh](render_pdf.sh)
- Diagram sources: [diagrams/](diagrams/)

The brief packages the v0.1 first-30-days protocol architecture into a PDF the
team reviewed during v0.1 acceptance. It records the OpenAPI contract, examples,
conformance entry, and host-owned adapter boundary.

## Render

```bash
docs/architecture_brief/render_pdf.sh
```

The script renders Graphviz diagram assets into `images/` and then produces
`jarvis_protocol_architecture_brief.pdf`.
