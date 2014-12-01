
from Products.CMFCore.utils import getToolByName

def validateSubmit(obj, event):
    if not event.transition or \
       event.transition.id not in ['submit']:
        return
    containedItems = obj.listFolderContents()
    if len(containedItems) < 1:
        from Products.CMFCore.utils import getToolByName
        putils = getToolByName(obj, 'plone_utils')
        putils.addPortalMessage(u'You did not attach a proposal document. Please use browser back button, edit the proposal and select the faculty reviewers to review the proposal.','error')
        obj.REQUEST.RESPONSE.redirect('/proposal_member_view') 
        raise ValueError, "You did not attach a proposal document"
        #from Products.statusmessages.interfaces import IStatusMessage
        #status=IStatusMessage(self.request)
        #request = obj.REQUEST
        #IStatusMessage(request).addStatusMessage("You did not attach a proposal document", type="error")
        #return IStatusMessage(request).showStatusMessages()
        #from Products.CMFPlone import PloneMessageFactory as _
        #context=self.context
        #RESPONSE = context.REQUEST.RESPONSE
        #context.plone_utils.addPortalMessage(_(u'You did not attach a proposal document.'))
        #raise ValueError, "You did not attach a proposal document"


def postSubmit(obj, event):
    if not event.transition or \
       event.transition.id not in ['submit']:
        return
    user = obj.portal_membership.getMemberById('Proposer')
    obj.changeOwnership(user, recursive=1)
    #import pdb;pdb.set_trace()
    obj.setCreators(['Proposer',])
    for child in obj.objectValues():
        child.setCreators(['Proposer',])
        child.reindexObject()

def validateSendToGroup(obj, event):
    if not event.transition or \
       event.transition.id not in ['sendToGroup']:
        return
    reviewers = obj.getFacultyReviewer()
    if len(reviewers) == 0:
        from Products.CMFCore.utils import getToolByName
        putils = getToolByName(obj, 'plone_utils')
        putils.addPortalMessage(u'You did not set faculty reviewers. Please use browser back button and Submit after attaching the document.','error')
        raise ValueError, "You did not set any faculty reviewers"

def create_review_forms(obj, event):
    if not event.transition or \
       event.transition.id not in ['sendToGroup']:
        return
    reviewers = obj.getFacultyReviewer()
    count = 1
    for r in reviewers:
        if r <> '':
            
            if obj.uwosh_grants_default_type == 'GraduateProposal':
                id = obj.generateUniqueId('ReviewerFormGrad')
                newFormId = obj.invokeFactory(type_name="ReviewerFormGrad", id=id)
            if obj.uwosh_grants_default_type == 'UnderGraduateProposal':
                id = obj.generateUniqueId('ReviewerForm')
                newFormId = obj.invokeFactory(type_name="ReviewerForm", id=id)
            newForm = getattr(obj, newFormId)
            newForm.setTitle('Review Form - '+str(count))
            count = count + 1
            newForm.setReviewer(r)
            newForm.setCreators(['Reviewer',r,])
	    user = obj.portal_membership.getMemberById(r)
	    newForm.changeOwnership(user)
            #newForm.__ac_local_roles__ = None
            newForm.manage_setLocalRoles(user.getId(), ['Owner'])
            newForm.reindexObject()
            obj.portal_groups.addPrincipalToGroup(r, 'uwosh.grants: ActiveReviewers')

def validatesendToProposer(obj, event):
    if not event.transition or \
       event.transition.id not in ['sendToProposer']:
        return
    approved = obj.getProposalApproved()
    if approved == '':
        from Products.CMFCore.utils import getToolByName
        putils = getToolByName(obj, 'plone_utils')
        putils.addPortalMessage(u'You did not Approve/Reject the Proposal. Please use browser back button, edit the Proposal and select one among the    options.','error')
        raise ValueError, "You did not approve the proposal"

def validateFile(self):
    from Products.CMFCore.utils import getToolByName
    from Products.CMFPlone import PloneMessageFactory as _
    plone_utils = getToolByName(self,'plone_utils')
    plone_utils.addPortalMessage(_(u'Please correct the indicated errors.'))
    return state.set(status='failure')

#retrieve children objects
def transitionChildrenObjects(obj, event):
    if not event.transition or \
       event.transition.id in ['submit','sendToGroup']:
        return

    children = obj.ZopeFind(event.object, search_sub=1)
    wftool = obj.portal_workflow

    #loop through the children objects
    for _, sobj in children:
    #transition each object
        if not sobj.portal_type in ['File']:
            wftool.doActionFor(sobj, event.transition.id)

def addProposerToProposersGroup(obj, event):
    portal_groups = getToolByName(obj, 'portal_groups')
    portal_membership = getToolByName(obj, 'portal_membership')
    member = portal_membership.getAuthenticatedMember()
    if 'uwosh.grants: Proposers' not in member.getGroups():
        portal_groups.addPrincipalToGroup(member.getUserName(), 'uwosh.grants: Proposers')
