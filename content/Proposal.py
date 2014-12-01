# -*- coding: utf-8 -*-
#
# File: Proposal.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
# modified by J.H. Gutow <gutow@uwosh.edu> 10/2009
#

__author__ = """T. Kim Nguyen <nguyen@uwosh.edu> <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.uwosh_grants.config import *
from common import getProposalReviewersVocabulary

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.image import ATImage
from Products.ATContentTypes.content.file import ATFile
from Products.ATVocabularyManager import NamedVocabulary
from ReadOnlyRichWidget import *

import logging

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='instructions',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default="""STEP 1: Fill out the information below and click on the "Save" button at the
	bottom. Step 2: will be to upload the proposal.  Step 3: will be to submit the proposal.
	Additional details and help are available at right.<br><br>""",
        widget=ReadOnlyRichWidget(
            label='Instructions',
            label_msgid='uwosh_grants_label_instructions',
            i18n_domain='uwosh_grants',
        ),
        default_output_type='text/html',
        modify="Manager",
	read_permission="uwosh_grants: View instructions",
    ),

    StringField(
        name='proposerName',
        widget=StringField._properties['widget'](
            label="Student Proposer 1 Name",
            label_msgid='uwosh_grants_label_proposerName',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        searchable=1,
	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposerId',
	searchable=True,
	isMetadata=True,
        index='FieldIndex:schema',
        widget=StringField._properties['widget'](
            label="Proposer 1 Student ID #",
            label_msgid='uwosh_grants_label_proposerName',
            i18n_domain='uwosh_grants',
        ),
        required=1,
	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposerEmail',
        widget=StringField._properties['widget'](
            label="Student Proposer 1 Email",
            label_msgid='uwosh_grants_label_proposerEmail',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        validators=('isEmail',),
	write_permission="uwosh_grants: View proposer details",
    ),
    
TextField(
        name='mailingAddress1',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default="""<b>Student Proposer 1 Mailing Address</b>(Official award/deny letters will 
	be sent to this address.)<br/>""",
        widget=ReadOnlyRichWidget(
            label='Student Proposer 1 Mailing Address',
            label_msgid='uwosh_grants_label_instructions_mail_address',
            i18n_domain='uwosh_grants',
        ),
        default_output_type='text/html',
        modify="Manager",
	read_permission="uwosh_grants: View instructions",
    ),

    StringField(
        name='proposerMailAddressLine1',
        widget=StringField._properties['widget'](
            label="Address Line 1",
            label_msgid='uwosh_grants_label_proposerMailAddressLine1',
            i18n_domain='uwosh_grants',
        ),
        required=1,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposerMailAddressLine2',
        widget=StringField._properties['widget'](
            label="Address Line 2",
            label_msgid='uwosh_grants_label_proposerMailAddressLine2',
            i18n_domain='uwosh_grants',
        ),
        required=0,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposerCity',
        widget=StringField._properties['widget'](
            label="City",
            label_msgid='uwosh_grants_label_proposerCity',
            i18n_domain='uwosh_grants',
        ),
        required=1,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposerState',
        widget=StringField._properties['widget'](
            label="State",
            label_msgid='uwosh_grants_label_proposerState',
            i18n_domain='uwosh_grants',
        ),
        required=1,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposerZip',
        widget=StringField._properties['widget'](
            label="Zip Code",
            label_msgid='uwosh_grants_label_proposerZip',
            i18n_domain='uwosh_grants',
        ),
        required=1,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2Name',
        widget=StringField._properties['widget'](
            label="Student Proposer 2 Name",
            label_msgid='uwosh_grants_label_proposerName',
            i18n_domain='uwosh_grants',
        ),
        searchable=1,
	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2Id',
	searchable=True,
	isMetadata=True,
        index='FieldIndex:schema',
        widget=StringField._properties['widget'](
            label="Proposer 2 Student ID #",
            label_msgid='uwosh_grants_label_proposerName',
            i18n_domain='uwosh_grants',
        ),
	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2Email',
        widget=StringField._properties['widget'](
            label="Student Proposer 2 Email",
            label_msgid='uwosh_grants_label_proposerEmail',
            i18n_domain='uwosh_grants',
        ),
        validators=('isEmail',),
	write_permission="uwosh_grants: View proposer details",
    ),

TextField(
        name='mailingAddress2',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default="""<b>Student Proposer 2 Mailing Address</b>(Official award/deny letters will 
	be sent to this address.)<br/>""",
        widget=ReadOnlyRichWidget(
            label='Student Proposer 2 Mailing Address',
            label_msgid='uwosh_grants_label_instructions_mail_address',
            i18n_domain='uwosh_grants',
        ),
        default_output_type='text/html',
        modify="Manager",
	read_permission="uwosh_grants: View instructions",
    ),

    StringField(
        name='proposer2MailAddressLine1',
        widget=StringField._properties['widget'](
            label="Address Line 1",
            label_msgid='uwosh_grants_label_proposer2MailAddressLine1',
            i18n_domain='uwosh_grants',
        ),
        required=0,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2MailAddressLine2',
        widget=StringField._properties['widget'](
            label="Address Line 2",
            label_msgid='uwosh_grants_label_proposer2MailAddressLine2',
            i18n_domain='uwosh_grants',
        ),
        required=0,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2City',
        widget=StringField._properties['widget'](
            label="City",
            label_msgid='uwosh_grants_label_proposer2City',
            i18n_domain='uwosh_grants',
        ),
        required=0,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2State',
        widget=StringField._properties['widget'](
            label="State",
            label_msgid='uwosh_grants_label_proposer2State',
            i18n_domain='uwosh_grants',
        ),
        required=0,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='proposer2Zip',
        widget=StringField._properties['widget'](
            label="Zip Code",
            label_msgid='uwosh_grants_label_proposer2Zip',
            i18n_domain='uwosh_grants',
        ),
        required=0,
	default_output_type='text/html',
 	write_permission="uwosh_grants: View proposer details",
    ),

    StringField(
        name='primaryFacultyAdvisorName',
        widget=StringField._properties['widget'](
            label="Primary Advisor Name",
            label_msgid='uwosh_grants_label_primaryFacultyAdvisorName',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        searchable=1,
	write_permission="uwosh_grants: View faculty advisers",
        default_method="getProposerNameDefault",
    ),

    StringField(
        name='primaryFacultyAdvisorId',
        widget=StringField._properties['widget'](
            label="Primary Advisor Account",
            label_msgid='uwosh_grants_label_primaryFacultyAdvisorID',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        searchable=1,
	write_permission="uwosh_grants: View faculty advisers",
        default_method="getProposerIdDefault",
    ),

    StringField(
        name='primaryFacultyAdvisorEmail',
        widget=StringField._properties['widget'](
            label="Primary Advisor Email",
            label_msgid='uwosh_grants_label_proposerEmail',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        validators=('isEmail',),
	write_permission="uwosh_grants: View faculty advisers",
        default_method="getProposerEmailDefault",
    ),

    StringField(
        name='primaryFacultyAdvisorDept',
        widget=StringField._properties['widget'](
            label="Primary Advisor Department",
            label_msgid='uwosh_grants_label_primaryFacultyDept',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        searchable=1,
	write_permission="uwosh_grants: View faculty advisers",
    ),


    StringField(
        name='facultyAdvisor2Name',
        widget=StringField._properties['widget'](
            label="Advisor 2 Name",
            label_msgid='uwosh_grants_label_facultyAdvisor2Name',
            i18n_domain='uwosh_grants',
        ),
        searchable=1,
	write_permission="uwosh_grants: View faculty advisers",
    ),
    StringField(
        name='facultyAdvisor3Name',
        widget=StringField._properties['widget'](
            label="Advisor 3 Name",
            label_msgid='uwosh_grants_label_facultyAdvisor3Name',
            i18n_domain='uwosh_grants',
        ),
        searchable=1,
	write_permission="uwosh_grants: View faculty advisers",
    ),

    TextField(
        name='abstract',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Proposal Abstract",
	    description="(A summary of less than 250 words. See help for more info.)",
            label_msgid='uwosh_grants_label_abstract',
            i18n_domain='uwosh_grants',
        ),
        default_output_type='text/html',
        searchable=1,
    ),

    BooleanField(
        name='studentIsPrimaryAuthor',
        widget=BooleanField._properties['widget'](
            label="Advisor verification that the student was the primary author of this proposal",
            description="By checking this box the advisor is indicating that none of the advisors were the primary author(s) of this proposal. The student made a substantial contribution to the writing of this proposal.",
            label_msgid='uwosh_grants_label_studentIsPrimaryAuthor',
            description_msgid='uwosh_grants_help_studentIsPrimaryAuthor',
            i18n_domain='uwosh_grants',
        ),
        required_by_state=['directorReview'],
    ),

    StringField(
	name='awardTimeFrame',
	widget=SelectionWidget(
	    label="Award Requested For",
	    description="Select one",
	    label_msgid='uwosh_grants_awardTimeFrame',
	    description_msgid='uwosh_grants_help_awardTimeFrame',
	    i18n_domain='uwosh_grants',
	),
	required=1,
	vocabulary=['Summer','Academic Year', ],
	),

    TextField(
        name='upload',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default="""<b>Don't forget to save!</b><br>Click on the "Save" button below so that the data you 
	filled in above is not lost.  You will then be able to move on to step 2.  After saving you can edit 
	any incorrect data by clicking on the "edit" tab near the top.<br>""",
        widget=ReadOnlyRichWidget(
            label="",
            label_msgid='uwosh_grants_label_upload',
            i18n_domain='uwosh_grants',
        ),
        default_output_type='text/html',
        modify="Manager",
	read_permission="uwosh_grants: View instructions",
    ),
    StringField(
	name='facultyReviewer',
	widget=MultiSelectionWidget(
	    label="Faculty Reviewer",
	    description="Select the reviewers",
	    label_msgid='uwosh_grants_label_facultyReviewern',
	    description_msgid='uwosh_grants_help_facultyReviewer',
	    i18n_domain='uwosh_grants',
	),
	required=0,
	vocabulary='getProposalReviewersVocabulary',
	write_permission="uwosh_grants: Set reviewer permission",
	),
    StringField(
	name='proposalApproved',
	widget=SelectionWidget(
	    label="Proposal Status",
	    description="Select one",
	    label_msgid='uwosh_grants_label_proposalApproved',
	    description_msgid='uwosh_grants_help_proposalApproved',
	    i18n_domain='uwosh_grants',
	),
	required=0,
	vocabulary=['Pending','Denied','Alternate (approved pending availability of funds)', 'Approved',],
	write_permission="uwosh_grants: Set approved permission",
	),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema
schema["proposerName"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["proposerId"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["proposerEmail"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["instructions"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["primaryFacultyAdvisorName"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["primaryFacultyAdvisorId"].widget.visible={"edit": "invisible", "view": "invisible"}
schema["facultyAdvisor2Name"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["facultyAdvisor3Name"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["facultyReviewer"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["proposalApproved"].widget.visible = {"edit": "visible", "view": "invisible"}
schema["upload"].widget.visible = {"edit": "visible", "view": "invisible"}

Proposal_schema = BaseFolderSchema.copy() + \
    schema.copy()
Proposal_schema.moveField('title', direction=1)

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Proposal(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProposal)

    meta_type = 'Proposal'
    _at_rename_after_creation = True

    schema = Proposal_schema

    #logger = logging.getLogger('Proposal')

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    getProposalReviewersVocabulary = getProposalReviewersVocabulary

    def avgResearchQuestionOrCreativeGoal(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        #self.logger.info('Got %s review forms for proposal %s' % (numReviews, self.id))
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getResearchQuestionOrCreativeGoal())
            except:
                value = 0.0
            #self.logger.info('Value %s for review %s' % (value, form.id))
            accumulator = accumulator + value
        retval = accumulator / numReviews
        #self.logger.info('average is %s for review %s' % (retval, form.id))
        return retval

    def avgMethodologyAndDesign(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getMethodologyAndDesign())
            except:
                value = 0.0
            accumulator = accumulator + value
        return accumulator / numReviews

    def avgMotivation(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getMotivation())
            except:
                value = 0.0
            accumulator = accumulator + value
        return accumulator / numReviews

    def avgFeasibility(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getFeasibility())
            except:
                value = 0.0
            accumulator = accumulator + value
        return accumulator / numReviews

    def avgTimeline(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getTimeline())
            except:
                value = 0.0
            accumulator = accumulator + value
        return accumulator / numReviews

    def avgProjectOutcomes(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getProjectOutcomes())
            except:
                value = 0.0
            accumulator = accumulator + value
        return accumulator / numReviews

    def avgProposalQualityAndClarity(self):
        reviewForms = [o for o in self.objectValues() if ((o.portal_type == 'ReviewerForm') or (o.portal_type == 'ReviewerFormGrad'))]
        numReviews = len(reviewForms)
        if numReviews == 0:
            #raise ValueError, "No review forms exist for this proposal!"
            return 0
        accumulator = 0.0
        for form in reviewForms:
            try:
                value = float(form.getProposalQualityAndClarity())
            except:
                value = 0.0
            accumulator = accumulator + value
        return accumulator / numReviews

    def getProposerNameDefault(self):
        pm = self.portal_membership
        m = pm.getAuthenticatedMember()
        if m <> 'Anonymous User':
            return m.getProperty('fullname', '')

    def getProposerIdDefault(self):
        pm = self.portal_membership
        m = pm.getAuthenticatedMember()
        if m <> 'Anonymous User':
            return m.id

    def getProposerEmailDefault(self):
        pm = self.portal_membership
        m = pm.getAuthenticatedMember()
        if m <> 'Anonymous User':
            return m.getProperty('email', '')


registerType(Proposal, PROJECTNAME)
# end of class Proposal

##code-section module-footer #fill in your manual code here
##/code-section module-footer



