
from Products.CMFCore.utils import getToolByName

def getProposalReviewersVocabulary(self):
    portal_groups = getToolByName(self, 'portal_groups')
    reviewersGroup = portal_groups.getGroupById('uwosh.grants: Reviewers')
    return reviewersGroup.getMemberIds()
