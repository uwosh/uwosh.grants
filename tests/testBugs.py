
from Testing import ZopeTestCase # side effect import. leave it here.
from Products.ATContentTypes.tests import atcttestcase
from Products.validation.interfaces.IValidator import IValidationChain
from Products.ATContentTypes.content.schemata import ATContentTypeSchema

from Products.Archetypes.atapi import *

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException

class TestBugs(UwoshgrantsTestCase):

    def test_wfmapping(self):
        pfwf = ('uwosh_grants_proposal_workflow',)
        rfwf = ('uwosh_grants_review_workflow',)

        mapping = {
            'Proposal' : pfwf,
            'ReviewerForm' : rfwf,
            'ReviewerFormGrad' : rfwf,
            'File' : (),

            }
        """
        for pt, wf in mapping.items():
            pwf = self.wf.getChainFor(pt)
            self.failUnlessEqual(pwf, wf, (pt, pwf, wf))
        """
    def test_striphtmlbug(self):
        self.login(self._default_user)
        self.folder.invokeFactory('Proposal', 'proposal1')
        p = getattr(self.folder, 'proposal1')
        p.setTitle("HTML end tags start with </ and end with >")
        self.assertEqual(p.Title(), "HTML end tags start with </ and end with >")
        """
        self.folder.invokeFactory('ReviewerForm', 'reviewerform1')
        rug = getattr(self.folder, 'reviewerform1')
        rug.setTitle("HTML end tags start with </ and end with >")
        self.assertEqual(rug.Title(), "HTML end tags start with </ and end with >")
        self.folder.invokeFactory('ReviewerFormGrad', 'reviewerformgrad1')
        rg = getattr(self.folder, 'reviewerformgrad1')
        rg.setTitle("HTML end tags start with </ and end with >")
        self.assertEqual(rg.Title(), "HTML end tags start with </ and end with >")
        """
    def test_validation_layer_from_id_field_from_base_schema_was_initialized(self):
        field = ATContentTypeSchema['id']
        self.failUnless(IValidationChain.isImplementedBy(field.validators))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestBugs))

    return suite
    
if  __name__ == '__main__':
    framework()
