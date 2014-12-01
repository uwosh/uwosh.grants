
from Testing import ZopeTestCase # side effect import. leave it here.
from Products.ATContentTypes.tests import atcttestcase
from Products.validation.interfaces.IValidator import IValidationChain
from Products.ATContentTypes.content.schemata import ATContentTypeSchema

from Products.Archetypes.atapi import *

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException

class TestDynamicVocabularies(UwoshgrantsTestCase):

    def createProposal(self):
        self.login(self._default_user)
        id = self.folder.invokeFactory(type_name='Proposal', id='test-proposal')
        return self.folder[id]

    def createReviewerForm(self, proposal):
        self.portal.portal_groups.addPrincipalToGroup(self._default_user, 'uwosh.grants: Directors')
        self.login(self._default_user)
        id = proposal.invokeFactory(type_name='ReviewerForm', id='test-reviewerform')
        return proposal[id]

    def createReviewerFormGrad(self, proposal):
        self.portal.portal_groups.addPrincipalToGroup(self._default_user, 'uwosh.grants: Directors')
        self.login(self._default_user)
        id = proposal.invokeFactory(type_name='ReviewerFormGrad', id='test-reviewerformgrad')
        return proposal[id]

    def testGetProposalReviewersVocabulary(self):
        from Products.uwosh_grants.content.common import getProposalReviewersVocabulary
        self.assertEqual(getProposalReviewersVocabulary(self.portal), ['Reviewer'])

    def testProposalFacultyReviewerField(self):
        proposal = self.createProposal()
        self.assertEqual(proposal.getField('facultyReviewer').vocabulary, 'getProposalReviewersVocabulary')
        self.assertEqual(proposal.getProposalReviewersVocabulary(), ['Reviewer'])

    def testReviewerFormReviewerField(self):
        proposal = self.createProposal()
        reviewerForm = self.createReviewerForm(proposal)
        self.assertEqual(reviewerForm.getField('reviewer').vocabulary, 'getProposalReviewersVocabulary')
        self.assertEqual(reviewerForm.getProposalReviewersVocabulary(), ['Reviewer'])

    def testReviewerFormGradReviewerField(self):
        proposal = self.createProposal()
        reviewerFormGrad = self.createReviewerFormGrad(proposal)
        self.assertEqual(reviewerFormGrad.getField('reviewer').vocabulary, 'getProposalReviewersVocabulary')
        self.assertEqual(reviewerFormGrad.getProposalReviewersVocabulary(), ['Reviewer'])


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestDynamicVocabularies))

    return suite
    
if  __name__ == '__main__':
    framework()
