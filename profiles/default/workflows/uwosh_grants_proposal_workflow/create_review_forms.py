def create_review_forms(self,state_change,**kw):
    obj = state_change.object
    obj.invokeFactory(type_name="ReviewerForm", id="Reviewer1")
    obj.invokeFactory(type_name="ReviewerForm", id="Reviewer2")
    obj.invokeFactory(type_name="ReviewerForm", id="Reviewer3")
    obj.invokeFactory(type_name="ReviewerForm", id="Reviewer4")