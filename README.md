# Le Duc Tam (tamld) — Personal Portfolio & LLM-Agent Endpoint

> Production static site and machine-readable LLM endpoint deployed on GitHub Pages at **https://tamld.github.io/**.

## 🚀 Features
- **Anti-AI-Slop Engineering**: High-contrast, tactile dark-tech aesthetic (Inter/Geist + JetBrains Mono) without generic purple gradients or marketing fluff.
- **Dual-Track Competency**: 11+ years of bare-metal enterprise IT operations & infrastructure paired with AI Systems Engineering & Agentic Harnesses.
- **Interactive Terminal Widget**: Client-side Vanilla JS terminal simulator (`tamld --whoami`, `tamld --skills`, `tamld --homelab`, `tamld --projects`).
- **Machine-Readable Standard (`llms.txt`)**: Fully compliant with [llmstxt.org](https://llmstxt.org/) specification for zero-overhead LLM / AI Agent context ingestion.
- **Zero-Build & Zero-Dependency**: Single-file HTML5 + Tailwind CSS CDN, sub-100ms FCP, zero npm dependencies, hosted on GitHub Pages CDN.

## 📂 Key Files
- `index.html`: Main visual portfolio interface.
- `llms.txt`: Curated markdown summary and index for AI agents (`https://tamld.github.io/llms.txt`).
- `llms-full.txt`: Comprehensive single-file technical dossier and career history (`https://tamld.github.io/llms-full.txt`).
- `.nojekyll`: Disables Jekyll parsing on GitHub Pages.

## 🌐 Machine Consumption
Any LLM or autonomous agent can fetch Tam's verified profile directly via:
```bash
curl -sL https://tamld.github.io/llms.txt
```
or for the full dossier:
```bash
curl -sL https://tamld.github.io/llms-full.txt
```

---
© 2026 Le Duc Tam (tamld).
