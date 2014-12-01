# -*- coding: utf-8 -*-
#
# File: ReviewerFormGrad.py
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
            label="Intellectual or Creative Merit**",
            description="The proposal should clearly explain the project’s intellectual or creative merit, how the project is grounded in the theory and/or literature of the discipline, and the significance/importance/contribution of the project to the discipline",
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
            label="Methodology/Design",
            description="The proposal should clearly explain the project’s research design; e.g. the hypotheses to be tested, questions to be explored, or creative activity to be undertaken, and the processes that will be used.  This description should also spell out the roles of both the graduate student and mentors in the project.",
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
            description="The proposal should describe why this project is appropriate for the student i.e. how it ties into the student’s own learning, career interests and projected career path.",
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
            label="Feasibility**",
            description="The proposal should (1) show that the student has, or can acquire, the necessary skills and knowledge for the project, (2) ensure a faculty mentor will provide appropriate supervision and training, (3) show that required equipment, materials, software and library resources are available or accessible,  and (4) demonstrate that other special arrangements (if necessary) have been made.",
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
            description="The proposal should spell out the time line over which the project be carried out, including an estimate of how long each methodological step will take.",
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
            description="The proposal should specify the project’s expected outcomes  (e.g., papers, artistic or creative works, models, proposals for extramural funding, demonstrations, exhibitions and manuals).  Outcomes should be appropriate to the project and the discipline and be achievable by the student.",
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
            description="The proposal should avoid jargon, define terms and concepts (where appropriate), and be proofread for organization, grammar, and clarity.",
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

ReviewerFormGrad_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ReviewerFormGrad(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IReviewerFormGrad)

    meta_type = 'ReviewerFormGrad'
    _at_rename_after_creation = True

    schema = ReviewerFormGrad_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    getProposalReviewersVocabulary = getProposalReviewersVocabulary


registerType(ReviewerFormGrad, PROJECTNAME)

##code-section module-footer #fill in your manual code here
##/code-section module-footer



