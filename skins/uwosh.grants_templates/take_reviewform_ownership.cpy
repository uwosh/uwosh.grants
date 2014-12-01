## Controller Python Script "take_reviewform_ownership"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

containedItems = context.listFolderContents()

for ci in containedItems:
    if ci.portal_type=='ReviewerForm':
        r=ci.getReviewer()
        user = context.portal_membership.getMemberById(r)
        #print user
        #return printed
        ci.setCreators(['Reviewer',r,])
        #ci.changeOwnership(user)
        #newForm.__ac_local_roles__ = None
        ci.manage_setLocalRoles(user.getId(), ['Owner'])
        ci.reindexObject()
        context.portal_groups.addPrincipalToGroup(r, 'uwosh.grants: ActiveReviewers')

    if ci.portal_type=='ReviewerFormGrad':
        r=ci.getReviewer()
        user = context.portal_membership.getMemberById(r)
        #print user
        #return printed
        ci.setCreators(['Reviewer',r,])
        #ci.changeOwnership(user)
        ci.manage_setLocalRoles(user.getId(), ['Owner'])
        ci.reindexObject()
        context.portal_groups.addPrincipalToGroup(r, 'uwosh.grants: ActiveReviewers')
