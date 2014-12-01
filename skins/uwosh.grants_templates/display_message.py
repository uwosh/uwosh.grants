## Script (Python) "take_reviewform_ownership"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

from Products.CMFCore.utils import getToolByName
putils = getToolByName(context, 'plone_utils')
putils.addPortalMessage(u'Added Ownership','error')

