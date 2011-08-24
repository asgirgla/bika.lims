from Products.validation import validation
from bika.lims.content.validators import *
validation.register(FormulaValidator("formula_validator"))
validation.register(ServiceKeywordValidator("service_keyword_validator"))
validation.register(InterimFieldTitleValidator("interim_field_title_validator"))

# import this to create messages in the bika domain.
from zope.i18nmessageid import MessageFactory
bikaMessageFactory = MessageFactory('bika')
# import this to log messages
import logging
logger = logging.getLogger('Bika')

from bika.lims.validators import *

from AccessControl import ModuleSecurityInfo, allow_module
from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.utils import ContentInit, ToolInit, getToolByName
from Products.CMFPlone import PloneMessageFactory
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.GenericSetup import EXTENSION, profile_registry

from bika.lims.config import *
from content import *
from controlpanel import *

allow_module('bika.lims')
allow_module('AccessControl')

def initialize(context):

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    ContentInit(
        PROJECTNAME,
        content_types = content_types,
        permission = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti = ftis,
        ).initialize(context)
