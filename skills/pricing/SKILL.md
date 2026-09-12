---
name: pricing
description: "Use for pricing decisions, packaging, monetization strategy, value metrics, willingness-to-pay research, price changes, and regional or international pricing."
---

# Pricing strategy

Design and evaluate pricing around customer value, adoption, retention, and cost to serve. Reuse supplied context and available evidence; ask only for missing information that materially changes the decision. Establish product type, target segments, go-to-market motion, current plans, alternatives, observed conversion/churn/ARPU, and the business goal. Treat any supplied product context as input; do not assume a particular company, SKU, account, price, or billing provider.

## Three decisions

1. **Packaging**: what each plan includes, limits, support, access, and who it is for.
2. **Value metric**: the unit that scales with customer value and is easy to understand and hard to game.
3. **Price point**: the amount tested against willingness to pay, alternatives, adoption, and sustainable cost to serve.

Use a Good/Better/Best structure only when the tiers represent meaningful customer choices. Differentiate through features, usage, support, access, security, or customization. A cheaper alternative is a reference point, not a price floor: validate willingness to pay, competitive context, retention, and variable costs together.

Load [packaging and offers](references/packaging-and-offers.md) for tier design, personas, freemium/trial choices, enterprise packaging, and subscription or consumable tradeoffs.

## Research and decisions

Use interviews and Van Westendorp or Gabor-Granger surveys for price sensitivity; MaxDiff or conjoint methods for packaging; and usage-to-outcome analysis to identify value thresholds. Segment by persona, use case, geography, and acquisition source. Do not treat survey answers or one conversion snapshot as a final price.

For a price increase, establish a baseline, model new and retained revenue, choose grandfathering or a transition path, communicate the added value, and define a rollback or monitoring plan. Existing customers, renewals, taxes, store rules, and contract terms may require separate treatment.

Load [research and experiments](references/research-and-experiments.md) for study design, demand curves, usage-value analysis, and decision evidence.

## Regional pricing

Use purchasing-power data as a range signal, never as the sole rule. Start with net revenue after platform fees, taxes, refunds, support, and variable compute/API costs. Set a sustainable floor from unit economics, then test regional prices against dialog completion, paywall-to-subscribe, retention, and revenue or ROAS by country. Low acquisition cost or high top-of-funnel volume does not prove a market is profitable.

Verify the live product and offer before discussing a regional change; similar SKUs, currencies, and promotional offers are easy to confuse. Any billing or store price write requires existing user authorization and a provider-supported dry run where available. This skill does not edit billing catalogs, subscriptions, or store prices automatically.

Load [regional pricing](references/regional-pricing.md) for generic event-query patterns, cost-floor modeling, retention analysis, and safe price-change checks.

## Pricing-page audit

When the request is about a pricing page’s clarity or machine readability, score human buyer experience and AI-agent readiness separately. Use rendered text/HTML, a paste test, and a prioritized impact-by-effort fix list. Hand implementation to the appropriate schema, AI-search, CRO, or [$copywriting](../copywriting/SKILL.md) workflow.

Load [pricing page teardown](references/pricing-page-teardown.md) for the ten-dimension rubric and output template.

## Boundaries

Check the actual research, analytics, billing, and store tools available before using them. Use authorized read-only analytics or catalog queries when needed for analysis. Analysis alone does not authorize dependency installation, billing mutations, price changes, experiment launches, or publication. When an action is already authorized, preserve that authorization; otherwise present a concrete proposal and ask for the missing decision at the point of mutation.
