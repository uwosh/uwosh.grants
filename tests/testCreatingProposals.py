
from Testing import ZopeTestCase # side effect import. leave it here.
from Products.ATContentTypes.tests import atcttestcase
from Products.validation.interfaces.IValidator import IValidationChain
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.Five.testbrowser import Browser

from Products.Archetypes.atapi import *

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsFunctionalTestCase
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFCore.utils import getToolByName

class TestCreatingProposals(UwoshgrantsFunctionalTestCase):

    def _createProposal(self):
        self.login(self._default_user)
        id = self.folder.invokeFactory(type_name='Proposal', id='test-proposal')
        return self.folder[id]

    def _loginThroughBrowserAsDefaultUser(self):
        self.browser = Browser()
        self.browser.open(self.portal.absolute_url() + '/login_form')
        self.browser.getControl(name='__ac_name').value = self._default_user
        self.browser.getControl(name='__ac_password').value = 'password'
        self.browser.getControl(name='submit').click()
        self.assertTrue('You are now logged in' in self.browser.contents)

    def _createFillOutAndSubmitAProposal(self):
        self.browser.open(self.portal.absolute_url() + '/proposals/createObject?type_name=Proposal')
        self.browser.getControl('Title').value = 'Test Proposal'
        self.browser.getControl('Proposer Name').value = 'John Doe'
        self.assertEqual(self.browser.getControl('Proposer ID').value, self._default_user)
        self.browser.getControl('Proposer Email').value = 'jdoe@uwosh.edu'
        self.browser.getControl('Primary Faculty Advisor Name').value = 'Douglas Adams'
        self.browser.getControl('Save').click()

    def testUserIsAddedToTheProposersGroup(self):
        portal_membership = getToolByName(self.portal, 'portal_membership')
        member = portal_membership.getMemberById(self._default_user)
        self.assertEqual(sorted(member.getGroups()), ['AuthenticatedUsers'])
        self._loginThroughBrowserAsDefaultUser()
        self._createFillOutAndSubmitAProposal()
        member = portal_membership.getMemberById(self._default_user)
        self.assertEqual(sorted(member.getGroups()), ['AuthenticatedUsers', 'uwosh.grants: Proposers'])
        
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestCreatingProposals))

    return suite
    
if  __name__ == '__main__':
    framework()
