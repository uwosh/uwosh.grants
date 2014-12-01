# -*- coding: utf-8 -*-
#
# File: ReviewerForm.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
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
from Products.ATVocabularyManager import NamedVocabulary

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='researchQuestionOrCreativeGoal',
        widget=SelectionWidget(
            label="Research Question or Creative Goal",
            description="Does the proposal spell out the hypothesis to test, or the theorem to prove, or the issue to examine, or the creation to develop? Does it describe the state of knowledge within the discipline and what new learning or new knowledge the project will result in?",
            label_msgid='uwosh_grants_label_researchQuestionOrCreativeGoal',
            description_msgid='uwosh_grants_help_researchQuestionOrCreativeGoal',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='methodologyAndDesign',
        widget=SelectionWidget(
            label="Methodology and Design",
            description="Does the proposal spell out the proposed research process, identifying the techniques to be used, and the sequence of steps to be taken? Does it show how these steps will lead to completing the research goal? Does it clearly identify the student’s role in the research?",
            label_msgid='uwosh_grants_label_methodologyAndDesign',
            description_msgid='uwosh_grants_help_methodologyAndDesign',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='motivation',
        widget=SelectionWidget(
            label="Motivation",
            description="Does the proposal discuss why the student is interested in this particular project, and why the project is appropriate for this particular student? Does it describe the link between this research project and both the student’s learning history, as well as the student’s future learning and goals?",
            label_msgid='uwosh_grants_label_motivation',
            description_msgid='uwosh_grants_help_motivation',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='feasibility',
        widget=SelectionWidget(
            label="Feasibility",
            description="Does the proposal discuss why the project is appropriate to student’s skills and abilities? Does it have appropriate mentor supervision/training; and (if appropriate) needed equipment and facilities?",
            label_msgid='uwosh_grants_label_feasibility',
            description_msgid='uwosh_grants_help_feasibility',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='timeline',
        widget=SelectionWidget(
            label="Time Line",
            description="Does the proposal present a reasonable time line for the research to be completed?",
            label_msgid='uwosh_grants_label_timeline',
            description_msgid='uwosh_grants_help_timeline',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='projectOutcomes',
        widget=SelectionWidget(
            label="Project Outcomes",
            description="Does the proposal specify the project’s tangible outcomes, appropriate to the type of project, including an appropriate outlet for presenting the project’s outcomes to the University community?",
            label_msgid='uwosh_grants_label_projectOutcomes',
            description_msgid='uwosh_grants_help_projectOutcomes',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='proposalQualityAndClarity',
        widget=SelectionWidget(
            label="Proposal Quality and Clarity",
            description="Are all the ideas clear and understandable to readers outside the discipline? Are technical terms avoided or explained? Is the proposal well organized, logical, and free of spelling and grammatical errors?",
            label_msgid='uwosh_grants_label_proposalQualityAndClarity',
            description_msgid='uwosh_grants_help_proposalQualityAndClarity',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponse"""),
    ),
    StringField(
        name='holisticEvaluation',
        widget=SelectionWidget(
            label="Holistic Evaluation",
            description="Select whichever applies",
            label_msgid='uwosh_grants_label_holisticEvaluation',
            description_msgid='uwosh_grants_help_holisticEvaluation',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        vocabulary=NamedVocabulary("""ReviewFormResponseHolistic"""),
    ),
    TextField(
        name='comment',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            description="To provide the student with feedback, please comment on the proposal’s strengths as well as its major deficiencies. Reviews without comments will be taken less seriously by the final review panel.",
            label='Comment',
            label_msgid='uwosh_grants_label_comment',
            description_msgid='uwosh_grants_help_comment',
            i18n_domain='uwosh_grants',
        ),
        default_output_type='text/html',
    ),
    StringField(
        name='reviewer',
        searchable=True,
	isMetadata=True,
	index='FieldIndex:schema',
        widget=SelectionWidget(
            label="Reviewer",
            description="",
            label_msgid='uwosh_grants_label_reviewer',
            description_msgid='uwosh_grants_help_reviewer',
            i18n_domain='uwosh_grants',
        ),
        required=1,
        enforce_vocabulary=1,
        vocabulary='getProposalReviewersVocabulary',
        write_permission="uwosh_grants: Set reviewer permission",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ReviewerForm_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ReviewerForm(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IReviewerForm)

    meta_type = 'ReviewerForm'
    _at_rename_after_creation = True

    schema = ReviewerForm_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    getProposalReviewersVocabulary = getProposalReviewersVocabulary

registerType(ReviewerForm, PROJECTNAME)
# end of class ReviewerForm

##code-section module-footer #fill in your manual code here
##/code-section module-footer



