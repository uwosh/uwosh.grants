# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """T. Kim Nguyen <nguyen@uwosh.edu> <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('uwosh_grants: setuphandlers')
from Products.uwosh_grants.config import PROJECTNAME
from Products.uwosh_grants.config import DEPENDENCIES
import os
from config import product_globals
from Globals import package_home
from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotuwosh_grantsProfile(context):
    return context.readDataFile("uwosh_grants_marker.txt") is None

def installVocabularies(context):
    """creates/imports the atvm vocabs."""
    if isNotuwosh_grantsProfile(context): return 
    site = context.getSite()
    # Create vocabularies in vocabulary lib
    atvm = getToolByName(site, ATVOCABULARYTOOL)
    vocabmap = {'ReviewFormResponseHolistic': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'ReviewFormResponse': ('VdexVocabulary', 'SimpleVocabularyTerm'),
         'YesNoNA': ('SimpleVocabulary', 'SimpleVocabularyTerm'),
        }
    for vocabname in vocabmap.keys():
        if not vocabname in atvm.contentIds():
            atvm.invokeFactory(vocabmap[vocabname][0], vocabname)

        if len(atvm[vocabname].contentIds()) < 1:
            if vocabmap[vocabname][0] == "VdexVocabulary":
                vdexpath = os.path.join(
                    package_home(product_globals), 'data', '%s.vdex' % vocabname)
                if not (os.path.exists(vdexpath) and os.path.isfile(vdexpath)):
                    logger.warn('No VDEX import file provided at %s.' % vdexpath)
                    continue
                try:
                    #read data
                    f = open(vdexpath, 'r')
                    data = f.read()
                    f.close()
                except:
                    logger.warn("Problems while reading VDEX import file "+\
                                "provided at %s." % vdexpath)
                    continue
                # this might take some time!
                atvm[vocabname].importXMLBinding(data)
            else:
                pass



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotuwosh_grantsProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotuwosh_grantsProfile(context): return
    site = context.getSite()
    # add related groups
    pg = site.portal_groups
    allGroups = pg.getGroupIds()
    for g in ('uwosh.grants: Reviewers', 'uwosh.grants: Directors', 'uwosh.grants: Panel',
              'uwosh.grants: Proposers', 'uwosh.grants: ActiveReviewers'):
        if (g not in allGroups):
            pg.addGroup(g)
    # add users who will own proposals and review forms to obscure true ownership
    pr = site.portal_registration
    pm = site.portal_membership
    pw = site.portal_workflow
    for u in ('Proposer', 'Reviewer', ):
        if (not pm.getMemberInfo(u)):
            pr.addMember(u, pr.getPassword(length=25))
    pg.setRolesForGroup('uwosh.grants: Reviewers', ['uwosh.grants.reviewer',])
    pg.setRolesForGroup('uwosh.grants: Directors', ['uwosh.grants.director',])
    pg.setRolesForGroup('uwosh.grants: Panel', ['uwosh.grants.panel',])
    pg.setRolesForGroup('Faculty', ['uwosh.grants.faculty',])

    pg.addPrincipalToGroup ('Reviewer', 'uwosh.grants: Reviewers')
    """
    grants-welcome = getattr(site , 'grants-welcome')
    proposals = getattr(site , 'proposals')
    if pw.getInfoFor(grants-welcome, 'review_state') != 'published':
            pw.doActionFor(grants-welcome, 'publish')
    if pw.getInfoFor(proposals, 'review_state') != 'published':
            pw.doActionFor(proposals, 'publish')
    """
##code-section FOOT
##/code-section FOOT
