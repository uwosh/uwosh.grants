import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException


class TestInstallation(UwoshgrantsTestCase):
    """Ensure product is properly installed"""

    def afterSetUp(self):
        self.css        = self.portal.portal_css
        self.kupu       = self.portal.kupu_library_tool
        self.skins      = self.portal.portal_skins
        self.types      = self.portal.portal_types
        self.factory    = self.portal.portal_factory
        self.workflow   = self.portal.portal_workflow
        self.properties = self.portal.portal_properties

    def test_added_workflow(self):
        ids = self.portal.portal_workflow.objectIds()
        self.failUnless('uwosh_grants_proposal_workflow' in ids)
        self.failUnless('uwosh_grants_review_workflow' in ids)
        
    def test_roles_added(self):
        pass
        
class TestUwoshgrantsProposal(UwoshgrantsTestCase):
    
    def createProosal(self):
           self.login(self._default_user)

           self.portal.invokeFactory(type_name="Proposal", id="testproposal")

           return self.portal['testproposal']
          
    def test_defaults_should_be_correctly_set(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #self.portal_workflow.doActionFor(pro, 'submit')
        
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestInstallation))
    suite.addTest(makeSuite(TestUwoshgrantsProposal))

    return suite
    
if  __name__ == '__main__':
    framework()
