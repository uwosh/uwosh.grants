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
     
class TestUwoshgrantsProposalSubmitWithFile(UwoshgrantsTestCase):
    
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
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        pro.invokeFactory(type_name="File", id="10_it_organizations-1.pdf")
        try:
            self.portal_workflow.doActionFor( app, 'submit')
            self.assertEquals(True, False)
        except:
            pass

    def test_transition_sendToGroup(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        pro.invokeFactory(type_name="File", id="10_it_organizations-1.pdf")
        try:
            self.portal_workflow.doActionFor( app, 'sendToGroup')
            self.assertEquals(True, False)
        except:
            pass

    def test_no_other_roles_should_be_able_to_do_action(self):
        pro = self.createProosal()
        self.login('director1')
        pro.setFacultyReviewer([1,2])
        self.logout()
        
        for user in self._all_users:
            if user != 'director1':
                self.login(user)
                self.assertRaises(WorkflowException, self.portal_workflow.doActionFor, pro, 'sendToGroup')
                self.logout()
        try:
            self.portal_workflow.doActionFor( app, 'sendToGroup')
            self.assertEquals(True, False)
        except:
            pass



    def test_proposerEmailField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('proposerEmail')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 0, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getProposerEmail',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setProposerEmail',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == 'View',
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        'uwosh_grants: View proposer details',
                        'Value is %s' % field.write_permission)
        self.failUnless(field.generateMode == 'veVc',
                        'Value is %s' % field.generateMode)
        self.failUnless(field.force == '', 'Value is %s' % field.force)
        self.failUnless(field.type == 'string', 'Value is %s' % field.type)
        self.failUnless(isinstance(field.storage, AttributeStorage),
                        'Value is %s' % type(field.storage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage(),
                        'Value is %s' % field.getLayerImpl('storage'))
        self.failUnless(ILayerContainer.isImplementedBy(field))
        #self.failUnless(field.validators == ('isEmail',1),
        #                'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))          
             
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestUwoshgrantsProposalSubmitWithFile))

    return suite
    
if  __name__ == '__main__':
    framework()
