from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize

class CommonViewStuff(BrowserView):
    #@memoize
    pass

class ViewAll(CommonViewStuff):
    template = ViewPageTemplateFile('proposals_list.pt')
    
    def update(self):
        pass
    
class ReviewView(CommonViewStuff):
    __call__ = ViewPageTemplateFile('review_forms_average.pt')


