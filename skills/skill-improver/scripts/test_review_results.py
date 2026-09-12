import copy
import unittest
from review_results import analyze, render


def fixture():
    cases = [dict(id='t', split='train'), dict(id='v', split='validation', critical=True, should_trigger=True), dict(id='n', split='validation', should_trigger=False)]
    runs = [dict(candidate=c, case=k, status='ok', score=s, passed=True, evidence=f'{c}-{k}.txt', triggered=k!='n') for c,s in [('base',.5),('new',.8)] for k in ['t','v','n']]
    return dict(schema_version=1, baseline='base', candidates=['base','new'], min_pairs=2, min_mean_gain=.1, cases=cases, runs=runs)


class ReviewTests(unittest.TestCase):
    def test_paired_gain_and_frontier(self):
        r=analyze(fixture());self.assertEqual(r['candidates'][0]['decision'],'eligible_for_review');self.assertEqual(r['training_frontier'],['new'])
    def test_missing_repeat_not_green(self):
        d=fixture();d['cases'][1]['repetitions']=2
        self.assertEqual(analyze(d)['candidates'][0]['decision'],'inconclusive')
    def test_critical_failure_rejects_despite_gain(self):
        d=fixture();d['runs'][4]['passed']=False
        self.assertEqual(analyze(d)['candidates'][0]['decision'],'reject')
    def test_error_not_zero_or_pass(self):
        d=fixture();d['runs'][4]['status']='error'
        self.assertEqual(analyze(d)['candidates'][0]['decision'],'inconclusive')
    def test_test_set_cannot_select(self):
        d=fixture();before=analyze(d);d['cases'].append(dict(id='sealed',split='test',critical=True,should_trigger=False));d['runs'].append(dict(candidate='new',case='sealed',status='ok',score=0,passed=False,evidence='sealed',triggered=True))
        after=analyze(d);self.assertEqual(before['candidates'],after['candidates']);self.assertEqual(before['trigger_metrics'],after['trigger_metrics']);self.assertEqual(after['test_runs_excluded'],1)
    def test_bad_scores_and_duplicate_rejected(self):
        for score in [float('nan'),float('inf'),True,-1,2]:
            d=fixture();d['runs'][0]['score']=score
            with self.assertRaises(ValueError):analyze(d)
        d=fixture();d['runs'].append(copy.deepcopy(d['runs'][0]))
        with self.assertRaises(ValueError):analyze(d)
    def test_trigger_unknown_and_false_positive(self):
        d=fixture();d['runs'][5]['triggered']=True;del d['runs'][4]['triggered'];r=analyze(d)['trigger_metrics']['new'];self.assertEqual(r['fp'],1);self.assertEqual(r['unknown'],1);self.assertIsNone(r['recall'])
    def test_missing_trigger_observation_blocks_routing_eligibility(self):
        d=fixture();del d['runs'][4]['triggered']
        self.assertEqual(analyze(d)['candidates'][0]['decision'],'inconclusive')
    def test_evidence_required(self):
        d=fixture();d['runs'][0]['evidence']=' '
        with self.assertRaises(ValueError):analyze(d)
    def test_html_escapes_recorded_content(self):
        self.assertNotIn('<script>',render({'candidate':'<script>alert(1)</script>'}))
    def test_missing_cost_disclosed(self):
        r=analyze(fixture())['resource_usage']['new']['cost'];self.assertEqual(r['runs_with_measurement'],0);self.assertEqual(r['recorded_runs'],3)

if __name__=='__main__':unittest.main()
