# Regional pricing and unit economics

## Analytics patterns

Adapt these patterns to the available analytics schema; verify event names and property types first. Use a consistent window and currency normalization.

```sql
-- acceptance at the purchase dialog
SELECT properties.price, properties.currency,
       count(DISTINCT person_id) AS completed
FROM events
WHERE event = 'subscription_completed'
  AND timestamp >= now() - interval '90 days'
GROUP BY properties.price, properties.currency;
```

Pair completion with a cancellation or dismissal event at the same stage. That ratio describes resolved dialogs only. For completion among all eligible dialog exposures, use the exposure denominator and account for pending or abandoned attempts; deduplicate at a consistent attempt/user unit. Missing events and users who both cancel and later complete can bias naive counts. For geographic conversion, compare paywall views and completed subscriptions by country, acquisition source, plan, currency, and period type.

## Cost-floor model

For each country or region calculate:

- gross price, tax, store/platform fee, refunds, and net revenue
- expected active usage and variable API/compute cost
- support, payment, fraud, and compliance costs
- conversion, retention, and expected lifetime net contribution

Set a floor that remains positive under plausible usage and retention variance. Let local purchasing power influence prices above that floor. A low price can increase taps while reducing dialog completion or attracting high-cost users; evaluate retained contribution rather than install or subscriber counts alone.

## Market comparison

Compare markets using retained subscribers, cohort revenue, churn, payback, and country-level spend where attribution is reliable. Separate currency or tax effects from willingness to pay. Investigate payment rails, local trust, language, and acquisition quality before lowering price in a weak-converting region.

## Safe catalog checks

Before any recommendation involving a promo or retention offer, identify the currently sold offering and exact store product identifier through an approved read-only catalog path. Confirm that the offer belongs to that product and that base and discount points are current. Similar annual or regional SKUs can make a correct write ineffective. Never read service-account files or embed catalog IDs in the skill.

Price writes to App Store, Google Play, a billing provider, or a paywall backend require exact authorization, a provider-supported dry run when available (otherwise validate the proposed change locally), and a post-change readback. Ambiguous responses require state inspection before retrying; do not duplicate a price or offer mutation.
