
# Import the base test case classes
from Testing import ZopeTestCase
from Products.CMFPlone.tests import PloneTestCase
from unittest import TestCase, TestSuite, makeSuite, main
from Products.CMFCore.WorkflowCore import WorkflowException

# HACK: Explicitly import zcml to make roadrunner work
def isTestrunnerRoadrunner():
    from sys import argv
    for arg in argv:
        if 'roadrunner' in arg:
            return True
    return False

if isTestrunnerRoadrunner():
    from Products.Five import zcml
    from Products.Five import fiveconfigure
    import Products.uwosh_grants
    import Products.ATVocabularyManager

    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', Products.uwosh_grants)
    zcml.load_config('configure.zcml', Products.ATVocabularyManager)
    fiveconfigure.debug_mode = False


# These must install cleanly
ZopeTestCase.installProduct('ATVocabularyManager')
ZopeTestCase.installProduct('uwosh_grants')

# Set up the Plone site used for the test fixture. The PRODUCTS are the products
# to install in the Plone site (as opposed to the products defined above, which
# are all products available to Zope in the test fixture)
PRODUCTS = ['ATVocabularyManager', 'uwosh_grants']
PloneTestCase.setupPloneSite(products=PRODUCTS)

class UwoshgrantsTestCase(PloneTestCase.PloneTestCase):
    """
    Base
    """
    _oie_users = { 'director1':['uwosh.grants.director'],
                   'director2':['uwosh.grants.director'],
                   'panel1':['uwosh.grants.panel'],
                   'panel2':['uwosh.grants.panel'],
                   'reviewer1':['uwosh.grants.reviewer'],
                   'reviewer2':['uwosh.grants.reviewer'],
                   'reviewer3':['uwosh.grants.reviewer'],
                   'proposer2':['Member'], 
                   'proposer3':['Member'] 
                   }
    
    _default_user = 'proposer1'
    
    _all_users = _oie_users.keys() + [_default_user]
    _default_program = None
    
    def afterSetUp(self):
        self.acl_users = self.portal.acl_users
        self.portal_workflow = self.portal.portal_workflow
        self.portal_registration = self.portal.portal_registration
        
        #self.mockMailHost()
        self.setDefaultProgram()
        self.createUsers()
        
        self.login()
        self.setRoles(('Manager', 'Owner'))
        #create_settings_documents(settings_folder, self.portal)
        self.logout()
        
    def setDefaultProgram(self):
        self.login()
        self.setRoles(('Manager', 'Owner'))
        
        programId = self.portal.invokeFactory(type_name='Proposal', 
                                              id=self.portal.generateUniqueId(), 
                                              title="testproposal")
        
        self._default_program = self.portal[programId]
        self.logout()

    def createUsers(self):
        self.login()
        self.setRoles(('Manager', 'Owner'))
         
        self.portal.acl_users._doAddUser(self._default_user, 'password', ['Member', 'Owner', 'uwosh.grants.faculty'], [])
        self.portal.portal_membership.getMemberById(self._default_user).setMemberProperties({'email': self._default_user + '@uwoshgrants.com'})
        
        for user, roles in self._oie_users.iteritems():
            self.portal.acl_users._doAddUser(user, 'password', roles, [])
            self.portal.portal_membership.getMemberById(user).setMemberProperties({'email': user + '@uwoshgrants.com'})
        
        self.logout()
              
    def assertHasTheseRoles(self, transition, roles):
        map(lambda role: self.failUnless(role in roles ), transition.getGuard().roles)
        self.failUnless(len(roles) == len(transition.getGuard().roles))
        
    def hasTheseTransitions(self, state, desiredTransitions):
        map(lambda transition: self.failUnless(transition in desiredTransitions ), state.getTransitions())
        self.failUnless(len(desiredTransitions) == len(state.getTransitions()))

    def hasPermissionRoles(self, state, permission, desired_roles):
        for role in state.getPermissionInfo(permission)['roles']:
            self.failUnless(role in desired_roles)
    
    def fill_out_proposal(self, pro):
        pro.setTitle('Test Proposal')
        pro.setProposerName("John Dorapalli")
        pro.setProposerId("johnd")
        pro.setProposerEmail("johnd@gmail.com")
        pro.setPrimaryFacultyAdvisorName("John AAA")
        pro.setFacultyAdvisor2Name("John BBB")
        pro.setAbstract("Doe version and work on it some more later use the button at the bottom of this form. Once you have saved this form a number of green tabs will appear above. To make changes click on the tab. With the green tabs showing you can also submit by selecting in the green  menu.version and work on it some more later use the button at the bottom of this form. Once you have saved this form a number of green tabs will appear above. To make changes click on the tab. With the")
        pro.setStudentIsPrimaryAuthor(True)
   
    def getState(self, obj):
        return self.portal_workflow.getInfoFor(obj, 'review_state', None)
        

class UwoshgrantsFunctionalTestCase(UwoshgrantsTestCase, PloneTestCase.FunctionalTestCase):
    pass


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(UwoshgrantsTestCase))
    return suite
    
if __name__ == '__main__':
    framework()
