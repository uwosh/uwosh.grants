from Testing import ZopeTestCase # side effect import. leave it here.
import os, sys
from Products.Archetypes.interfaces.layer import ILayerContainer
from Products.Archetypes.atapi import *
from Products.ATContentTypes.tests.utils import dcEdit
from Products.ATContentTypes.tests.utils import EmptyValidator
from Products.ATContentTypes.tests.utils import EmailValidator
from Products.ATContentTypes.tests.utils import NotRequiredTidyHTMLValidator
"""
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))
"""
from uwoshgrantstestcase import UwoshgrantsTestCase
from Products.CMFCore.WorkflowCore import WorkflowException
from DateTime import DateTime
import Missing

class TestFormatCatalogMetadata(UwoshgrantsTestCase):

    def afterSetUp(self):
        self.script = self.portal.formatCatalogMetadata        

    def testFormatDate(self):
        date = '2005-11-02 13:52:25'
        format = '%m-%d-%Y %I:%M %p'
        self.portal.portal_properties.site_properties.manage_changeProperties(
                            localLongTimeFormat='%m-%d-%Y %I:%M %p')
        self.assertEqual(self.script(date),
                         DateTime(date).strftime(format))
        self.assertEqual(self.script(DateTime(date)),
                         DateTime(date).strftime(format))

    def testFormatDict(self):
        self.assertEqual(self.script({'a':1,'b':2}), 'a: 1, b: 2')

    def testFormatList(self):
        self.assertEqual(self.script(('a','b',1,2,3,4)), 'a, b, 1, 2, 3, 4')
        self.assertEqual(self.script(['a','b',1,2,3,4]), 'a, b, 1, 2, 3, 4')
        # this also needs to be able to handle unicode that won't encode to ascii
        ustr = 'i\xc3\xadacute'.decode('utf8')
        self.assertEqual(self.script(['a','b',ustr]), 'a, b, i\xc3\xadacute'.decode('utf8'))

    def testFormatString(self):
        self.assertEqual(self.script('fkj dsh ekjhsdf kjer'), 'fkj dsh ekjhsdf kjer')

    def testFormatTruncates(self):
        self.portal.portal_properties.site_properties.manage_changeProperties(
                            search_results_description_length=12, ellipsis='???')
        self.assertEqual(self.script('fkj dsh ekjhsdf kjer'), 'fkj dsh ekjh???')

    def testFormatStrange(self):
        self.assertEqual(self.script(None), '')
        self.assertEqual(self.script(Missing.Value()), '')

    def testUnicodeValue(self):
        """ Make sure non-ascii encodable unicode is acceptable """
        
        ustr = 'i\xc3\xadacute'.decode('utf8')
        self.assertEqual(self.script(ustr), ustr)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestFormatCatalogMetadata))
    return suite
    
if  __name__ == '__main__':
    framework()

