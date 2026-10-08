# Le Duc Tam (tamld) — Personal Portfolio & LLM-Agent Endpoint

> Production static site and machine-readable LLM endpoint deployed on GitHub Pages at **https://tamld.github.io/**.

## 🚀 Features
- **Anti-AI-Slop Engineering**: High-contrast, tactile dark-tech aesthetic (Inter/Geist + JetBrains Mono) without generic purple gradients or marketing fluff.
- **Dual-Track Competency**: 11+ years of bare-metal enterprise IT operations & infrastructure paired with AI Systems Engineering & Agentic Harnesses.
- **Interactive Terminal Widget**: Client-side Vanilla JS terminal simulator (`tamld --whoami`, `tamld --skills`, `tamld --homelab`, `tamld --projects`).
- **Machine-Readable Standard (`llms.txt`)**: Fully compliant with [llmstxt.org](https://llmstxt.org/) specification for zero-overhead LLM / AI Agent context ingestion.
- **Zero-Build & Zero-CDN Icons**: Standalone single-file HTML5 with self-contained inline SVG sprites, Schema.org JSON-LD entity graph, sub-100ms FCP, and zero external icon CDN dependencies.
- **Decoupled SRE Telemetry**: Live machine-readable JSON telemetry feed (`/data/telemetry.json`) consumed by terminal emulator commands.

## 📂 Key Files
- `index.html`: Main visual portfolio interface with Schema.org JSON-LD and self-contained SVGs.
- `data/telemetry.json`: Sanitized bare-metal homelab SRE telemetry snapshot (`https://tamld.github.io/data/telemetry.json`).
- `llms.txt`: Curated markdown summary and index for AI agents (`https://tamld.github.io/llms.txt`).
- `llms-full.txt`: Comprehensive single-file technical dossier and career history (`https://tamld.github.io/llms-full.txt`).
- `.nojekyll`: Disables Jekyll parsing on GitHub Pages.
- `.githooks/pre-commit`: Deterministic git hook preventing gradients, blur, and persona hallucinations.

## 🌐 Machine Consumption
Any LLM, scraper, or autonomous agent can query Tam's verified profile directly via:
```bash
# Curated LLM index
curl -sL https://tamld.github.io/llms.txt

# Full engineering dossier
curl -sL https://tamld.github.io/llms-full.txt

# Live homelab SRE telemetry
curl -sL https://tamld.github.io/data/telemetry.json
```

---
© 2026 Le Duc Tam (tamld).
