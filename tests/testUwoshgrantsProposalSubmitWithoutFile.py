import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException
     
class TestUwoshgrantsProposalSubmitWithoutFile(UwoshgrantsTestCase):
    
    def createProosal(self):
           self.login(self._default_user)

           self.portal.invokeFactory(type_name="Proposal", id="testproposalsubmit")

           return self.portal['testproposalsubmit']
          
    def test_defaults_should_be_correctly_set(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #pro.invokeFactory(type_name="File", id="10_it_organizations-1.pdf")
        try:
            self.portal_workflow.doActionFor(pro, 'submit')
            self.assertEquals(True, False)
        except:
            pass    
        #self.assertEquals('directorReview', self.getState(pro))
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestUwoshgrantsProposalSubmitWithoutFile))

    return suite
    
if  __name__ == '__main__':
    framework()
