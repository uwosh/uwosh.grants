import os, sys
from Products.Archetypes.interfaces.layer import ILayerContainer
from Products.Archetypes.atapi import *
from Products.ATContentTypes.tests.utils import dcEdit
from Products.ATContentTypes.tests.utils import EmptyValidator
from Products.ATContentTypes.tests.utils import EmailValidator
from Products.ATContentTypes.tests.utils import NotRequiredTidyHTMLValidator

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException
     
class TestUwoshgrantsProposalFields(UwoshgrantsTestCase):
    
    def createProosal(self):
           self.login(self._default_user)

           self.portal.invokeFactory(type_name="Proposal", id="testproposalsubmit")

           return self.portal['testproposalsubmit']

    def test_proposerNameField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('proposerName')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getProposerName',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setProposerName',
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
        #self.failUnless(field.validators == EmptyValidator,
        #                'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))    
             
    def test_proposerIdField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('proposerId')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 1, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getProposerId',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setProposerId',
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
        #self.failUnless(field.validators == EmptyValidator,
        #                'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))    
             

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

    def test_primaryFacultyAdvisorNameField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('primaryFacultyAdvisorName')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 1, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getPrimaryFacultyAdvisorName',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setPrimaryFacultyAdvisorName',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == 'View',
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        'uwosh_grants: View faculty advisers',
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
        #self.failUnless(field.validators == EmptyValidator,
        #                'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))   

    def test_FacultyAdvisor2NameField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('facultyAdvisor2Name')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getFacultyAdvisor2Name',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setFacultyAdvisor2Name',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == 'View',
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        'uwosh_grants: View faculty advisers',
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
        self.failUnless(field.validators == EmptyValidator,
                        'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))      

    def test_FacultyAdvisor3NameField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('facultyAdvisor3Name')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getFacultyAdvisor3Name',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setFacultyAdvisor3Name',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == 'View',
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        'uwosh_grants: View faculty advisers',
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
        self.failUnless(field.validators == EmptyValidator,
                        'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, StringWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab))) 
                
    def test_abstractField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        #dummy = self._dummy
        field = pro.getField('abstract')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (),
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getAbstract',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setAbstract',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == 'View',
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        'Modify portal content',
                        'Value is %s' % field.write_permission)
        self.failUnless(field.generateMode == 'veVc',
                        'Value is %s' % field.generateMode)
        self.failUnless(field.force == '', 'Value is %s' % field.force)
        self.failUnless(field.type == 'text', 'Value is %s' % field.type)
        self.failUnless(isinstance(field.storage, AttributeStorage),
                        'Value is %s' % type(field.storage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage(),
                        'Value is %s' % field.getLayerImpl('storage'))
        self.failUnless(ILayerContainer.isImplementedBy(field))
        #self.failUnless(field.validators == NotRequiredTidyHTMLValidator,
        #                'Value is %s' % repr(field.validators))
        self.failUnless(isinstance(field.widget, RichWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(pro)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))

        self.failUnless(field.primary == 0, 'Value is %s' % field.primary)
        self.failUnless(field.default_content_type is None,
                        'Value is %s' % field.default_content_type)
        self.failUnless(field.default_output_type == 'text/html',
                        'Value is %s' % field.default_output_type)
        self.failUnless('text/html' in field.getAllowedContentTypes(pro))

    def test_facultyReviewerField(self):
        pro = self.createProosal()
        self.fill_out_proposal(pro)
        field = pro.getField('facultyReviewer')
        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0, 'Value is %s' % field.required)
        #self.failUnless(field.default == (), 'Value is %s' % str(str(field.default)))
        self.failUnless(field.searchable == 0, 'Value is %s' % field.searchable)
        self.failUnless(field.enforceVocabulary == 0,
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getFacultyReviewer',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setFacultyReviewer',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == 'View',
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        'uwosh_grants: Set reviewer permission',
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
        self.failUnless(field.validators == EmptyValidator,
                        'Value is %s' % repr(field.validators))
        self.failUnless(isinstance(field.widget, MultiSelectionWidget),
                        'Value is %s' % id(field.widget))
           
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestUwoshgrantsProposalFields))

    return suite
    
if  __name__ == '__main__':
    framework()
