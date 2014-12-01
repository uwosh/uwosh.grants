import os, sys
from Products.Archetypes.interfaces.layer import ILayerContainer
from Products.Archetypes.atapi import *
from Products.ATContentTypes.tests.utils import dcEdit
from Products.ATContentTypes.tests.utils import EmptyValidator
from Products.ATContentTypes.tests.utils import EmailValidator

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException
     
class TestUwoshgrantsProposalWorkflow(UwoshgrantsTestCase):
    
    def createProosal(self):
           self.login(self._default_user)

           self.portal.invokeFactory(type_name="Proposal", id="testproposalsubmit")

           return self.portal['testproposalsubmit']
          
    def test_defaults_should_be_correctly_set_and_file_attached(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        pro.invokeFactory(type_name="File", id="10_it_organizations-1.pdf")
        #self.portal_workflow.doActionFor(pro, 'submit')
        #self.portal_workflow.doActionFor(pro, 'sendToGroup')
        
    def test_transition_submit(self):
        #pro = self.createProosal()
        #self.fill_out_proposal(pro)
        #pro.invokeFactory(type_name="File", id="10_it_organizations-1.pdf")
        try:
            self.portal_workflow.doActionFor( pro, 'submit')
            self.assertEquals(True, False)
        except:
            print "submit failed"
            pass

    def test_transition_sendToGroup(self):
        #pro = self.createProosal()
        #self.fill_out_proposal(pro)
        self.login('director1')
        ##pro.invokeFactory(type_name="File", id="10_it_organizations-1.pdf")
        try:
            pro.setFacultyReviewer(['reviewer1','reviewer2'])
            #import pdb;pdb.set_trace()
            self.portal_workflow.doActionFor( pro, 'sendToGroup')
            self.assertEquals(True, False)
        except:
            print "sendToGroup failed"
            #pass
    """
    def test_no_other_roles_should_be_able_to_do_action(self):
        pro = self.createProosal()
        self.login('director1')
        pro.setFacultyReviewer(['Reviewer One','Reviewer Two'])
        self.logout()
        
        for user in self._all_users:
            if user != 'director1':
                self.login(user)
                self.assertRaises(WorkflowException, self.portal_workflow.doActionFor, pro, 'sendToGroup')
                self.logout()
        try:
            self.portal_workflow.doActionFor( pro, 'sendToGroup')
            self.assertEquals(True, False)
        except WorkflowException, e:
            print "sendToGroup failed",e

    def test_transition_sendToPanel(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        self.login('director1')
        #import pdb;pdb.set_trace()
        #pro.invokeFactory(type_name="File", id="10_it_organizations-33.pdf")
        self.login('director1')
        pro.setFacultyReviewer(['Reviewer One','Reviewer Two'])
        self.portal_workflow.doActionFor( pro, 'sendToPanel')

    def test_transition_sendToProposer(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        self.login('director1')
        #pro.invokeFactory(type_name="File", id="10_it_organizations-4.pdf")
        #self.login('director1')
        #pro.setFacultyReviewer([1,2])
        pro.setProposalApproved(True)
        self.portal_workflow.doActionFor( pro, 'sendToProposer')
     
        """     
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestUwoshgrantsProposalWorkflow))

    return suite
    
if  __name__ == '__main__':
    framework()
